import requests
from datetime import datetime
import os

today_date = datetime.now().strftime("%d/%m/%Y")
now_time = datetime.now().strftime("%X")

GENDER = 'male'
WEIGHT_KG = 68
WEIGHT_CM = 187
AGE = 23

sheet_endpoint = 'https://api.sheety.co/96b85a69d38d890adf468ad958709c2e/workout/workouts'

API_KEY = 'cf6ce9197132596c6dddd3a456188185'
APP_ID = '3a60851a'
MY_USERNAME = 'kolyasch'
MY_PASSWORD = 'yU4Z4?zUtugW'

exercise_endpoint = 'https://trackapi.nutritionix.com/v2/natural/exercise'

exercise_text = input('Tell me which exercises you did: ')

parameters = {
    "query": exercise_text,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": WEIGHT_CM,
    "age": AGE
}

headers = {
    'x-app-id': APP_ID,
    'x-app-key': API_KEY
}

response = requests.post(exercise_endpoint, json=parameters, headers=headers)
result = response.json()

for exercise in result["exercises"]:
    sheet_inputs = {
        "workout": {
            'date': today_date,
            'time': now_time,
            'exercise': exercise['name'].title(),
            'duration': exercise['duration_min'],
            'calories': exercise['nf_calories']
        }
    }

    sheet_response = requests.post(sheet_endpoint, json=sheet_inputs, auth=(MY_USERNAME, MY_PASSWORD))
    print(sheet_response.text)
