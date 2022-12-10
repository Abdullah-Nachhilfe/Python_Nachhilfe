import requests as rq
import json # für Umgang und Umwandelung von JSON Dateien in Py
# response = rq.get('https://gtfs.swu.de/daten/routes.txt')

# print(response.status_code)
# # Status code: 
# # 200       anfrage ist erfolgreich
# # 401       Sie müssen sich einloggen
# # 403       Sie haben kein Recht auf die Resource zuzugreifen
# # 404       Die gesuchte Resource existiert nicht

# if response.status_code == 200:
#     #inhalt_roh = response.content # Inhalt als Maschinen lesbarer Code
#     inhalt = response.content.decode() # Inhalt als String. Voraussetzung, es handelt sich uum einen String
#     zeilen = inhalt.splitlines() # String zeilenweise splitten
#     for zeile in zeilen[:5]:
#         print(zeile)




URL = 'https://api.coinbase.com/v2/exchange-rates?currency=EUR'
re = rq.get(URL)
def ermittle_kurs_usd():
    if re.status_code == 200:
        inhalt_json = re.content.decode() # Hier: Inhalt ist JSON  
        inhalt = json.loads(inhalt_json) # Umwandelung von JSON in Python Datenstruktur
        data = inhalt['data']
        rates = data['rates']
        rate_usd = rates['USD']
        return float(rate_usd)

def umrechnen_euro_in_usd(betrag):
    kurs = ermittle_kurs_usd()
    return kurs * betrag

print('$%.2f'% umrechnen_euro_in_usd(7.50))
    
# EURO in andere Währung, z.B. $