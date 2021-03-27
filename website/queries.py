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



def get_tracks():
    """
    Returns all tracks on the minerva DB
    """

    # connect to the database
    db = connect_minerva_db()

    # return all the tracks as a list
    tracks = list(db.tracks.find())
    return tracks


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


def add_track()

    track_name
    track_description
    track_genre
    audio
    artwork
    pricing
    track_date
    track_price
    track_credits
    is_public