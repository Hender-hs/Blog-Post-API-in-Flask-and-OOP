from app.models.request_model       import DataRequest
from app                            import db
from datetime                       import datetime

class DBManipulation : 

    
    def get_all_posts() -> list:

        all_posts = db.posts.find()

        return list(all_posts)

    

    def get_post_by_id(id: int) -> dict:

        especific_post = db.posts.find_one({'_id': id})

        return especific_post



    @classmethod

    def get_new_id(cls) -> int:

        all_posts_list = cls.get_all_posts()

        if not all_posts_list:

            new_id = 1

            return new_id

        all_posts_list = list(all_posts_list)

        last_id = all_posts_list[-1].get('_id')

        new_id = last_id + 1

        return new_id



    @classmethod
    
    def save(cls, kwargs) -> dict:

        target_new_id = cls.get_new_id() 

        data_to_save = {**kwargs, '_id': target_new_id}

        db.posts.insert_one(data_to_save)

        return data_to_save



    def delete_a_post(id: int) -> dict:

        deleted_post = db.posts.find_one_and_delete({'_id': id})

        return deleted_post



    def update_a_post(data_to_update: dict, id: int) -> dict:

        post_to_filter = {'_id': id}

        DataRequest.patch_verify_keys(set(data_to_update.keys()))

        DataRequest.verifying_values_type(data_to_update)

        data_to_update = {**data_to_update, 'updated_at': str(datetime.now())}

        db.posts.update_one(post_to_filter, {'$set': data_to_update})

        updated_data = db.posts.find_one(post_to_filter)

        return updated_data