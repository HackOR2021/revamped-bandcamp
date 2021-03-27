from flask import Flask, render_template, request, redirect, url_for

# import os to manage the file connections
import os
import json
import datetime


# import the general python mongodb driver
import pymongo

# import the specific module to handshake flask with mongoDB
from flask_pymongo import PyMongo

from bson import ObjectId

# Connects to fl
class JSONEncoder(json.JSONEncoder):
    ''' extend json-encoder class'''

    def default(self, o):
        if isinstance(o, ObjectId):
            return str(o)
            if isinstance(o, datetime.datetime):
                return str(o)
                return json.JSONEncoder.default(self, o)


# 


def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'fdjkhngkjefj dk'

    # Configure the connection to the database
    client = pymongo.MongoClient("mongodb+srv://HackOR_2021_user:cmh2LPJzNgOYKX8y@hackor2021cluster.d6r9o.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
    
    # isolate the desired database from MongoDb
    db = client.minerva

    # isolate each of the collections used by the database
    artists=db.artists
    fans=db.fans
    tracks=db.tracks
    shows=db.shows
    albums=db.albums

    # Creates a wrapper around the app instance that is tied to the database

    from .views import views

    app.register_blueprint(views, url_prefix='/')

    return app