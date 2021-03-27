from pymongo import MongoClient



def connect_minerva_db():
    """
    Create a connection to the live mongoDB server, select the minerva database and return it so we can query
    """
    client = MongoClient("mongodb+srv://HackOR_2021_user:cmh2LPJzNgOYKX8y@hackor2021cluster.d6r9o.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
    return client.minerva


def get_artists():
    """
    Returns all artists on the minerva DB
    """
    # Connect to database
    db = connect_minerva_db()

    # return all the artists as a list
    artists = list(db.artists.find())
    return artists

def get_ten_artists():
    """
    Returns ten artists from the minerva DB
    """
    # Connect to database
    db = connect_minerva_db()

    # return all the artists as a list
    ten_artists = list(db.artists.find().limit(10))
    return ten_artists

def get_tracks():
    """
    Returns all tracks on the minerva DB
    """

    # connect to the database
    db = connect_minerva_db()

    # return all the tracks as a list
    tracks = list(db.tracks.find())
    return tracks

def get_ten_tracks():
    """
    Returns all tracks on the minerva DB
    """

    # connect to the database
    db = connect_minerva_db()

    # return all the tracks as a list
    ten_tracks = list(db.tracks.find().limit(10))
    return ten_tracks

def get_tracks_of_artist(artist_id):
    """
    Returns all tracks on the minerva DB that are associated with the provided artist id
    """

    # connect to the database
    db = connect_minerva_db()

    # return all the tracks as a list
    artist_tracks = list(db.tracks.find( { _id: artist_id } ))
    return artist_tracks


def get_fans():
    """
    Returns all fans on the minerva DB
    """

    # connect to the database
    db = connect_minerva_db()

    # return all the fans as a list
    fans = list(db.fans.find())
    return fans


def get_albums():
    """
    Returns all albums on the minerva DB
    """

    # connect to the database
    db = connect_minerva_db()

    # return all the albums as a list
    albums = list(db.albums.find())
    return albums


def get_shows():
    """
    Returns all shows on the minerva DB
    """

    # connect to the database
    db = connect_minerva_db()

    # return all the shows as a list
    shows = list(db.shows.find())
    return shows


def get_ten_shows():
    """
    Returns all shows on the minerva DB
    """

    # connect to the database
    db = connect_minerva_db()

    # return all the shows as a list
    ten_shows = list(db.shows.find().limit(10))
    return ten_shows

def add_track(track_artist, track_name, track_description, track_genre, 
    track_audio, track_artwork, track_pricing, track_date, track_credits, is_public):
    """
    Provided track details, add a new track to Minerva
    """

    # connect to the database
    db = connect_minerva_db()   

    # package up the track details
    new_track = {
            "track_artist": track_artist,
            "track_name": track_name,
            "track_description": track_description,
            "track_genre": track_genre,
            "track_audio": track_audio,
            "track_artwork": track_artwork,
            "track_pricing": track_pricing,
            "track_date": track_date,
            "track_credits": track_credits,
            "is_public": is_public
        }

    # add the track to the database
    track_id = db.tracks.insert_one(new_track)

    # return the track id of the newly added track
    return track_id
    
def add_album():
    # Adds an album to the database
    pass

def add_fan(fan_username, fan_password, fan_first_name, fan_last_name):
    # Adds a fan to the database
    db = connect_minerva_db()
    new_fan = {"fan_username": fan_username,
     "fan_password": fan_password,
     "fan_first_name": fan_first_name,
     "fan_last_name": fan_last_name
     }

    return db.fans.insert_one(new_fan)

def add_show(show_date, show_time, show_name, show_artist, show_description, show_link):
    # Adds a show to the database
    db = connect_minerva_db()
    new_show = {"show_date": show_date, 
    "show_time": show_time, 
    "show_name": show_name, 
    "show_artist": show_artist, 
    "show_description": show_description, 
    "show_link": show_link
    }

    return db.shows.insert_one(new_show)

def add_artist(first_name, last_name, email, website, city, state, profile_image):
    # Adds an artist to the database
    db = connect_minerva_db()
    new_artist = {
        "first_name": first_name,
        "last_name": last_name,
        "email": email,
        "website": website,
        "city": city,
        "state": state,
        "profile_image": profile_image
   }
    return db.tracks.insert_one(new_artist)



