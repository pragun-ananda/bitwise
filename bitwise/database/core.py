import os
import json
from typing import Any
import pymongo
from pymongo import MongoClient
from bitwise.data.mail.parse import EmailParser
from models import DOCUMENT_MODEL, ATTEMPT_MODEL

# Redefine constants to match your database and authorization criteria
DATABASE_NAME = 'bitwise'
COLLECTION_NAME = 'problems'
AUTH_JSON_NAME = 'mongoauth.json'

class DatabaseClient():

    def __init__(self):
        if not os.path.exists(AUTH_JSON_NAME):
            raise Exception('Authorization JSON not found. Check files.')
        self.connection = self.connect_to_db()

    def connect_to_db(self):
        file = open(AUTH_JSON_NAME)
        info = json.load(file)
        access_key = list(info.keys())[0]
        cluster = MongoClient(access_key)
        db = cluster[DATABASE_NAME]
        collection = db[COLLECTION_NAME]
        return collection

    def create(self, 
               source="",
               difficulty="",
               company="",
               answer_format="",
               topic="",
               score=0,
               number=0,
               ) -> Any:
        post = DOCUMENT_MODEL
        params = [source, difficulty, company, answer_format, topic, score, number]
        for param in params:
            key = str(param)
            post[key] = param
        post_id = self.collection.insert_one(post).inserted_id
        return post_id

    def read(self):
        '''TODO'''
        return None

    def update(self):
        '''TODO'''
        return None

    def delete(self):
        '''TODO'''
        return None

'''
API methods:

- insert_one({})
- insert_many([{}, {}, ...])
- find({}) -> returns iterable object
- find_one({}) -> returns dictionary
- delete_one({})
- delete_many({})
- update_one({}, {})    * param2 are update operators *
- count_documents({})
'''

'''
TODO:
    - Create an API to handle all CRUD operations
    - Consider saving sensitive info somewhere (authenticate.json)

'''

test_model = DOCUMENT_MODEL
collection.insert_one(test_model)
