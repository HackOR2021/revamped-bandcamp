from flask import Blueprint, render_template

views = Blueprint('views', __name__)

@views.route('/')
def home():
    return render_template("index.html")

@views.route('/artist-home')
def artist_home():
    return render_template("artist_home.html")