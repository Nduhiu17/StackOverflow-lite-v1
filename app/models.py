import uuid

from datetime import datetime

#create a mock database
MOCK_DATABASE = {
    "questions": [ ]

}


class Question:
    '''Class to model a question'''
    def __init__(self, title, body):
        #method to initialize Question class
        self.id = uuid.uuid4()
        self.title = title
        self.body = body
        self.date_created = datetime.now()
        self.date_modified = datetime.now()

