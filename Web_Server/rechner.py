from flask import Flask, request

app = Flask(__name__)

# 1. Start Seite hat Mehrere Web-Formulare zum Rechnen
# 2. Verabrebeiten
# 3. Darstellen

@app.route('/')
def index():
    
    return '''<h1>Herzlich Willkommen zu diesem sehr guten Rechner</h1>
            Pound to kg
            <form action="/lb_to_kg">
            <input type="text" name="lb">
            <input type="submit" value = "rechne">
            </form>
            Kelvin to Celsius
            <form action="/K_to_C">
            <input type="text" name="K">
            <input type="submit" value = "rechne">
            </form>'''

@app.route('/lb_to_kg')
def lb_to_kg():
    if 'lb' in request.args:
        lb = float(request.args['lb'])
        kg = lb/2.2046
        return '%slb = %skg' % (lb, kg)
    else:
        return 'Etwas ist schiefgelaufen'

@app.route('/K_to_C')
def K_to_C():
    if 'K' in request.args:
        K = float(request.args['K'])
        C = K - 273.15
        
        return '%sK = %.2f°C' % (K,C)
    else:
        return 'Etwas ist schiefgelaufen'
    
if __name__ == '__main__':
    app.run()