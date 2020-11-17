from flask import Flask, render_template, jsonify, request
import Adafruit_DHT
import time

DHT_SENSOR = Adafruit_DHT.DHT11
SENSOR_PIN = 4

app = Flask(__name__)

# route() decorator is used to bind URLs to functions
# can have multiple route() calls
@app.route('/')
def index():
    #humidity,temperature = Adafruit_DHT.read(DHT_SENSOR,SENSOR_PIN)
    #sensor_data = {"temp": temperature,"humidity": humidity}
    

    #print(sensor_data)
    return render_template("index.html")

@app.route('/progress')
def progress():
    humidity,temperature = Adafruit_DHT.read(DHT_SENSOR,SENSOR_PIN)
    sensor_data = {"temp": temperature,"humidity": humidity}
    print(sensor_data)
    return jsonify(sensor_data)

# This is where the server is ran debug=true means debugging is turned on
# host='0.0.0.0' is the address we are requesting to connect to
# Flask uses a built in web server that is light weight and NOT meant for production
if __name__ == '__main__':
    app.run(debug=True, host='10.0.0.233')
