import requests
from datetime import datetime
import smtplib
import time
MY_LAT = 41.82
MY_LONG = 41.77528
my_email = "serbnikolas@gmail.com"
password = "966542464063"


def is_iss_overhead():
    response1 = requests.get(url='http://api.open-notify.org/iss-now.json')
    response1.raise_for_status()

    data1 = response1.json()

    latitude = float(data1['iss_position']['latitude'])
    longitude = float(data1['iss_position']['longitude'])
    if MY_LAT - 5 <= latitude <= MY_LAT + 5 and MY_LONG - 5 <= longitude <= MY_LONG + 5:
        print('look up')
        return True
    print(latitude, longitude)


def is_night():
    parameters = {
        'lat': MY_LAT,
        'lng': MY_LONG,
        'formatted': 0
    }

    response = requests.get(url='http://api.sunrise-sunset.org/json', params=parameters)
    response.raise_for_status()
    data = response.json()['results']
    sunrise = int(data['sunrise'].split('T')[1].split(':')[0])
    sunset = int(data['sunset'].split('T')[1].split(':')[0])

    print(sunrise)
    print(sunset)

    time_now = datetime.now().hour
    if time_now >= sunset or time_now <= sunrise:
        return True

while True:

    if is_iss_overhead() and is_night():
        with smtplib.SMTP("smtp.gmail.com: 587") as connection:
            connection.starttls()
            connection.login(user=my_email, password=password)
            connection.sendmail(from_addr=my_email,
                                to_addrs='kolyasch1999@mail.ru',
                                msg=f'Subject: MKC\n\nглянь на небо!')
    time.sleep(60)
