import os
import json
import pymongo
from pymongo import MongoClient
from bitwise.data.mail.parse import EmailParser
from models import DOCUMENT_MODEL, ATTEMPT_MODEL

DATABASE = 'bitwise'
COLLECTION = 'problems'
AUTH_JSON = 'mongoauth.json'

class DatabaseClient():

    def __init__(self):
        if not os.path.exists(AUTH_JSON):
            raise Exception('Authorization JSON not found. Check files.')
        self.connection = self.connect_to_db()

    def connect_to_db(self):
        file = open(AUTH_JSON)
        info = json.load(file)
        access_key = list(info.keys())[0]
        cluster = MongoClient(access_key)
        db = cluster[DATABASE]
        collection = db[COLLECTION]
        return collection

    def create(self, 
               source="",
               difficulty="",
               company="",
               answer_format="",
               topic="",
               score=0,
               number=0,
               ):
        new_entry = DOCUMENT_MODEL
        params = [source, difficulty, company, answer_format, topic, score, number]
        for param in params:
            key = str(param)
            new_entry[key] = param
        self.collection.insert_one(new_entry)
               
    def update(self,
               )

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
