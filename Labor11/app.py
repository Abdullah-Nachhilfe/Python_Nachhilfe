from flask import Flask, send_file, render_template, request
import readData


app = Flask(__name__)

a = 'key'




@app.route('/')
def helloworld():

    return render_template('index.html')

@app.route('/weather_data')
def show_weather_data():
    if 'city_name' in request.args:
        city_name = request.args['city_name']
        wetter = readData.get_weather_data(city_name)
        
        return render_template('show_weather.j2', wetter = wetter)
    else:
        return 'Etwas ist falsch'
if __name__ == '__main__':
    app.run()