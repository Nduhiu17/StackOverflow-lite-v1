import json
import unittest
from datetime import datetime

from app import app
from app.database import create_questions_table, create_answers_table, drop_questions_table, drop_answers_table, \
    create_users_table
from app.models import Answer
from config import TestingConfig
from tests.helper_functions import post_quiz, register_user, login_user, post_answer


class TestAnswer(unittest.TestCase):
    '''class to test an answer'''

    def tearDown(self):
        drop_questions_table()
        drop_answers_table()
        create_users_table()
        create_questions_table()
        create_answers_table()

    def test_init(self):
        '''test that an answer is initialized'''
        self.new_answer = Answer(id=1, body="how to init python how to init python how to init python", question_id=1,
                                 user_id=1,
                                 date_created=datetime.now(), date_modified=datetime.now(),accept=False)
        self.assertTrue(type(self.new_answer.id), int)
        self.assertEqual(type(self.new_answer), Answer)

    def setUp(self):
        '''setting up configurations for testing'''
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
        '''test that an answer can be posted'''
        response = login_user(self)
        result = json.loads(response.data)
        self.assertIn("access_token", result)
        new_answer = {'body': 'errossssssssssssssssssssssssssssssssssssssssssssssssss','accept':False}
        response = self.client.post('/api/v1/questions/1/answers', data=json.dumps(new_answer),
                                    headers={'Authorization': f'Bearer {result["access_token"]}',
                                             'Content-Type': 'application' '/json'})
        self.assertEqual(response.status_code, 201)

    def test_post_short_answer_body(self):
        '''test cant post invalid short answer'''
        response = login_user(self)
        result = json.loads(response.data)
        self.assertIn("access_token", result)
        new_answer = {'body': 'erro'}
        response = self.client.post('/api/v1/questions/2/answers', data=json.dumps(new_answer),
                                    headers={'Authorization': f'Bearer {result["access_token"]}',
                                             'Content-Type': 'application' '/json'})
        self.assertEqual(response.status_code, 400)

    def test_cant_post_to_no_question(self):
        '''test cant post an answer to unavailable question'''
        response = post_answer(self)
        self.assertEqual(response.status_code, 404)

    def test_cant_modify_no_answer(self):
        '''test that you can't modify non-answer'''
        response = login_user(self)
        result = json.loads(response.data)
        self.assertIn("access_token", result)
        answer = {'body': 'errojjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjj'}
        response = self.client.post('/api/v1/questions/2/anwsers', data=json.dumps(answer),
                                    headers={'Authorization': f'Bearer {result["access_token"]}',
                                             'Content-Type': 'application' '/json'})
        new_answer = {'body':'rrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrr'}
        response2 = self.client.put('/api/v1/questions/2/anwsers/1', data=json.dumps(new_answer),
                                    headers={'Authorization': f'Bearer {result["access_token"]}',
                                             'Content-Type': 'application' '/json'})
        self.assertEqual(response.status_code, 404)








