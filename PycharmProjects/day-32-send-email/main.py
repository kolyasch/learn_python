import smtplib
import datetime as dt
import pandas


my_email = "serbnikolas@gmail.com"
password = "966542464063"

data = pandas.read_csv('birthdays.csv')


now = dt.datetime.now()
today_tuple = (now.month, now.day)


birthdays_dict = {(data_row.month, data_row.day): data_row for (index, data_row) in data.iterrows()}

if today_tuple in birthdays_dict:
    birthday_person = birthdays_dict[today_tuple]
    with smtplib.SMTP("smtp.gmail.com: 587") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email,
                            to_addrs=birthday_person['email'],
                            msg=f'Subject: С днём рождения!\n\nЧекни ЛОЛ))!)!))!)')
