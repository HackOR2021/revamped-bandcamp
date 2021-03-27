from flask import Flask
from flask_pymongo import PyMongo

from website.database import mongo

from .views import views

import os


def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'fdjkhngkjefj dk'

    # add connection to mongodb server
    app.config['MONGO_URI'] = "mongodb+srv://HackOR_2021_user:cmh2LPJzNgOYKX8y@hackor2021cluster.d6r9o.mongodb.net/myFirstDatabase?retryWrites=true&w=majority"
    
    # connect to the specific minerva server
    app.config['MONGO_DBNAME'] = os.environ.get('minerva',app.name)

    # start up mongodb
    mongo = PyMongo()

    # connect mongodb to our local app
    mongo.init_app(app)

    # load views as blueprint on the database-registered app
    app.register_blueprint(views, url_prefix='/')

    return app