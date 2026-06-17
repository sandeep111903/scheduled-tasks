import os

import requests
from twilio.rest import Client


account_sid =  os.getenv("TWILIO_ACCOUNT_SID")
auth_token = os.getenv("TWILIO_AUTH_TOKEN")
print("SID from env:", account_sid)
print("Token from env:", auth_token)
client = Client(account_sid, auth_token)


Weather_Base_URL = "https://api.openweathermap.org/data/2.5/forecast"
Weather_API_KEY = os.getenv("TWILIO_API_KEY")
LATITUDE = 51.9522
LONGITUDE = 5.8484

query_params = {
    "lat": LATITUDE,
    "lon": LONGITUDE,
    "appid": Weather_API_KEY,
    "cnt": 4
}

response = requests.get(Weather_Base_URL, params=query_params)
response.raise_for_status()
weather_data = response.json()

will_rain = False
for weather in weather_data["list"]:
    for condition in weather["weather"]:
        if condition["id"] < 800:
            will_rain = True
if will_rain:
    message = client.messages.create(
        from_='whatsapp:+14155238886',
        body="Its going to rain in arnhem",
        to='whatsapp:+919160029944'
    )
# print(weather_data)
# print(weather_data["list"][0]["weather"][0]["id"])
