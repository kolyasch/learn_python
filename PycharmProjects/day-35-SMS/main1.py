import requests
import os
from twilio.rest import Client
from twilio.http.http_client import TwilioHttpClient

OWM_Endpoint = 'https://api.openweathermap.org/data/2.5/onecall'
api_key = '05f8dce18baf8ff0ed3bcbe85507667d'
account_sid = 'AC4fd856e13a9056d7a69ed2b47e725163'
auth_token = 'ba5c7868625263d5fda3f61fb859052c'
MY_LAT = 41.82
MY_LONG = 41.77528

weather_params = {
    'lat': 49.195061,
    'lon': 16.606836,
    'appid': api_key,
    'exclude': 'current, minutely, daily'
}

response = requests.get(OWM_Endpoint, params=weather_params)
response.raise_for_status()
weather_data = response.json()
weather_slice = weather_data['hourly'][9:12]

for hour_data in weather_slice:
    condition_code = hour_data['weather'][0]['id']
    if condition_code < 700:
        proxy_client = TwilioHttpClient()
        """This code we need to update our pythonanywhere account"""
        proxy_client.session.proxies = {'https': os.environ['https_proxy']}

        client = Client(account_sid, auth_token, http_client=proxy_client)
        message = client.messages.create(
            body='Кажется дождь собирается... Возьми зонтик!☂️',
            from_='+16204624508',
            to='+995568831889'
        )
        print(message.status)
        break
