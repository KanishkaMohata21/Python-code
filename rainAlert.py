import requests
import os
from twilio.rest import Client

account_sid = os.environ.get("ACCOUNT_SID")
auth_token = os.environ.get("AUTH_TOKEN")


client = Client(account_sid, auth_token)

endpoint = "https://api.openweathermap.org/data/2.5/weather?"
api_key = os.environ.get("OWM_API_KEY")

weather_params = {
    "lat": 19.07609019,
    "lon": 72.877426,
    "appid": api_key 
}

response = requests.get(endpoint, params=weather_params)
response.raise_for_status()
weather_data = response.json()
condition_code=weather_data["weather"][0]["id"]
if condition_code<700:
    message = client.messages \
                .create(
                     body="Get your umbrella",
                     from_='+17726182826',
                     to='+91 00000000000'
                 )
else:
    message = client.messages \
                .create(
                     body="Donot get your umbrella ",
                     from_='+17726182826',
                     to='+91 00000000000'
                 )
print(message.status)



