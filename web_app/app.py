from flask import Flask, request, render_template
import joblib
import numpy as np
import requests
import board
import Adafruit_DHT
import busio
import digitalio
import adafruit_bmp280
import RPi.GPIO as GPIO
from adafruit_veml6070 import VEML6070

# export FLASK_ENV=development
app = Flask(__name__)

CATEGORICAL_DATA = {
    'Place': {'beach': 1, 'gym': 2, 'home': 3, 'office': 4, 'park': 5, 'party': 6, 'restaurant': 7, 'shopping mall': 8},
    'Clothes': {'Athletic shorts, sport bra, sneakers': 1, 'Dress, heels shoes': 2, 'Dress, sandals': 3, 'Jeans, blouse, boots': 4, 'Jeans, blouse, coat, boots': 5, 'Jeans, blouse, raincoat, boots': 6, 'Jeans, hoodie,  sneakers': 7, 'Jeans, hoodie, raincoat, boots': 8, 'Jeans, hoodie, raincoat, sneakers': 9, 'Jeans, t-shirt, jacket, sneakers': 10, 'Jumpsuit, heels shoes': 11, 'Jumpsuit, jacket, elegant shoes': 12, 'Leggings, athletic shirt, sneakers': 13, 'Leggings, hoodie, raincoat, sneakers': 14, 'Leggings, hoodie, winter coat, boots': 15, 'Leggings, t-shirt, sneakers': 16, 'Leggins, t-shirt, raincoat, sneakers': 17, 'Leggins, t-shirt, running shoes': 18, 'Pants, blouse, heels shoes': 19, 'Pants, blouse, jacket, elegant shoes': 20, 'Pants, blouse, jacket, sneakers': 21, 'Pants, blouse, sneakers': 22, 'Pants, hoodie,  sneakers': 23, 'Pants, sweater, winter coat, boots, scarf': 24, 'Pants, t-shirt, raincoat, sneakers': 25, 'Pants, t-shirt, sneakers': 26, 'Pijamas': 27, 'Shorts, t-shirt, sandals': 28, 'Ski pants, thermal blouse, winter coat, boots, hat, scarf, gloves': 29, 'Skirt, blouse, elegant shoes': 30, 'Skirt, blouse, heels shoes': 31, 'Slacks, blouse, winter coat, boots': 32, 'Slacks, button-up shirt, boots': 33, 'Slacks, button-up shirt, coat, boots': 34, 'Slacks, button-up shirt, jacket, boots': 35, 'Slacks, button-up shirt, raincoat, boots': 36, 'Slacks, sweater, winter coat, boots': 37, 'Swinsuit, summer dress, flip-flops, hat': 38, 'Swinsuit, summer dress, sandals, hat': 39, 'Track pants, hoodie, raincoat, sneakers': 40, 'Track pants, hoodie, sneakers': 41, 'Track pants, hoodie, winter coat, boots': 42}
    }

# Load the model
model = joblib.load('../static/clothes_recommendation_model.pkl')

# Set up DHT22
DHT_SENSOR = Adafruit_DHT.DHT22
DHT_PIN = 4

def read_dht22_sensor():
    humidity, temperature = Adafruit_DHT.read_retry(DHT_SENSOR, DHT_PIN)
    if humidity is not None and temperature is not None:
        return round(temperature, 2), round(humidity, 2)
    else:
        return None, None


# Set up VEML6070
i2c = busio.I2C(board.SCL, board.SDA)
uv = VEML6070(i2c)


def read_veml6070_sensor():
    uv_intensity = uv.uv_raw
    uv_condition = uv.get_index(uv_intensity)
    uv_index = int((uv_intensity * 5) / 1024)
    return uv_index


# Set up BMP280
spi = board.SPI()
cs = digitalio.DigitalInOut(board.D5)
sensor = adafruit_bmp280.Adafruit_BMP280_SPI(spi, cs)

def read_bmp280_sensor():
    temperature_c_bmp = sensor.temperature
    pressure_hpa = sensor.pressure
    return round(temperature_c_bmp, 2), round(pressure_hpa, 2)


# Set up rain sensor
rain_pin = 17
GPIO.setmode(GPIO.BCM)
GPIO.setup(rain_pin, GPIO.IN)


def read_rain_sensor():
    if GPIO.input(rain_pin):
        return 0
    else:
        return 1

API_KEY = "35d3c9f2e0ea47358c590558231806"
LOCATION = "Cluj-Napoca"


def get_api_data():
    url = f"http://api.weatherapi.com/v1/current.json?key={API_KEY}&q={LOCATION}&aqi=no"
    response = requests.get(url)
    data = response.json()
    return data["current"]


@app.route('/', methods=['GET', 'POST'])
def home():
    datetoday = get_api_data()["last_updated"][0:10]
    icon = get_api_data().get('condition').get('icon')
    
    # Citire senzor DHT22 
    temperature_c_dht, humidity = read_dht22_sensor()
    # Citire senzor BMP280 
    temperature_c_bmp, pressure_hpa = read_bmp280_sensor()

    temperature = round((temperature_c_bmp + temperature_c_dht)/2.0, 1)

    # Citire senzor de ploaie 
    rain = read_rain_sensor()

    condition = get_api_data().get('condition').get('text')
    
    context = {
        'datetoday': datetoday, 
        'icon': icon,
        'temperature': temperature,
        'condition': condition,
        'selected_place': 'beach',
        'places': CATEGORICAL_DATA.get('Place').keys()
    }

    if 'sunny' in condition.lower():
        context['accessory'] = 'Take your sunglasses!'
    elif 'overcast' in condition.lower() or 'rain' in condition.lower() or rain == 1:
        context['accessory'] = 'Take your umbrella!'

    if request.method == 'POST':
        # Citire senzor VEML6070 
        uv_index = read_veml6070_sensor()

        selected_place = request.form.get('place')
        context['selected_place'] = selected_place

        if selected_place in CATEGORICAL_DATA['Place']:
            place_encoded = CATEGORICAL_DATA['Place'][selected_place]
        else:
            place_encoded = CATEGORICAL_DATA['Place']['home']

        print("\nTemp={:.2f}*C  Humidity={:.2f}% UV Index={} BMP Press={:.2f} Rain={}\n".format(temperature, humidity, uv_index, pressure_hpa, rain))

        X = np.array([temperature, pressure_hpa, humidity, uv_index, rain, place_encoded])
        X = X.reshape(1, -1)
        y = model.predict(X)
        clothes = list(CATEGORICAL_DATA['Clothes'].keys())[y[0]-1]
        clothes = clothes.split(", ")
        context['clothes'] = clothes

    return render_template('home.html', context=context)

if __name__ == '__main__':
    app.run(debug=True)