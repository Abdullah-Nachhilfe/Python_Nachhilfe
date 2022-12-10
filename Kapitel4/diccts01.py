# Dictionary => Daten Struktur
# Element --> key : value
from pprint import pprint

dictt = {'zehn' : 10, 'neun' : 9, 'acht' : 8, 
         'sieben' : 7, 'null' : 0}

# Zugriff erfolg über key und nicht Index!!
# key = 'neun'
# print(dictt.get('one', 'Unknown key'))
dictt['eins'] = 1


# iterieren über Dictionaries

# for key in  dictt:
#     value = dictt[key]
#     print('Key: %s Value: %s' % (key, value))

# for key, value in dictt.items():
#     print(key, value)

# # Gibt eine sortierte Liste der Keys
# dictt1 = sorted(dictt)
# print(dictt1)

# Der in Operator überprüft ob Key vorhanden ist.
print(dictt)

# Löscht key und sein Value
del dictt['null']
print(dictt)

# Liste der Values = Werte
# print(list(dictt.values()))

# Liste der Keys = Wert
print(list(dictt.keys()))

