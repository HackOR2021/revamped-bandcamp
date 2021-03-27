from flask import Flask
from flask_pymongo import PyMongo

from website.database import mongo


import os


def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'fdjkhngkjefj dk'

    app.config['MONGO_URI'] = "mongodb+srv://HackOR_2021_user:cmh2LPJzNgOYKX8y@hackor2021cluster.d6r9o.mongodb.net/myFirstDatabase?retryWrites=true&w=majority"
    app.config['MONGO_DBNAME'] = os.environ.get('minerva',app.name)

    mongo = PyMongo()

    mongo.init_app(app)
    
    from .views import views

    app.register_blueprint(views, url_prefix='/')

    return app