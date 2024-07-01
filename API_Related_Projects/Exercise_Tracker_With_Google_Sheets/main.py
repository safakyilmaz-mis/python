from datetime import datetime

import requests

APP_ID = "YOUR APP ID"
URL = "https://trackapi.nutritionix.com/v2/natural/exercise"

header = {
    "x-app-id": "YOUR_ID",
    "x-app-key": "YOUR_APP_KEY",
}

user_input = input("Which excercise you did?: ")

params = {
    "query": user_input,
    "weight_kg": "YOUR_WEIGHT",
    "height_cm": "YOUR_HEIGHT",
    "age": "YOUR_AGE",
}

response = requests.post(url=URL, json=params, headers=header)
# print(response.json()["exercises"][0]["name"])

ACTIVITY = response.json()["exercises"][0]["name"]
print(ACTIVITY)
DURATION = response.json()["exercises"][0]["duration_min"]
CALORIES = response.json()["exercises"][0]["nf_calories"]

time_for_sheety = datetime.now()
date_sheety = f"{time_for_sheety.today().day}/{time_for_sheety.today().month}/{time_for_sheety.today().year}"
# time_for_sheety.strftime("")
time_sheety = f"{time_for_sheety.today().hour}:{time_for_sheety.today().minute}:{time_for_sheety.today().second}"

URL_SHEETY = "YOUR SHEETY ADDRESS"

PARAMS_SHEETY = {
    "sheet1":
      {
            "calories": CALORIES,
            "date": date_sheety,
            "time": time_sheety,
            "exercise": ACTIVITY,
            "duration": DURATION,
        }

}

LOGIN_PARAMS = {
    "Authorization": "YOUR AUTH CODE"
}


response2 = requests.post(url=URL_SHEETY, json=PARAMS_SHEETY, headers=LOGIN_PARAMS)

# print(response2.text)
#
# print(requests.get(url=URL_SHEETY).text)

