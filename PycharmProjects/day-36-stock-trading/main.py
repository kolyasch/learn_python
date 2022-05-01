import requests
from twilio.rest import Client

account_sid = 'AC4fd856e13a9056d7a69ed2b47e725163'
auth_token = 'ba5c7868625263d5fda3f61fb859052c'

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"
STOCK_KEY_API = '52UDTWONP5VDODQC'
API_key_news = '7dabf39caa3f44b6a472f443bd2dedf9'

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

stock_params = {
    'function': 'TIME_SERIES_DAILY',
    'symbol': STOCK_NAME,
    'apikey': STOCK_KEY_API
}
response = requests.get(STOCK_ENDPOINT, params=stock_params)
data = response.json()['Time Series (Daily)']
yesterday = data
data_list = [value for (key, value) in data.items()]
yesterday_data = data_list[0]
yesterday_closing_price = float(yesterday_data['4. close'])
print(yesterday_closing_price)

day_before_yesterday_day = data_list[1]
day_before_yesterday_closing_price = float(day_before_yesterday_day['4. close'])
print(day_before_yesterday_closing_price)

difference = yesterday_closing_price - day_before_yesterday_closing_price
up_down = None
if difference > 5:
    up_down = '📈'
else:
    up_down = '📉'

percent = abs(100 - (yesterday_closing_price * 100 / day_before_yesterday_closing_price))
print(percent)

news_params = {
    'qInTitle': COMPANY_NAME,
    'apiKey': API_key_news
}
response2 = requests.get(NEWS_ENDPOINT, params=news_params)
data1 = response2.json()['articles']
three_articles = data1[:3]
formatted_articles = [f"{STOCK_NAME}: {up_down}{round(percent)}%\nHeadline: {article['title']}. \nBrief: {article['description']}" for article in three_articles]
if percent > 0:
    client = Client(account_sid, auth_token)
    for article in formatted_articles:
        message = client.messages.create(
            body=article,
            from_='+16204624508',
            to='+995568831889'
        )
        print(message.status)
