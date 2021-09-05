from flask                          import Flask, jsonify, request
from app.models.data_model          import DataRequest
from app.models.exceptions_errors   import PropMissingError, ValueTypeError, InvalidProps

def init_app(app: Flask):


    @app.get('/posts')

    def read_posts():
  
        all_posts = DataRequest.get_all_posts()

        json_return = all_posts or {'message': 'there is no any post'}

        return jsonify(json_return), 200



    @app.get('/posts/<int:id>')

    def get_especific_post_by_id(id: int) -> list:

        especific_post = DataRequest.get_post_by_id(id)

        if not especific_post:

            return {'message': 'This id does not exist'}, 404

        return jsonify(especific_post), 200



    @app.post('/posts')

    def create_post():

        try: 

            treated_data = DataRequest.verify_json_request(**request.json)

            data_obj = DataRequest(**treated_data)

            inserted_data = data_obj.save()

            return inserted_data, 201
        
        except PropMissingError as error:

            return error.__dict__, 400

        except ValueTypeError as error:

            return error.__dict__, 400



    @app.delete('/posts/<int:id>')

    def delete_post_by_id(id: int) -> list:

        deleted_post = DataRequest.delete_a_post(id) 

        if not deleted_post:

            return {'message': 'this id does not exist'}, 404

        return jsonify(deleted_post), 200 




    @app.patch('/posts/<int:id>')

    def patch_post(id: int):

        try:

            updated_post = DataRequest.update_a_post(data_to_update=request.json, id=id)

            if not updated_post:

                return {'message': 'this id does not exist'}, 404

            return jsonify(updated_post), 201

        except InvalidProps as error:

            return error.__dict__, 400

        except ValueTypeError as error:

            return error.__dict__, 400



