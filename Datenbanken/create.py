# Was ist ein Dokument? ==> JSON-Objekt

from pymongo import MongoClient
from pprint import pprint
DB_URL = 'mongodb+srv://cluster0.g42vq.mongodb.net/'
DB_USER = 'labor_user'
DB_PASSWORD = 'RFzhGrCZVMOOWlTN'

# Client Erstellung (Verbindung zum Server)
client = MongoClient(DB_URL,
                     username = DB_USER,
                     password = DB_PASSWORD)

# Neuer Datenbank
db_cinema = client['cinema']
# Neue Collection im Datenbank
col_films = db_cinema['films']
col_films.drop() # NUR FÜR DIESE ÜBUNG!! SOLLTE NICHT VERWENDET WERDEN!



film_nightmare = {'titel' : 'The Nightmare Before Christmas', 
             'jahr' : 1993, 
             'regie' : { 
                 'name': 'Henry Selick', 
                 'geb': 1952 
             }, 
             'dauer': 76,
             'imdb' : 8.0, 
             'genres':['Animation', 'Family', 'Fantasy']
}
print(col_films.estimated_document_count())

# Einfügen eines einzelnen Dokument:
col_films.insert_one(film_nightmare)
print(col_films.estimated_document_count())

filme = [
         {'titel' : 'Being John Malkovich', 'jahr' : 1999, 'dauer': 113, 'imdb' : 7.7, 
          'regie' : { 'name': 'Spike Jonze', 'geb': 1969 }, 
          'genres': ['Comedy', 'Drama', 'Fantasy'] },
         {'titel' : 'The Sixth Sense', 'jahr' : 1999, 'dauer': 107, 'imdb' : 8.1, 
          'regie' : { 'name': 'M. Night Shyamalan', 'geb': 1970 }, 
          'genres': ['Drama', 'Mystery', 'Thriller'] }, 
         {'titel': 'Fight Club', 'jahr': 1999,  'dauer': 161, 'imdb': 8.8,
          'regie': {'name': 'David Fincher', 'geb': 1962}, 
          'genres': ['Drama']}
]
# Einfügen mehrere Filme (Dokumente)
# for film in filme:
#     col_films.insert_one(film)
col_films.insert_many(filme)

print(col_films.estimated_document_count())
