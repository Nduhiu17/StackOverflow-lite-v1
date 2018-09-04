import json
import unittest
from app import app
from app.models import Question, MOCK_DATABASE
from config import TestingConfig


class TestQuestion(unittest.TestCase):
    '''class to test a question'''

    def setUp(self):
        # setting up configurations for testing
        self.app = app
        self.app.config.from_object(TestingConfig)
        self.client = self.app.test_client()
        self.app.testing = True

    def tearDown(self):
        pass

    def test_init(self):
        # test that a question is initialized
        self.new_question = Question(title="how to init python",
                                     body="how to init python how to init python how to init python")
        self.assertTrue(type(self.new_question.id), int)
        self.assertEqual(type(self.new_question), Question)