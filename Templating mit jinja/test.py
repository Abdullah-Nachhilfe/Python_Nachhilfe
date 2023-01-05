getränke = [{'num': 1, 'bezch': 'Cafe Creama', 'preis': '1.80'},
            {'num': 2, 'bezch': 'Cappucchino', 'preis': '2.60'},
            {'num': 3, 'bezch': 'Latte Macchiato', 'preis': '3.20'}]




for getränk in getränke:
    num = getränk['num']
    preis = getränk['preis']
    bezeichnung = getränk['bezch']
    ausgabe = '<a href = "/getränke/%s/preis"> %s</a><strong>%s</strong>' % (num, bezeichnung,preis)
    print(ausgabe)
    



name = 'hilfe'
vorname = 'Nach'

print(vorname + name)