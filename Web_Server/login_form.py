from flask import Flask, request

app = Flask(__name__)

@app.route('/login_form')
def login_form():
    
    return '''
            <form action="/login" method = "POST">
                <p>
                    Username:
                    <input type="text" name="name">
                </p>
                <p>
                    Passwort:
                    <input type="password" name = "pw">
                </p>
                <input type="submit" value="login" >
                
            </form>'''

# Nachteile: - debugging 
# Wir können GET und POST zusammen verwenden
@app.route('/login', methods = ['POST', 'GET'])
def login():
    if request.method == 'POST':
        name = request.form['name']
        pw = request.form['pw']
    if request.method == 'GET':
        name = request.args['name']
        pw = request.args['pw']
    return 'Hallo, %s! Du hast die %s-Methode verwendet' % (name,request.method) 



























if __name__ == '__main__':
    app.run()