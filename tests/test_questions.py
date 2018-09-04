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

    def test_question_posted(self):
            # method to test a question can be posted
        new_question = {'title': 'error sit voluptatem accusantium doloremque laudantium',
                        'body': 'error sit voluptatem accusantium doloremque laudantiumerror sit volupta'}
        response = self.client.post('api/v1/questions', data=json.dumps(new_question),
                                    headers={'Content-Type': 'application' '/json'})
        self.assertEqual(response.status_code, 201)

    def test__post_invalid_title(self):
            # test cant post with an invalid title
        new_question = {'title': 'shotitle',
                        'body': 'error sit voluptatem accusantium doloremque laudantiumerror sit voluptatem accusantium doloremque laudantium'}
        response = self.client.post('api/v1/questions', data=json.dumps(new_question),
                                    headers={'Content-Type': 'application' '/json'})
        self.assertEqual(response.status_code, 400)

    def test_post_invalid_body(self):
        # test cant post with an invalid body
        new_question = {'title': 'error sit voluptatem accusantium doloremque laudantium',
                        'body': 'short body'}
        response = self.client.post('api/v1/questions', data=json.dumps(new_question),
                                    headers={'Content-Type': 'application' '/json'})
        self.assertEqual(response.status_code, 400)

    def test_get_a_single_question(self):
        #method to get a single question
        question = MOCK_DATABASE['questions'][0]
        response = self.client.get(f'api/v1/questions/{question.id}',content_type='application/json')
        result = json.loads(response.data.decode())
        self.assertEqual(response.status_code, 200)

    def test_get_non_existing_question(self):
        question = MOCK_DATABASE[ 'questions' ][ 0 ]
        response = self.client.get(f'api/v1/questions/gggggg-ggggggggg-gggggggg', content_type='application/json')
        result = json.loads(response.data.decode())
        self.assertEqual(response.status_code, 404)

    def test_get_all_questions(self):
            # test can get all questions
        response = self.client.get('/api/v1/questions', content_type='application/json')
        self.assertEqual(response.status_code, 200)