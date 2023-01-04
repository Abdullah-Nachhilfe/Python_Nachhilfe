import requests as rq
import json
from pprint import pprint
from datetime import datetime

def get_geo_coordinates(city_name):
    URL = 'https://nominatim.openstreetmap.org/search.php?city=%s&format=json' % city_name
    response = rq.get(URL)
    if response.status_code == 200:
        inhalt_roh = response.content.decode()
        inhalt = json.loads(inhalt_roh)
    stadt = inhalt[0]
    koordinaten = {'lat':stadt['lat'], 'lon' : stadt['lon']}
    return koordinaten

def get_weather_data(city_name):
    koordinaten = get_geo_coordinates(city_name)
    lat = koordinaten['lat']
    lon = koordinaten['lon']
    URL = 'https://api.open-meteo.com/v1/forecast?latitude=%s&longitude=%s&hourly=temperature_2m' % (lat, lon)
    response = rq.get(URL)
    if response.status_code == 200:
        inhalt_roh = response.content.decode()
        inhalt = json.loads(inhalt_roh)
    temp = inhalt['hourly'] # hourly temp
    now = datetime.now().isoformat() # akteulle Zeit in iso8061 Format
    for time in temp['time']:
        if time[:13] == now[:13]:
            index = temp['time'].index(time)
            C = temp['temperature_2m']
            aktuelle_temp = C[index]
            return {'aktuelle Stunde' : now, 'Temperatur in °C' : aktuelle_temp}
    


print(get_weather_data('Ulm'))


