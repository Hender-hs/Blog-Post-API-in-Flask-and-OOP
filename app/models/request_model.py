from app                            import db
from app.models.exceptions_errors   import KeyMissingError, ValueTypeError, InvalidKeysError
from datetime                       import datetime

class DataRequest :


    def __init__(self, title: str, author: str, tags: str, content: str) -> None:

        self.title = title
        self.author = author
        self.tags = tags
        self.content = content
        self.created_at = str(datetime.now())



    @staticmethod

    def verifying_request_keys(request_keys: dict) -> None:

        missed_keys = []

        correct_keys = {'title', 'author', 'tags', 'content'}

        for key in correct_keys:

            if not key in request_keys:

                missed_keys.append(key)

        if missed_keys:

            raise KeyMissingError(missed_keys)



    @staticmethod

    def verifying_values_type(dict_request: dict) -> None:

        wrong_types = []

        for key, value in dict_request.items():

            if type(value) != str:

                wrong_types.append(key)

        if wrong_types:

            raise ValueTypeError(wrong_types)    



    @classmethod

    def verify_json_request(cls, **kwargs) -> dict:

        cls.verifying_request_keys(kwargs)

        cls.verifying_values_type(kwargs)

        data =  {'title': kwargs['title'], 'author': kwargs['author'], 'tags': kwargs['tags'], 'content': kwargs['content']}

        return data


    
    @staticmethod

    def patch_verify_keys(keys: set) -> None:

        allowed_keys = {'title', 'author', 'tags', 'content'}

        wrong_keys = keys.difference(allowed_keys) 

        if wrong_keys:

            raise InvalidKeysError(wrong_keys)
