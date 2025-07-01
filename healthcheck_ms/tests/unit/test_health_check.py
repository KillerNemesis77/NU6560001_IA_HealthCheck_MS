import unittest
from flask import Flask
from app.api.health_check import health_check

class TestHealthCheck(unittest.TestCase):
    def setUp(self):
        self.app = Flask(__name__)
        self.app.testing = True
        self.client = self.app.test_client()
        self.app.add_url_rule('/health', 'health', health_check)

    def test_health_check(self):
        response = self.client.get('/health')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.get_json(), {"status": "healthy"})