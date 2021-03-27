from pymongo import MongoClient

def get_artists():
    client = MongoClient("mongodb+srv://HackOR_2021_user:cmh2LPJzNgOYKX8y@hackor2021cluster.d6r9o.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
    db = client.minerva
    artists = list(db.artists.find())
    return artists