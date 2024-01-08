# test_app.py
import unittest
from unittest.mock import patch
from server import app

# Mock classes for simulating database interactions
class MockedConnection:
    def cursor(self):
        return MockedCursor()

    def close(self):
        pass

class MockedCursor:
    def execute(self, query, params=None):
        pass

    def close(self):
        pass

class MockedMySQLConnector:
    def connect(self, **kwargs):
        return MockedConnection()

class AppTestCase(unittest.TestCase):

    def setUp(self):
        self.client = app.test_client()
        self.client.testing = True

    def test_home_status_code(self):
        result = self.client.get('/')
        self.assertEqual(result.status_code, 200)

    @patch('server.mysql.connector')
    def test_health_route(self, mock_db_connector):
        # Mock the mysql.connector to use our MockedMySQLConnector
        mock_db_connector.MySQLConnection = MockedConnection
        mock_db_connector.connect = MockedMySQLConnector().connect
        
        # Now when '/health' is accessed, it should use the mock connection
        result = self.client.get('/health')
        self.assertEqual(result.status_code, 200)
        self.assertIn("Application is up and running!", result.data.decode())

    @patch('server.save_user_to_database')
    def test_save_user(self, mock_save):
        # Mock the save_user_to_database function to do nothing
        mock_save.return_value = None

        # Send a POST request to the server's save_user route
        result = self.client.post('/', data={'name': 'John', 'address': '123 Elm Street'})
        
        # Assert that the request was successful
        self.assertEqual(result.status_code, 200)
        # Assert the mock was called with the correct arguments
        mock_save.assert_called_with('John', '123 Elm Street')

if __name__ == '__main__':
    unittest.main()
