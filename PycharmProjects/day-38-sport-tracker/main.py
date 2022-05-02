import requests

GENDER = 'male'
WEIGHT_KG = 68
WEIGHT_CM = 187
AGE = 23

API_KEY = 'cf6ce9197132596c6dddd3a456188185'
APP_ID = '3a60851a'

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
print(result)
