import joblib
import numpy as np
from sklearn.ensemble import RandomForestClassifier

CONDITION_CATEGORICAL = {'Condition': {'Blowing snow': 1, 'Clear': 2, 'Cloudy': 3, 'Heavy rain at times': 4, 'Heavy snow': 5, 'Light freezing rain': 6, 'Light rain': 7, 'Light rain shower': 8, 'Light snow': 9, 'Light snow showers': 10, 'Moderate or heavy rain shower': 11, 'Moderate or heavy snow showers': 12, 'Moderate rain at times': 13, 'Moderate snow': 14, 'Overcast': 15, 'Partly cloudy': 16, 'Patchy heavy snow': 17, 'Patchy light rain': 18, 'Patchy light snow': 19, 'Patchy moderate snow': 20, 'Patchy rain possible': 21, 'Patchy snow possible': 22, 'Sunny': 23}}
PLACE_CATEGORICAL = {'Place': {'beach': 1, 'gym': 2, 'home': 3, 'office': 4, 'park': 5, 'party': 6, 'restaurant': 7, 'shopping mall': 8, 'ski resort': 9}}
CLOTHES_CATEGORICAL = {'Clothes': {'Athletic shorts, sport bra, sneakers': 1, 'Dress, heels shoes': 2, 'Dress, sandals': 3, 'Jeans, blouse, boots': 4, 'Jeans, blouse, coat, boots': 5, 'Jeans, blouse, raincoat, boots': 6, 'Jeans, hoodie,  sneakers': 7, 'Jeans, hoodie, raincoat, boots': 8, 'Jeans, hoodie, raincoat, sneakers': 9, 'Jeans, t-shirt, jacket, sneakers': 10, 'Jumpsuit, heels shoes': 11, 'Jumpsuit, jacket, elegant shoes': 12, 'Leggings, athletic shirt, sneakers': 13, 'Leggings, hoodie, raincoat, sneakers': 14, 'Leggings, hoodie, winter coat, boots': 15, 'Leggings, t-shirt, sneakers': 16, 'Leggins, t-shirt, raincoat, sneakers': 17, 'Leggins, t-shirt, running shoes': 18, 'Pants, blouse, heels shoes': 19, 'Pants, blouse, jacket, elegant shoes': 20, 'Pants, blouse, jacket, sneakers': 21, 'Pants, blouse, sneakers': 22, 'Pants, hoodie,  sneakers': 23, 'Pants, sweater, winter coat, boots, scarf': 24, 'Pants, t-shirt, raincoat, sneakers': 25, 'Pants, t-shirt, sneakers': 26, 'Pijamas': 27, 'Shorts, t-shirt, sandals': 28, 'Ski pants, thermal blouse, winter coat, boots, hat, scarf, gloves': 29, 'Skirt, blouse, elegant shoes': 30, 'Skirt, blouse, heels shoes': 31, 'Slacks, blouse, winter coat, boots': 32, 'Slacks, button-up shirt, boots': 33, 'Slacks, button-up shirt, coat, boots': 34, 'Slacks, button-up shirt, jacket, boots': 35, 'Slacks, button-up shirt, raincoat, boots': 36, 'Slacks, sweater, winter coat, boots': 37, 'Swinsuit, summer dress, flip-flops, hat': 38, 'Swinsuit, summer dress, sandals, hat': 39, 'Track pants, hoodie, raincoat, sneakers': 40, 'Track pants, hoodie, sneakers': 41, 'Track pants, hoodie, winter coat, boots': 42}}

model = joblib.load('../static/clothes_recommendation_model.pkl')
t = -5
c = 'Clear'
p = 1017.0
h = 77
l = 1.0
r = 0
place = 'ski resort'
c_encoded = CONDITION_CATEGORICAL['Condition'][c]
place_encoded = PLACE_CATEGORICAL['Place'][place]
X = np.array([t, c_encoded, p, h, l, r, place_encoded])
X = X.reshape(1, -1)
y = model.predict(X)
clothes = list(CLOTHES_CATEGORICAL['Clothes'].keys())[y[0]-1]
print(clothes)