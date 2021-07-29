import pymongo
from pymongo import MongoClient
from bitwise.data.mail.parse import EmailParser
from models import DOCUMENT_MODEL, ATTEMPT_MODEL


cluster = MongoClient(# add auth info from json)
db = cluster['bitwise']
collection = db['problems']

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