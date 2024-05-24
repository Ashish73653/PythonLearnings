import requests
from datetime import datetime

user_api = "904b5c5734ac6e05328542bc49da2290"
city = input("Enter city name: ")
countryCode = input("Enter country code: ")

complete_api_link = "https://api.openweathermap.org/data/2.5/weather?q="+city+","+countryCode+"&appid="+user_api
api_link = requests.get(complete_api_link)
api_data = api_link.json()

temp_city = ((api_data['main']['temp'])-273.15)
weather_desc = api_data['weather'][0]['description']
feelsLike = ((api_data['main']['feels_like'])-273.15)
hmdt = api_data['main']['humidity']
wind_spd = api_data['wind']['speed']
date_time = datetime.now().strftime("%d %b %Y  |  %I:%M:%S %p")

print("----------------------------------------------")
print("Weather Stats for -{} || {}".format(city.upper(), date_time))
print("----------------------------------------------")
print("Current temperature is: {:.2f} deg C".format(temp_city))
print("Current weather desc  :", weather_desc)
print("Feels like            : {:.2f} deg C".format(feelsLike))
print("Current Humidity      :", hmdt, '%')
print("Current wind speed    :", wind_spd, 'kmph')
print("----------------------------------------------")
