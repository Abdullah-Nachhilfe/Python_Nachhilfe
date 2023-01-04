from flask import Flask, request, render_template

app = Flask(__name__)

#########
# ware = ['Maus', 'Tastatur', 'Lautsprecher', 'Bildschirm', 'Tasse']

ware = {'Maus': 20, 'Tastatur': 19, 'Lautsprecher': 25, 'Bildschirm': 10, 'Tasse': 50}
ware['Wasserflasche'] = 100
ware['Teekanne'] = 200

@app.route('/')
def index():
    
    return render_template('shop.j2', ware_template = ware)



if __name__ == '__main__':
    app.run()