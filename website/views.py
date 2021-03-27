from flask import Blueprint, render_template


from pymongo import ReturnDocument, MongoClient

from website import mongo


def get_artists():
    client = MongoClient("mongodb+srv://HackOR_2021_user:cmh2LPJzNgOYKX8y@hackor2021cluster.d6r9o.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
    db = client.minerva
    artists = list(db.artists.find())
    return artists

views = Blueprint('views', __name__)

@views.route('/')
def home():
    db_artists = get_artists()
    print(db_artists[0]['first_name'])
    return render_template("index.html", artists = db_artists)

@views.route('/artist-home')
def artist_home():
    return render_template("artist_home.html")

@views.route('/add-tracks')
def add_tracks():
    return render_template("new_track.html")

@views.route('/edit-tracks')
def edit_tracks():
    return render_template("edit_track.html")