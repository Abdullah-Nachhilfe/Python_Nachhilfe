from pymongo import MongoClient
from pprint import pprint

# local = 'mongodb://localhost:27017/'

cluster = 'mongodb+srv://Nachhilfe:12345Abcd@cluster0.spdqnnv.mongodb.net/?retryWrites=true&w=majority'

client = MongoClient(cluster)

db = client.cima
col = db.aflam

