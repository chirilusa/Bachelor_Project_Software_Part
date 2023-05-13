import random
import csv

# Generate clothing combinations for different weather conditions
sunny_clothes = ["t-shirt", "shorts", "sandals"]
partly_cloudy_clothes = ["light sweater", "jeans", "sneakers"]
cloudy_clothes = ["sweater", "pants", "boots"]
rainy_clothes = ["rain jacket", "umbrella", "waterproof shoes"]
snowing_clothes = ["heavy coat", "hat", "gloves", "snow boots"]

# Define the range of weather parameters
min_temp = -10
max_temp = 30
min_humidity = 0
max_humidity = 100
min_wind_speed = 0
max_wind_speed = 50
min_luminosity = 0
max_luminosity = 10

# Generate random weather data for a year
with open('weather_data.csv', mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["Date", "Temperature (C)", "Humidity (%)", "Wind Speed (km/h)", "Luminosity (klux)", "Rain", "Umbrella", "Condition", "Clothes"])
    for month in range(1, 13):
        for day in range(1, 32):
            date = f"2022-{month:02d}-{day:02d}"
            temp = round(random.uniform(min_temp, max_temp), 1)
            humidity = random.randint(min_humidity, max_humidity)
            wind_speed = round(random.uniform(min_wind_speed, max_wind_speed), 1)
            luminosity = round(random.uniform(min_luminosity, max_luminosity), 1)
            rain = random.choice(["Yes", "No"])
            umbrella = "Yes" if rain == "Yes" else "No"
                
            # Determine the weather condition based on the temperature and luminosity
            if temp > 25 and luminosity > 5:
                condition = "Sunny"
                clothes = ", ".join(sunny_clothes)
            elif 15 <= temp <= 25 and luminosity <= 5:
                condition = "Partly Cloudy"
                clothes = ", ".join(partly_cloudy_clothes)              
            elif 5 <= temp < 15:
                condition = "Cloudy"
                clothes = ", ".join(cloudy_clothes)
            elif temp < 5 and rain == "Yes":
                condition = "Snowing"
                clothes = ", ".join(snowing_clothes)
            else:
                condition = "Rainy"
                clothes = ", ".join(rainy_clothes)
                
            # Add sunscreen to clothing combination if luminosity is high
            if luminosity > 5:
                clothes += ", sunscreen"
                
            writer.writerow([date, temp, humidity, wind_speed, luminosity, rain, umbrella, condition, clothes])
