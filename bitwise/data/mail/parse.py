import base64
from collections import defaultdict
from typing import List, Any
from bitwise.backend.mail.connection import create_service


CLIENT_FILE = 'clientauth.json'
API_NAME = 'gmail'
API_VERSION = 'v1'
SCOPES = ['https://mail.google.com/']
ADDRESS = 'founders@dailycodingproblem.com'
PROBLEM_AMOUNT = 10


class EmailParser():

    def __init__(self, api_instance, userId):
        self._api = api_instance
        self._userId = userId
        self._message_ids = []
        self._encoded_messages = []
        self._decoded_messages = []
        self._problems = []

    def get_message_ids(self) -> List[str]:
        if len(self._message_ids) == 0:
            raise ValueError("Message ID's have not been populated")
        else:
            return self._message_ids

    def get_problems(self) -> List[str]:
        if len(self._problems) == 0:
            raise ValueError("Problems have not been populated")
        else:
            return self._problems

    def get_message_ids_from_address(self) -> None:
        if self._api is None:
            raise Exception('API connection not established') 
        
        message_id_dict = self._api.users().messages().list(
            userId='me', maxResults=PROBLEM_AMOUNT, q='from:' + ADDRESS).execute()

        for message in message_id_dict['messages']:
            self._message_ids.append(message['id'])

    def get_encoded_messages_from_ids(self) -> None:
        if self._api is None:
            raise Exception('API connection not established')

        for id in self._message_ids:
            message = self._api.users().messages().get(userId=self._userId, id=str(id)).execute()
            self._encoded_messages.append(message)

    def decode_messages(self) -> None:
        if len(self._encoded_messages) == 0 or self._encoded_messages is None:
            raise Exception('Missing encoded messages. Check API connection') 

        for message in self._encoded_messages:
            encoded_data = message['payload']['parts'][0]['body']['data']
            decoded_bytes = base64.urlsafe_b64decode(encoded_data)
            decoded_message = str(decoded_bytes, 'utf-8')
            self._decoded_messages.append(decoded_message)

    def separate_coding_problems(self) -> None:
        if len(self._decoded_messages) == 0 or self._decoded_messages is None:
            raise Exception('Missing decoded messages. Check API connection') 

        # Content separator in email format 
        separator = '-' * 60
        
        for message in self._decoded_messages:
            sep_idx = message.find(separator)
            problem = message[:sep_idx].strip()
            self._problems.append(problem)
        
    def extract_problems(self) -> None:
        self.get_message_ids_from_address()
        self.get_encoded_messages_from_ids()
        self.decode_messages()
        self.separate_coding_problems()

'''
TODO:
    - implement a method to parse subject info (problem number, company, difficulty)
    - choose how data will be stored -> what's the best way for MongoDB? 
    - connect to DB and write data to MongoDB 
'''

def main():
    '''
        Connect to API. 
    '''
    api = create_service(CLIENT_FILE, API_NAME, API_VERSION, SCOPES)
    parser = EmailParser(api, userId='me')
    parser.extract_problems()
    problems = parser.get_problems()
    print(problems[0])

if __name__=='__main__':
    main()