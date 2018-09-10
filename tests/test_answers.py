import json
import unittest
from datetime import datetime

from app import app
from app.models import Answer, MOCK_DATABASE, Question
from config import TestingConfig


class TestAnswer(unittest.TestCase):
    '''class to test an answer'''

    def setUp(self):
        # setting up configurations for testing
        self.app = app
        self.app.config.from_object(TestingConfig)
        self.new_question = Question(id=4, title="how to init python",
                                     body="how to init python how to init python how to init python",
                                     date_created=datetime.now(), date_modified=datetime.now())
        self.new_question.save('self', 'title', 'body', 'date_created', 'date_modified')
        self.client = self.app.test_client()
        self.app.testing = True

    def tearDown(self):
        MOCK_DATABASE = dict(questions=[], answers=[], users=[])

    # def test_init(self):
    #     # test that an answer is initialized
    #     question = MOCK_DATABASE['questions'][0]
    #     self.new_answer = Answer(body="This is how to init python how to init python how to init python",
    #                              question_id=question.id)
    #     self.assertTrue(type(self.new_answer.id), int)
    #     self.assertEqual(type(self.new_answer), Answer)

    def test_answer_posted(self):
        # method to test an answer can be posted
        # question_to_answer = Question.get_by_id(1)
        # print("this is the ques",question_to_answer)
        new_answer = {'body': 'error sit voluptatem accusantium doloremque laudantiumerror sit volupta','question_id':'1'}
        response = self.client.post(f'/api/v1/questions/{1}/anwsers', data=json.dumps(new_answer),
                                    headers={'Content-Type': 'application' '/json'})
        self.assertEqual(response.status_code, 201)

    def test_post_short_answer_body(self):
        # test cant post with a short answer body
        # question_to_answer = MOCK_DATABASE['questions'][0]
        new_answer = {'body': 'short body'}
        response = self.client.post(f'/api/v1/questions/{1}/anwsers', data=json.dumps(new_answer),
                                    headers={'Content-Type': 'application' '/json'})
        self.assertEqual(response.status_code, 400)


