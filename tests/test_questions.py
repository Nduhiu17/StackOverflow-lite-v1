import json
import unittest
from datetime import datetime

from app import app
from app.database import drop_questions_table, drop_answers_table, create_questions_table, create_answers_table, \
    create_users_table, drop_users_table
from app.models import Question
from config import TestingConfig
from tests.helper_functions import register_user, login_user, post_quiz


class TestQuestion(unittest.TestCase):
    '''class to test a question'''

    def tearDown(self):
        drop_users_table()
        drop_questions_table()
        drop_answers_table()
        create_users_table()
        create_questions_table()
        create_answers_table()

    def setUp(self):
        # setting up configurations for testing
        self.app = app
        self.app.config.from_object(TestingConfig)
        self.new_question = Question(id=4, title="how to init python",
                                     body="how to init python how to init python how to init python", user_id=1,
                                     date_created=datetime.now(), date_modified=datetime.now())
        self.client = self.app.test_client()
        self.app.testing = True
        register_user(self)
        response = login_user(self)
        self.token = json.loads(response.data.decode())['access_token']

    def test_init(self):
        # test that a question is initialized
        self.new_question = Question(id=4, title="how to init python",
                                     body="how to init python how to init python how to init python", user_id=1,
                                     date_created=datetime.now(), date_modified=datetime.now())
        self.assertTrue(type(self.new_question.id), int)
        self.assertEqual(type(self.new_question), Question)

    def test_question_posted(self):
        # method to test a question can be posted
        response = post_quiz(self)
        self.assertEqual(response.status_code, 201)

    def test__post_invalid_title(self):
        response = login_user(self)
        result = json.loads(response.data)
        self.assertIn("access_token", result)
        new_question = {'title': 'sh',
                        'body': 'error sit voluptatem accusantium doloremque laudantiumerror sit volupta', 'user_id': 1}
        response = self.client.post('api/v1/questions', data=json.dumps(new_question),
                                    headers={'Authorization': f'Bearer {result["access_token"]}',
                                             'Content-Type': 'application' '/json'})
        self.assertEqual(response.status_code, 400)

    def test__post_invalid_title_(self):
        response = login_user(self)
        result = json.loads(response.data)
        self.assertIn("access_token", result)
        new_question = {'title': "hj",
                        'body': 'error sit voluptatem accusantium doloremque laudantiumerror sit volupta', 'user_id': 1}
        response = self.client.post('api/v1/questions', data=json.dumps(new_question),
                                    headers={'Authorization': f'Bearer {result["access_token"]}',
                                             'Content-Type': 'application' '/json'})
        self.assertEqual(response.status_code, 400)

    def test__post_invalid_title_int(self):
        response = login_user(self)
        result = json.loads(response.data)
        self.assertIn("access_token", result)
        new_question = {'title': 111111111111111,
                        'body': 'error sit voluptatem accusantium doloremque laudantiumerror sit volupta', 'user_id': 1}
        response = self.client.post('api/v1/questions', data=json.dumps(new_question),
                                    headers={'Authorization': f'Bearer {result["access_token"]}',
                                             'Content-Type': 'application' '/json'})
        self.assertEqual(response.status_code, 400)

    def test_post_invalid_body(self):
        response = login_user(self)
        result = json.loads(response.data)
        self.assertIn("access_token", result)
        new_question = {'title': 'error sit voluptatem accusantium doloremque laudantium',
                        'body': 'error', 'user_id': 1}
        response = self.client.post('api/v1/questions', data=json.dumps(new_question),
                                    headers={'Authorization': f'Bearer {result["access_token"]}',
                                             'Content-Type': 'application' '/json'})
        self.assertEqual(response.status_code, 400)

    def test_get_a_single_question(self):
        post_quiz(self)
        response = self.client.get(f'api/v1/questions/1', content_type='application/json')
        result = json.loads(response.data.decode())
        self.assertEqual(response.status_code, 200)

    def test_get_non_existing_question(self):
        response = self.client.get(f'api/v1/questions/145678', content_type='application/json')
        result = json.loads(response.data.decode())
        self.assertEqual(response.status_code, 404)

    def test_get_all_questions(self):
        # test can get all questions
        response = self.client.get('/api/v1/questions', content_type='application/json')
        self.assertEqual(response.status_code, 200)
        self.assertTrue(type(response), list)
