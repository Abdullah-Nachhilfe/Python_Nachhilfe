from pymongo import MongoClient
from pprint import pprint

DB_URL = 'mongodb+srv://cluster0.g42vq.mongodb.net/'
DB_USER = 'labor_user'
DB_PASSWORD = 'RFzhGrCZVMOOWlTN'

client = MongoClient(DB_URL,
    username=DB_USER,
    password=DB_PASSWORD)

db = client['cinema']
col = db['films']
# Meinstens speichern wir die Datenbankabfrage in einer Variable namens res
print(client.list_database_names())
# Beliebiges Dokument / Film
# res = col.find_one()
# print(res)

# Beliebiges Dokument / Film
# res = col.find_one(projection = {'_id' : 0})
# print(res)


# Alle Dokumente/Film in einer Collection:
# 
res = col.find(projection = {'_id' : 0}) # Interable
liste = list(res)
#pprint(liste)
# for film in res:
#     pprint(film)

# Ausgabe begrenzen
# res = col.find(projection = {'_id' : 0}).limit(2)

# for film in res:
#     pprint(film)

# Filme aus dem Jahr 1999

# res = col.find({'jahr' : 1999}, projection = {'_id' : 0})
# for film in res:
#     pprint(film)
# print(col.count_documents({'jahr' : 1999}))

# Find the Film Fight Club
# res = col.find_one({'titel': 'Fight Club'})
# pprint(res)