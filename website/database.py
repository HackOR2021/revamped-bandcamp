# # import the general python mongodb driver
# import pymongo

# import the specific module to handshake flask with mongoDB
from flask_pymongo import PyMongo


# # link to mongodb server
# mongo_uri = "mongodb+srv://HackOR_2021_user:cmh2LPJzNgOYKX8y@hackor2021cluster.d6r9o.mongodb.net/myFirstDatabase?retryWrites=true&w=majority"

mongo = PyMongo

# , render_template, request, redirect, url_for


# from flask import Blueprint, render_template



# # import os to manage the file connections
# import os
# import json
# import datetime


# # import the general python mongodb driver
# import pymongo

# # import the specific module to handshake flask with mongoDB
# from flask_pymongo import PyMongo

# from bson import ObjectId

# views = Blueprint('views', __name__)



# # Connects to fl
# class JSONEncoder(json.JSONEncoder):
#     ''' extend json-encoder class'''

#     def default(self, o):
#         if isinstance(o, ObjectId):
#             return str(o)
#             if isinstance(o, datetime.datetime):
#                 return str(o)
#                 return json.JSONEncoder.default(self, o)


# # general function to redirect back to home page
# def redurect_url():
#     return request.args.get('next') or request.referrer or url_for('index')


# def update_db():
#     """
#     Updates the mongoDB instance so we always have the freshest of data
#     """
    
#     # Grab all the data from all the collections
#     artists_new = artists.find()
#     fans_new = fans.find()
#     tracks_new = tracks.find()
#     shows_new = shows.find()
#     albums_new = albums.find()

#     # then, return the new data to the webpage and reload that page
#     return render_template('index.html', artists=artists_new, fans=fans_new, tracks=tracks_new, shows=shows_new, albums=albums_new)

# from flask import Flask, render_template, request, redirect, url_for




# def create_app():
#     app = Flask(__name__)
#     app.config['SECRET_KEY'] = 'fdjkhngkjefj dk'

#     # Configure the connection to the database
#     client = pymongo.MongoClient("mongodb+srv://HackOR_2021_user:cmh2LPJzNgOYKX8y@hackor2021cluster.d6r9o.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
    
#     # isolate the desired database from MongoDb
#     db = client.minerva

#     # isolate each of the collections used by the database
#     artists=db.artists
#     fans=db.fans
#     tracks=db.tracks
#     shows=db.shows
#     albums=db.albums


#     from .views import views

#     app.register_blueprint(views, url_prefix='/')

#     return app

# @views.route('/')
# def home():
#     return render_template("index.html")

# @views.route('/artist-home')
# def artist_home():
#     return render_template("artist_home.html")

# @views.route('/add-tracks')
# def add_tracks():
#     return render_template("new_track.html")

# @views.route('/edit-tracks')
# def edit_tracks():
#     return render_template("edit_track.html")


#     # Configure the connection to the database
#     client = pymongo.MongoClient("mongodb+srv://HackOR_2021_user:cmh2LPJzNgOYKX8y@hackor2021cluster.d6r9o.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
    
#     # isolate the desired database from MongoDb
#     db = client.minerva

#     # isolate each of the collections used by the database
#     artists=db.artists
#     fans=db.fans
#     tracks=db.tracks
#     shows=db.shows
#     albums=db.albums

#     # Add a general rule that forces the page to update and reload the connection to MongoDB when we return to the home page
#     app.add_rule("/", "update", update_db)


# # import os to manage the file connections
# import os
# import json
# import datetime


# # import the general python mongodb driver
# import pymongo

# # import the specific module to handshake flask with mongoDB
# from flask_pymongo import PyMongo

# from bson import ObjectId

# # Connects to fl
# class JSONEncoder(json.JSONEncoder):
#     ''' extend json-encoder class'''

#     def default(self, o):
#         if isinstance(o, ObjectId):
#             return str(o)
#             if isinstance(o, datetime.datetime):
#                 return str(o)
#                 return json.JSONEncoder.default(self, o)


# # general function to redirect back to home page
# def redurect_url():
#     return request.args.get('next') or request.referrer or url_for('index')


# def update_db():
#     """
#     Updates the mongoDB instance so we always have the freshest of data
#     """
    
#     # Grab all the data from all the collections
#     artists_new = artists.find()
#     fans_new = fans.find()
#     tracks_new = tracks.find()
#     shows_new = shows.find()
#     albums_new = albums.find()

#     # then, return the new data to the webpage and reload that page
#     return render_template('index.html', artists=artists_new, fans=fans_new, tracks=tracks_new, shows=shows_new, albums=albums_new)

