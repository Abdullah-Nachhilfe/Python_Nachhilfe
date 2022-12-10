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

# Update: Setzte imdb Wertung
# # col.update_one({'titel' : 'Brazil', 'jahr' : 1985}, {'$set' : {'imdb' : 8.0}})

# Setzte Geb.Datum für 'Jordan Peele'
# # col.update_many({'regie.name' : 'Jordan Peele' }, {'$set' : {'regie.geb' : 1979} })

# res = col.find({'regie.name' : 'Jordan Peele'}, projection = {'_id' : 0})
# for film in res:
#     pprint(film)

# Füge Genre Western zu Desperado

# # col.update_many({'titel' : 'Desperado'} , { '$push' : {'genres' : 'Western'} })


# res = col.find({'titel' : 'Desperado'}, projection = {'_id' : 0})
# for film in res:
#     pprint(film)

# col.update_many({'titel' : 'Brazil', 'jahr' : 1985}, { '$inc': {'imdb' : 0.5} })

# res = col.find({'titel' : 'Brazil', 'jahr' : 1985}, projection = {'_id' : 0})
# for film in res:
#     pprint(film)


# col.update_many({'regie.name' : 'Jordan Peele'}, { '$inc' : {'imdb' : 1.0} })
res = col.find({'regie.name' : 'Jordan Peele'}, projection = {'_id' : 0})
for film in res:
    pprint(film)
