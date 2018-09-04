import json
import unittest
from app import app
from config import TestingConfig


class TestQuestion(unittest.TestCase):
    '''class to test a question'''
    def setUp(self):
        #setting up configurations for testing
        self.app = app
        self.app.config.from_object(TestingConfig)
        self.client = self.app.test_client()
        self.app.testing = True

    def tearDown(self):
        pass

    def test_errror_404_handler(self):
        # method to test error 404 handler
        new_question = {'title': 'error sit voluptatem accusantium doloremque laudantium',
                        'body': 'error sit voluptatem accusantium doloremque laudantiumerror sit volupta'}
        response = self.client.post('api/v1/questionsm#@$', data=json.dumps(new_question),
                                    headers={'Content-Type': 'application' '/json'})
        self.assertEqual(response.status_code, 404)