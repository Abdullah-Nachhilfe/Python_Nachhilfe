from flask import Flask, render_template, request

tiere_dict = { 'raccoon': 'Waschbär',
'manatee': 'Seekuh',
'meerkat': 'Erdmännchen' }



app = Flask(__name__)

@app.route('/')
def index():
    
    return render_template('index.j2')


@app.route('/tiere')
def tiere():
    
    return render_template('tiere.j2', tiere_dict = tiere_dict)



## Klausur Beispiel:
getraenke = [{'num': 1, 'bezeichnung': 'Cafe Creama', 'preis': '1.80'},
            {'num': 2, 'bezeichnung': 'Cappucchino', 'preis': '2.60'},
            {'num': 3, 'bezeichnung': 'Latte Macchiato', 'preis': '3.20'}]


@app.route('/getraenke')
def getraenk():
    
    return render_template('menu.html' ,items = getraenke)

if __name__ == '__main__':
    app.run()
