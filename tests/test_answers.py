import json
import unittest
from app import app
from app.models import Answer, MOCK_DATABASE
from config import TestingConfig


class TestAnswer(unittest.TestCase):
    '''class to test an answer'''

    def setUp(self):
        # setting up configurations for testing
        self.app = app
        self.app.config.from_object(TestingConfig)
        self.client = self.app.test_client()
        self.app.testing = True

    def tearDown(self):
        pass

    def test_init(self):
        # test that an answer is initialized
        question = MOCK_DATABASE[ 'questions' ][ 0 ]
        self.new_answer = Answer(body="This is how to init python how to init python how to init python",question_id=question.id)
        self.assertTrue(type(self.new_answer.id), int)
        self.assertEqual(type(self.new_answer), Answer)

    def test_answer_posted(self):
        # method to test an answer can be posted
        question_to_answer =  MOCK_DATABASE['questions'][0]
        new_answer = {'body': 'error sit voluptatem accusantium doloremque laudantiumerror sit volupta'}
        response = self.client.post(f'/api/v1/questions/{question_to_answer.id}/anwsers', data=json.dumps(new_answer),headers={'Content-Type': 'application' '/json'})
        self.assertEqual(response.status_code, 201)

    def test_post_short_answer_body(self):
        # test cant post with a short answer body
        question_to_answer = MOCK_DATABASE[ 'questions' ][ 0 ]
        new_answer = {'body': 'short body'}
        response = self.client.post(f'/api/v1/questions/{question_to_answer.id}/anwsers', data=json.dumps(new_answer),
                                    headers={'Content-Type': 'application' '/json'})
        self.assertEqual(response.status_code, 400)

    def test_cant_post_to_no_question(self):
        # method to test you can post an answer to a non question
        question_to_answer = MOCK_DATABASE[ 'questions' ][ 0 ]
        new_answer = {'body': 'error sit voluptatem accusantium doloremque laudantiumerror sit volupta'}
        response = self.client.post('/api/v1/questions/1254/anwsers', data=json.dumps(new_answer),
                                    headers={'Content-Type': 'application' '/json'})
        self.assertEqual(response.status_code, 404)