import os
import json
from typing import Any
import pymongo
from pymongo import MongoClient
from bitwise.data.mail.parse import EmailParser
from models import DOCUMENT_MODEL, ATTEMPT_MODEL


''' Define constants below to match your database and authorization information '''
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

    def build_doc_request(self, params):
        request = DOCUMENT_MODEL
        for param in params:
            if len(param) == 0 or param == 0:
                continue
            key = str(param)
            request[key] = param
        return request

    def create(self, 
               source="",
               difficulty="",
               company="",
               answer_format="",
               topic="",
               score=0,
               number=0,
               ) -> Any:
               
        params = [source, difficulty, company, 
                  answer_format, topic, score, number]
        request = self.build_doc_request(params)
        post_id = self.collection.insert_one(request).inserted_id
        return post_id

    def read(self,
             id=0,
             source="",
             difficulty="",
             company="",
             answer_format="",
             topic="",
             score=0,
             number=0
             ) -> Any:

        params = [source, id, difficulty, company, 
                  answer_format, topic, score, number]
        request = self.build_doc_request(params)
        response = self.collection.find_one(request)
        return response

    def update(self,
               id=0,
               source="",
               difficulty="",
               company="",
               answer_format="",
               topic="",
               score=0,
               number=0
               ) -> None:

        document = self.read(id=id)
        params = [source, id, difficulty, company, 
                  answer_format, topic, score, number]
        request = self.build_doc_request(params)
        result = self.collection.update_one(document, request)
        return result

    def delete(self,
               id=0,
               source="",
               difficulty="",
               company="",
               answer_format="",
               topic="",
               score=0,
               number=0
               ) -> None:
        
        params = [source, id, difficulty, company, 
                  answer_format, topic, score, number]
        request = self.build_doc_request(params)
        result =  self.collection.delete_one(request)
        return result


# test_model = DOCUMENT_MODEL
# collection.insert_one(test_model)
