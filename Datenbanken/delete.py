from pymongo import MongoClient
from pprint import pprint

DB_URL = 'mongodb+srv://cluster0.spdqnnv.mongodb.net/'
DB_USER = 'Nachhilfe'
DB_PASSWORT = '12345Abcd'

client = MongoClient(DB_URL, username = DB_USER
                     , password = 
                     DB_PASSWORT)

db = client.cima
col = db.aflam

# res = col.find({'titel' : 'Psycho'}, projection = {'_id' : 0})
# for film in res:
#     pprint(film)
# col.delete_one({'titel': 'Psycho', 'jahr' : 1998})

# col.delete_many({'imdb': {'$lt' : 7.5}})

# res = col.find({'imdb': {'$lt' : 7.5}})
# for film in res:
#     pprint(film)

# col.delete_many({})
print(col.estimated_document_count())



# explizit durch angabe von Hostname oder IP und Port: 
# client = pymongo.MongoClient('imm-vm-sote', 27017)