from flask import Blueprint, render_template

# import mongo
from website import mongo


# import the database queries
import website.queries as dbq


views = Blueprint('views', __name__)

@views.route('/')
def home():

    # load ten artists, ten tracks, and ten shows from the database
    db_artists = dbq.get_ten_artists()
    db_tracks = dbq.get_ten_tracks()
    db_shows = dbq.get_ten_shows()
    return render_template("index.html", artists = db_artists, tracks=db_tracks, shows=db_shows)

@views.route('/artist-home')
def artist_home():
    return render_template("artist_home.html")

@views.route('/add-tracks')
def add_tracks():
    return render_template("new_track.html")

@views.route('/edit-tracks')
def edit_tracks():

    # load some tracks to edit
    tracks_to_edit = dbq.get_ten_tracks()

    return render_template("edit_track.html", tracks=tracks_to_edit)


@views.route('/view-tracks')
def view_tracks():
    return render_template("view_tracks.html")