import csv
import requests
import json
from datetime import datetime, timedelta

# with open("weather.csv", "w", newline="") as csv_file:
#      writer = csv.writer(csv_file)
#      writer.writerow(["Location", "Date", "Hour", "Temperature", "Condition", "Pressure", "Humidity", "Luminosity", "WillItRain"])

# Set up the API URL and parameters
api_key = "2d40cb06c0684a67b2f134845231803"
location = "Cluj-Napoca"

year = 2023
month = '03'
month_days = 31
for day in range(1, month_days + 1):
    if day < 10:
        history_date = f"{year}-{month}-0{day}"
    else:
        history_date = f"{year}-{month}-{day}"
    
    url = f"https://api.weatherapi.com/v1/history.json?key={api_key}&q={location}&dt={history_date}"


    # Make a request to the API and get the response
    response = requests.get(url)
    data = response.json()
    print(response.status_code)
    # Allows us to convert a python object into an equivalent JSON object (dump())
    # with open("data.json", "w", newline="") as file:
    #     json.dump(data, file, indent = 2)   
    
    # # Parse the data into a CSV file
    with open("weather.csv", "a", newline="") as csv_file:
        writer = csv.writer(csv_file)
        hours = data["forecast"]["forecastday"][0]["hour"]
        for i in range(len(hours)):
            writer.writerow([location, hours[i]["time"].split(' ')[0], hours[i]["time"].split(' ')[1], hours[i]["temp_c"], hours[i]["condition"]["text"], hours[i]["pressure_mb"],  hours[i]["humidity"], hours[i]["uv"], hours[i]["will_it_rain"]])
# # Parse the data into a CSV file
# with open("weather.csv", "w", newline="") as csv_file:
#     writer = csv.writer(csv_file)s
#     writer.writerow(["Location", "Temperature", "Condition", "Wind", "Pressure", "Precipitation", "Humidity", "Luminosity"])
#     
