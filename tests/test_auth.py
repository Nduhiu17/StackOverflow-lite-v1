import json
import unittest
from datetime import datetime

from app import app
from app.database import drop_questions_table, drop_answers_table, create_questions_table, create_answers_table, \
    drop_users_table, create_users_table
from app.models import User
from config import TestingConfig


class TestUser(unittest.TestCase):
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
        self.new_user = User.save(self, username="username",
                                  email="username@gmail.com", password="User.generate_hash(password)",
                                  date_created=datetime.now(), date_modified=datetime.now())

        self.client = self.app.test_client()
        self.app.testing = True

    def test_init(self):
        # test that a user is initialized
        self.new_user = User(username="username",
                             email="username@gmail.com", password="pasword",
                             date_created=datetime.now(), date_modified=datetime.now())
        self.assertTrue(type(self.new_user.id), int)
        self.assertEqual(type(self.new_user), User)

    def test_register(self):
        # Test can register a user
        new_user = {'username': 'username2', 'email': 'username2@email.com', 'password': 'password'}
        response = self.client.post('auth/signup',
                                    data=json.dumps(new_user), content_type='application/json')
        self.assertEqual(response.status_code, 201)

    def test_register_username_twice(self):
        # Test can register a username twice
        new_user = {'username': 'username', 'email': 'username@email.com', 'password': 'password'}
        response = self.client.post('auth/signup',
                                    data=json.dumps(new_user), content_type='application/json')
        self.assertEqual(response.status_code, 409)

    def test_register_email_twice(self):
        # Test can register a user an email  twice
        new_user = {'username': 'usernameert', 'email': 'username@gmail.com', 'password': 'password'}
        response = self.client.post('auth/signup',
                                    data=json.dumps(new_user), content_type='application/json')
        self.assertEqual(response.status_code, 409)

    def test_invalid_password(self):
        # Test cant register with no password
        response = self.client.post('auth/signup',
                                    data=json.dumps(
                                        {'username': 'username', 'email': 'username@mail.com', 'password': ''}),
                                    content_type='application/json')
        self.assertEqual(response.status_code, 400)

    def test_invalid_username(self):
        # Test cant register with invalid username
        response = self.client.post('auth/signup',
                                    data=json.dumps(
                                        {'username': 12365478875, 'email': 'username@mail.com', 'password': ''}),
                                    content_type='application/json')
        self.assertEqual(response.status_code, 400)

    def test_invalid_username2(self):
        # Test cant register with invalid username
        response = self.client.post('auth/signup',
                                    data=json.dumps(
                                        {'username': 'jk', 'email': 'username@mail.com', 'password': ''}),
                                    content_type='application/json')
        self.assertEqual(response.status_code, 400)

    def test_invalid_email(self):
        # Test cant register with invalid email
        response = self.client.post('auth/signup',
                                    data=json.dumps(
                                        {'username': 'username', 'email': 'usernameailcom', 'password': ''}),
                                    content_type='application/json')
        self.assertEqual(response.status_code, 400)

    def test_user_not_found(self):
        # test cant login a non user
        response = self.client.post('auth/login',
                                    data=json.dumps(
                                        {'username': 'username2', 'password': 'password'}),
                                    content_type='application/json')
        self.assertEqual(response.status_code, 404)

    def test_invalid_password_int(self):
        # test cant register with an invalid password
        response = self.client.post('auth/signup',
                                    data=json.dumps(
                                        {'username': "fghjklfghjk", 'email': 'username@mailcom', 'password': 1235455}),
                                    content_type='application/json')
        self.assertEqual(response.status_code, 400)

    def test_login_incorrect_username(self):
        # Test can't login with wrong username
        new_user = {'username': 'usernam', 'email': 'usernam@email.com', 'password': 'password'}
        response = self.client.post('auth/signup',
                                    data=json.dumps(new_user), content_type='application/json')
        self.assertEqual(response.status_code, 201)
        response2 = self.client.post('auth/login',
                                     data=json.dumps(
                                         {'username': 'usernam', 'password': 'passwo'}),
                                     content_type='application/json')
        self.assertEqual(response2.status_code, 403)

    def test_wrong_register_email(self):
        # Test can't  register a wrong email
        new_user = {'username': 'username', 'email': 455, 'password': 'password'}
        response = self.client.post('auth/signup',
                                    data=json.dumps(new_user), content_type='application/json')
        self.assertEqual(response.status_code, 400)
