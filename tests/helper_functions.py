import json


def register_user(self):
    # register user
    return self.client.post(
        'api/v1/auth/signup',
        data=json.dumps(dict(
            username='username254',
            email='username254@gmail.com',
            password='password'
        )),
        content_type='application/json'
    )


def login_user(self):
    # loginthe registered user
    return self.client.post(
        'api/v1/auth/login',
        data=json.dumps(dict(
            username='username254',
            password='password'
        )),
        content_type='application/json'
    )


def post_quiz(self):
    # loginthe registered user
    response = login_user(self)
    result = json.loads(response.data)
    self.assertIn("access_token", result)
    new_question = {'title': 'error sit voluptatem accusantium doloremque laudantium',
                    'body': 'error sit voluptatem accusantium doloremque laudantiumerror sit volupta', 'user_id': 1}
    response = self.client.post('api/v1/questions', data=json.dumps(new_question),
                                headers={'Authorization': f'Bearer {result["access_token"]}',
                                         'Content-Type': 'application' '/json'})
    return response


def post_answer(self):
    # login the registered user
    response = login_user(self)
    result = json.loads(response.data)
    self.assertIn("access_token", result)
    new_answer = {'body': 'error sit voluptatem accusantium doloremque laudantiumerror sit volupta'}
    response = self.client.post('/api/v1/questions/2/anwsers', data=json.dumps(new_answer),
                                headers={'Authorization': f'Bearer {result["access_token"]}',
                                         'Content-Type': 'application' '/json'})
    return response
