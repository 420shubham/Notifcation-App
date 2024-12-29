import requests
from twilio.rest import Client
import os

<<<<<<< HEAD
=======
account_sid = "enter from account"


>>>>>>> caf102e (removed the auth key)

 


MY_LAT = 27.712021
MY_LNG = 85.312950
API_KEY = os.environ.get("WEATHER_API_KEY")
BASE_URL ="https://api.openweathermap.org/data/2.5/weather"


parameters = {
    "lat": MY_LAT,
    "lon": MY_LNG,
    "appid": API_KEY,
}



# parameters = {
#     ("lat", "lon"):(MY_LAT, MY_LNG),
#     "appid": API_KEY,
# }


parameter1 = {
    "q": "Kathmandu,nepal",
    "appid":API_KEY
}


response = requests.get(BASE_URL, params=parameters)
response.raise_for_status()
data = response.json() 

print(response.status_code)
print(data["weather"][0]["main"])
print(data["weather"][0]["id"])


weather_condition = data["weather"][0]["id"]

if weather_condition > 700:
    client = Client(account_sid, API_KEY)
    message = client.messages.create(
    body="Join Earth's mightiest heroes. Like Kevin Bacon.",
    from_="+12315186588",
    to="+9779866140040",
    )

print(message.status)
