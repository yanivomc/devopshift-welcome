import sys
import os

# Add the src directory to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import pytest
from mainfe import app  # Assuming the frontend is a Flask app

@pytest.fixture
def client():
    """Create a test client using Flask's test client"""
    with app.test_client() as client:
        yield client

def test_homepage(client):
    """Test if homepage loads successfully"""
    response = client.get("/")
    assert response.status_code == 200
    assert b"Fetch Prices" in response.data  # Adjust based on actual page content

def test_invalid_route(client):
    """Test an invalid route returns 404"""
    response = client.get("/nonexistent")
    assert response.status_code == 404

def test_api_response(client):
    """Test a sample API endpoint"""
    response = client.get("/api/status")  # Replace with an actual endpoint
    assert response.status_code == 200
    assert response.json.get("status") == "OK"  # Adjust based on your API response
