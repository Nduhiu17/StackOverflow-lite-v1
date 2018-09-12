import json
from datetime import datetime


def register_user(self):
    #register user
    return self.client.post(
        'auth/register',
        data=json.dumps(dict(
            username='username254',
            email='username254@gmail.com',
            password='password'
        )),
        content_type='application/json'
        )

def login_user(self):
    #loginthe registered user
    return self.client.post(
        'auth/login',
        data=json.dumps(dict(
            username='username254',
            password='password'
        )),
        content_type='application/json'
    )

def post_quiz(self):
    #loginthe registered user
    response = login_user(self)
    result = json.loads(response.data)
    self.assertIn("access_token", result)
    new_question = {'title': 'error sit voluptatem accusantium doloremque laudantium',
                    'body': 'error sit voluptatem accusantium doloremque laudantiumerror sit volupta', 'user_id': 1}
    response = self.client.post('api/v1/questions', data=json.dumps(new_question),
                            headers={'Authorization': f'Bearer {result["access_token"]}',
                                     'Content-Type': 'application' '/json'})
    return response
    # return self.client.post(
    #     'api/v1/questions',
    #     data=json.dumps(dict(
    #         title='titletitletitletitletitletitletitletitletitletitletitletitletitletitletitletitletitletitle',
    #         body='bodybodybodybodybodybodybodybodybodybodybodybodybodybodybodybodybodybodybodybodybodybodybodybodybodybody',
    #         user_id=1,
    #         # date_created=str(datetime.now()),
    #         # date_modified=str(datetime.now())
    #
    #     )),
    #     content_type='application/json'
    # )

