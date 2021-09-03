from flask      import Flask
from pymongo    import MongoClient


client = MongoClient('mongodb://localhost:27017/')

db = client['kenzie']


def create_app():

    app = Flask(__name__)


    from app.views.routes import init_app

    init_app(app) 


    return app
