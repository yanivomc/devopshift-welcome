import unittest
import requests

class TestFlaskApiUsingRequests(unittest.TestCase):
    def setUp(self):
        self.base_url = "http://localhost:8080"  # Ensure this matches the port and host of your Flask app

    def test_index(self):
        # Test the main page
        response = requests.get(self.base_url)
        self.assertEqual(response.status_code, 200)

    def test_health_check(self):
        # Test the health check route
        response = requests.get(f"{self.base_url}/health")
        self.assertEqual(response.status_code, 200)
        self.assertIn("Application is up and running!", response.text)

if __name__ == "__main__":
    unittest.main()
