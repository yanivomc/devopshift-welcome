import sys
import os

# Add the src directory to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import pytest
import json
from unittest.mock import patch
from mainbe import app, save_to_db, get_crypto_prices  # Ensure correct import

@pytest.fixture
def client():
    """Flask test client setup"""
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

@patch('mainbe.requests.get')
def test_get_crypto_prices(mock_get):
    """Test CoinGecko API call with mock response"""
    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value = {
        "bitcoin": {"usd": 50000},
        "xrp": {"usd": 0.60}
    }

    result = get_crypto_prices()
    assert result["bitcoin"]["usd"] == 50000
    assert result["xrp"]["usd"] == 0.60

def test_fetch_price(client, mocker):
    """Test /fetch_price endpoint with mocked CoinGecko response"""
    mocker.patch('mainbe.get_crypto_prices', return_value={
        "bitcoin": {"usd": 50000},
        "xrp": {"usd": 0.60}
    })
    
    mocker.patch('mainbe.save_to_db', return_value=True)  # Simulate DB success
    
    response = client.get('/fetch_price')
    assert response.status_code == 200

    data = json.loads(response.data)
    assert data[0]["coin"] == "bitcoin"
    assert data[0]["price"] == 50000
    assert data[0]["saved"] is True

def test_fetch_price_api_failure(client, mocker):
    """Test /fetch_price failure when API call fails"""
    mocker.patch('mainbe.get_crypto_prices', return_value={})  # Simulate API failure
    
    response = client.get('/fetch_price')
    assert response.status_code == 500
    assert json.loads(response.data) == {"error": "Failed to fetch prices"}

@patch('mainbe.mysql.connector.connect')
def test_save_to_db(mock_db):
    """Test database insertion logic"""
    mock_cursor = mock_db.return_value.cursor.return_value
    mock_cursor.execute.return_value = None  # Simulate successful execution
    
    success = save_to_db("bitcoin", 50000)
    assert success is True
