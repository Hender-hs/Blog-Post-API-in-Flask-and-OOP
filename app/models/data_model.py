from app                            import db
from app.models.exceptions_errors   import PropMissingError, ValueTypeError, InvalidProps
from datetime                       import datetime

class DataRequest :


    def __init__(self, title: str, author: str, tags: str, content: str) -> None:

        self.title = title
        self.author = author
        self.tags = tags
        self.content = content
        self.created_at = str(datetime.now())


    
    @staticmethod

    def get_all_posts() -> list:

        all_posts = db.posts.find()

        return list(all_posts)



    @staticmethod

    def get_post_by_id(id: int) -> dict:

        especific_post = db.posts.find_one({'_id': id})

        return especific_post



    @staticmethod

    def verifying_request_keys(request_keys: dict) -> None:

        missed_keys = []

        correct_keys = {'title', 'author', 'tags', 'content'}

        for key in correct_keys:

            if not key in request_keys:

                missed_keys.append(key)

        if missed_keys:

            raise PropMissingError(missed_keys)



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


    
    def get_new_id(self) -> int:

        all_posts_list = self.get_all_posts()

        if not all_posts_list:

            new_id = 1

            return new_id

        all_posts_list = list(all_posts_list)

        last_id = all_posts_list[-1].get('_id')

        new_id = last_id + 1

        return new_id


    
    def save(self) -> dict:

        target_new_id = self.get_new_id() 

        data_to_save = {**self.__dict__, '_id': target_new_id}

        db.posts.insert_one(data_to_save)

        return data_to_save

        

    @staticmethod

    def delete_a_post(id: int) -> dict:

        deleted_post = db.posts.find_one_and_delete({'_id': id})

        return deleted_post


    
    @staticmethod

    def patch_verify_keys(keys: set) -> None:

        allowed_keys = {'title', 'author', 'tags', 'content'}

        wrong_keys = keys.difference(allowed_keys) 

        if wrong_keys:

            raise InvalidProps(wrong_keys)



    @classmethod

    def update_a_post(cls, data_to_update: dict, id: int) -> dict:

        post_to_filter = {'_id': id}

        cls.patch_verify_keys(set(data_to_update.keys()))

        cls.verifying_values_type(data_to_update)

        data_to_update = {**data_to_update, 'updated_at': str(datetime.now())}

        db.posts.update_one(post_to_filter, {'$set': data_to_update})

        updated_data = db.posts.find_one(post_to_filter)

        return updated_data

