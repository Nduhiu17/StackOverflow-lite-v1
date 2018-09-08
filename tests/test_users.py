import unittest
from app import app
from config import TestingConfig
import json

from app.models import User, MOCK_DATABASE


class TestUser(unittest.TestCase):

    def setUp(self):
        self.app = app
        self.app.config.from_object(TestingConfig)
        self.client = self.app.test_client()
        self.app.testing = True

    def tearDown(self):
        MOCK_DATABASE['users'] = []

    def test_init(self):
        # test a user is initialised
        self.new_user = User(username="Jane", email="jane@mail.com", password="password")
        self.assertTrue(type(self.new_user.id), int)
        self.assertEqual(type(self.new_user), User)

    def test_save(self):
        self.assertTrue(len(MOCK_DATABASE['users']) > 0)

    def test_user_saved(self):
        # method to test a user can be registered
        new_user = {'username': 'Testusername', 'email': 'test@mail.com', 'password': 'Mypassword'}
        response = self.client.post('api/v1/users', data=json.dumps(new_user),
                                    headers={'Content-Type': 'application' '/json'})
        self.assertEqual(response.status_code, 201)

    def test__save_invalid_username(self):
        # test cant save with an invalid username
        new_user = {'username': 'ndu', 'email': 'nduhiu254@gmail.com', 'password': 'password'}
        response = self.client.post('api/v1/users', data=json.dumps(new_user),
                                    headers={'Content-Type': 'application' '/json'})
        self.assertEqual(response.status_code, 400)

    def test_get_users(self):
        # test can get all users
        response = self.client.get('/api/v1/users', content_type='application/json')
        self.assertEqual(response.status_code, 200)
