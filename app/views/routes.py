from flask                          import Flask, jsonify, request
from app.models                     import DataRequest, DBManipulation, KeyMissingError, ValueTypeError, InvalidKeysError

def init_app(app: Flask):


    @app.get('/posts')

    def read_posts():
  
        all_posts = DBManipulation.get_all_posts()

        json_return = all_posts or {'message': 'there is no any post'}

        return jsonify(json_return), 200



    @app.get('/posts/<int:id>')

    def get_especific_post_by_id(id: int) -> list:

        especific_post = DBManipulation.get_post_by_id(id)

        if not especific_post:

            return {'message': 'This id does not exist'}, 404

        return jsonify(especific_post), 200



    @app.post('/posts')

    def create_post():

        try: 

            treated_data = DataRequest.verify_json_request(**request.json)

            data_obj = DataRequest(**treated_data)

            inserted_data = DBManipulation.save(data_obj.__dict__)

            return inserted_data, 201
        
        except KeyMissingError as error:

            return error.__dict__, 400

        except ValueTypeError as error:

            return error.__dict__, 400



    @app.delete('/posts/<int:id>')

    def delete_post_by_id(id: int) -> list:

        deleted_post = DBManipulation.delete_a_post(id) 

        if not deleted_post:

            return {'message': 'this id does not exist'}, 404

        return jsonify(deleted_post), 200 




    @app.patch('/posts/<int:id>')

    def patch_post(id: int):

        try:

            updated_post = DBManipulation.update_a_post(data_to_update=request.json, id=id)

            if not updated_post:

                return {'message': 'this id does not exist'}, 404

            return jsonify(updated_post), 201

        except InvalidKeysError as error:

            return error.__dict__, 400

        except ValueTypeError as error:

            return error.__dict__, 400
