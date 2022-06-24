import requests
import pandas as pd
from geopy.geocoders import Nominatim

geolocator = Nominatim(user_agent='your_app_name')

street_address = input("Enter your street address:\n")

city = input("Enter your city:\n")

state = input("Enter your state (abbreviated):\n")

zip_code = input("Enter your zip code:\n")

address = street_address+", "+city+", "+state+", "+zip_code

location = geolocator.geocode(address)

lat, lon = location.latitude, location.longitude

url = "https://maps.googleapis.com/maps/api/place/nearbysearch/json?location=+"+str(lat)+"%2C"+str(lon)+"&radius=1500&type=restaurant&keyword=cruise&key=AIzaSyBMhAl3wOF9iEfdawnaFZM8yaH8C08IZ5k"

payload={}
headers = {}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)
