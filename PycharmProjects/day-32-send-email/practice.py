import smtplib
import datetime as dt
import random

my_email = "serbnikolas@gmail.com"
password = "966542464063"

now = dt.datetime.now()
year = now.year
day_of_week = now.weekday()
if day_of_week == 5:
    with open('quotes.txt') as quotes_file:
        all_quotes = quotes_file.readlines()
        quote = random.choice(all_quotes)

    with smtplib.SMTP("smtp.gmail.com: 587") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email,
                            to_addrs='kolyasha@seznam.cz',
                            msg=f'Subject: Hello\n\nпривет')
