from pymongo import MongoClient

DB_URL = 'mongodb+srv://cluster0.g42vq.mongodb.net/'
DB_USER = 'labor_user'
DB_PASSWORD = 'RFzhGrCZVMOOWlTN'

# Client Erstellung (Verbindung zum Server)
client = MongoClient(DB_URL,
                     username = DB_USER,
                     password = DB_PASSWORD)

# Client ...:
# 1. das Programm, das ich schreibe
# 2. der PC, den ich nutzte
# 3. die Softwarekomponente, die ich verwende, um auf den Server zugreifen. (Hier: MongoClient)

# print(client)
# print(client.list_database_names())

# Neue Datenbank ablegen:
db_kunden = client['kunden']
# print(db_kunden)

# Neue Collection in einer Datenbank aufmachen:
col_Studenten = db_kunden['Studenten']

print(col_Studenten)
print(col_Studenten.estimated_document_count())