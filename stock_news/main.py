import requests
import os
from twilio.rest import Client

STOCK_NAME = "AMZN"
COMPANY_NAME = "Amazon.com Inc"
ACCOUNT_SID = "account_sid"
AUTH_TOKEN = "auth_token"
STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
STOCK_API_KEY = "stock_api_key"
NEWS_API_KEY="news_api_key"

client = Client(ACCOUNT_SID,AUTH_TOKEN)

stock_params = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK_NAME,
    "apikey": STOCK_API_KEY,
}

stock_response= requests.get(STOCK_ENDPOINT, params=stock_params)
data=stock_response.json()["Time Series (Daily)"]
data_list=[value for (key,value) in data.items()]

yesterday_data=data_list[0]
yesterday_closing_price=yesterday_data["4. close"]
print(yesterday_closing_price)

day_before_yesterday=data_list[1]
day_before_yesterday_closing_price=day_before_yesterday["4. close"]
print(day_before_yesterday_closing_price)

diff=float(yesterday_closing_price)-float(day_before_yesterday_closing_price)
up_down=None
if diff>0:
    up_down="↑"
else:
    up_down="↓"
diff_percent=round((diff/float(yesterday_closing_price))*100)
print(diff_percent)

news_params={
    "apiKey":NEWS_API_KEY,
    "qInTitle":COMPANY_NAME
}

if abs(diff_percent)>0:
    news_response=requests.get(NEWS_ENDPOINT,params=news_params)
    articles=news_response.json()["articles"]
    three_articles=articles[:3]
    formattted_articles=[f"{STOCK_NAME} : {up_down} {diff_percent}%\nHeadline:{article['title']} \nBrief:{article ['description']}" for article in articles]
    for article in formattted_articles:
        message = client.messages \
                    .create(
                        body=formattted_articles,
                        from_='+17726182826',
                        to='+91 00000000000'
                 )
print(message.status)