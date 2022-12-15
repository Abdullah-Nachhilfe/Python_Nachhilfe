from flask import Flask, request
# URL Pfad + Query

app = Flask(__name__) # Konstruktor-Aufruf -> Flask

@app.route('/') # Decorator -> Definiert die Pfad-Regel

def index(): # View-Funktion
    
    return '''<title>Startseite</title>
                <h1>Startseite von meinem Web-Server</h1>
                '''

@app.route('/Nachhilfe')
def nachhilfe(): # View-Funktion
    
    return 'Diese ist <em>Nachhilfe</em>'

@app.route('/MeinPfad')
def MeinPfad(): # View-Funktion
    
    return '<h1>Der Pfad hier ist MeinPfad</h1>'

# Pfad-Variabeln
@app.route('/hallo/<name>')
def hallo(name): # View-Funktion
    
    return ' Hallo, %s!' % name

@app.route('/dividiere')
def dividiere():
   a = request.args['a']
   b = request.args['b']
   c = int(a)/ int(b)
   return '%s / %s = %s' % (a, b, c)

@app.route('/spiegel')

def spiegel():
    if 'wort' in request.args:
        wort = request.args['wort']
        return wort[::-1]
    else:
        return 'Du hast einen Flaschen Key im Query angegeben'


if __name__ == '__main__':
    app.run()