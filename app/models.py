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

    def json_dumps(self):
            #method to return a json object from the question details
        obj = {
            "id": str(self.id),
            "title": self.title,
            "body": self.body,
            "date_created": str(self.date_created),
            "date_modified": str(self.date_modified)
        }
        return obj

    def save(self):
        #method to save a question
        MOCK_DATABASE[ "questions" ].append(self)
        return self.json_dumps()

