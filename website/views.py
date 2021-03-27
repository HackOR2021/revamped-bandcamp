from flask import Blueprint, render_template

# import mongo
from website import mongo


# import the database queries
import website.queries as dbq


views = Blueprint('views', __name__)

@views.route('/')
def home():

    # load ten artists from database
    db_artists = dbq.get_ten_artists()
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


@views.route('/view-tracks')
def view_tracks():
    return render_template("view_tracks.html")