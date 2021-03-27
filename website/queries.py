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