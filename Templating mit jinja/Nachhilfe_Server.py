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


if __name__ == '__main__':
    app.run()
