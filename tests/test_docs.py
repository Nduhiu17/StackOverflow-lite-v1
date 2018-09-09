import unittest
from app import app
from config import TestingConfig


class TestAnswer(unittest.TestCase):
    '''class to test an answer'''

    def setUp(self):
        # setting up configurations for testing
        self.app = app
        self.app.config.from_object(TestingConfig)
        self.client = self.app.test_client()
        self.app.testing = True

    def test_docs(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)