import json
import unittest
from datetime import datetime

from app import app
from app.database import create_questions_table, create_answers_table, drop_questions_table, drop_answers_table, \
    create_users_table
from app.models import Question, Answer
from config import TestingConfig
from tests.helper_functions import post_quiz, register_user


class TestAnswer(unittest.TestCase):
    '''class to test an answer'''

    def tearDown(self):
        drop_questions_table()
        drop_answers_table()
        create_users_table()
        create_questions_table()
        create_answers_table()

    def setUp(self):
        # setting up configurations for testing
        create_questions_table()
        create_answers_table()
        self.app = app
        self.app.config.from_object(TestingConfig)
        self.client = self.app.test_client()
        register_user(self)
        post_quiz(self)
        self.client = self.app.test_client()
        self.app.testing = True

    def test_answer_posted(self):
        # test that an answer can be posted
        new_answer = {'body': 'error sit voluptatem accusantium doloremque laudantiumerror sit volupta',
                      'question_id': '1'}
        response = self.client.post(f'/api/v1/questions/{1}/anwsers', data=json.dumps(new_answer),
                                    headers={'Content-Type': 'application' '/json'})
        self.assertEqual(response.status_code, 201)

    def test_post_short_answer_body(self):
        # test cant post invalid short answer
        new_answer = {'body': 'short body'}
        response = self.client.post(f'/api/v1/questions/{1}/anwsers', data=json.dumps(new_answer),
                                    headers={'Content-Type': 'application' '/json'})
        self.assertEqual(response.status_code, 400)

    def test_cant_post_to_no_question(self):
        # test can't post an answer to no question
        new_answer = {'body': 'error sit voluptatem accusantium doloremque laudantiumerror sit volupta'}
        response = self.client.post('/api/v1/questions/1254/anwsers', data=json.dumps(new_answer),
                                    headers={'Content-Type': 'application' '/json'})
        self.assertEqual(response.status_code, 404)

    def test_init(self):
        # test that an answer is initialized
        self.new_answer = Answer(id=1, body="how to init python how to init python how to init python", question_id=1,
                                 date_created=datetime.now(), date_modified=datetime.now())
        self.assertTrue(type(self.new_answer.id), int)
        self.assertEqual(type(self.new_answer), Answer)
