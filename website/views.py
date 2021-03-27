from flask import Blueprint, render_template

views = Blueprint('views', __name__)

@views.route('/')
def home():
    return render_template("index.html")

@views.route('/artist-home')
def artist_home():
    return render_template("artist_home.html")

@views.route('/add-tracks')
def add_tracks():
    return render_template("new_track.html")

@views.route('/edit-tracks')
def edit_tracks():
    return render_template("edit_track.html")