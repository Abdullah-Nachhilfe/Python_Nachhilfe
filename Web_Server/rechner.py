from flask import Flask, request, render_template

app = Flask(__name__)

# Templating mit Jinja:
# Warum Templating?
# Was ist templating?
# Wie arbeiten mit Jinja?

# Einfaches Beispiel:

# 1. python von HTML trennen
# 2 zusammen bringen, wo wir brauchen


@app.route('/')
def index():

    return render_template('index.j2')


@app.route('/rechner')
def rechner():

    return render_template('rechner.j2')


@app.route('/lb_to_kg')
def lb_to_kg():
    
    if 'lb' in request.args:
        lb = float(request.args['lb'])
        kg = lb / 2.205
        return render_template('lb_to_kg.j2',
                               g_kg = kg, g_lb = lb)

    else:
        return 'Etwas ist schiefgelaufen'


@app.route('/K_to_C')
def K_to_C():
    if 'K' in request.args:
        K = float(request.args['K'])
        C = K - 273.15
        
        return render_template('K_to_C.j2', K = K, C = C)
    
    else:
        return 'Etwas ist schiefgelaufen'

if __name__ == '__main__':
    app.run()