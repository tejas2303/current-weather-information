import requests

from datetime import datetime

api_key = '44e1c2feea0cad1c7cde530241c003e5'
location = input("Enter the city name: ")
location = location.lower()

complete_api_link = "https://api.openweathermap.org/data/2.5/weather?q="+location+"&appid="+api_key
api_link = requests.get(complete_api_link)
api_data = api_link.json()

temp_city = ((api_data['main']['temp']) - 273.15)
presure_city = api_data['main']['pressure']
weather_desc = api_data['weather'][0]['description']
hmdt = api_data['main']['humidity']
wind_spd = api_data['wind']['speed']
date_time = datetime.now().strftime("%d %b %Y | %I:%M:%S %p")

shapeai = open('Weather Data.txt', 'w')


shapeai.write("\n-------------------------------------------------------------")
shapeai.write("\nWeather shows for - {}  || {}".format(location.upper(), date_time))
shapeai.write("\n-------------------------------------------------------------")

shapeai.write("\n\nCurrent temperature is: {:.2f} deg C".format(temp_city))
shapeai.write("\nCurrent pressure is   : {:.2f} hPa ".format(presure_city))
shapeai.write("\nCurrent Humidity      : %d percent" %hmdt)
shapeai.write("\nCurrent wind speed    : %d kmph" %wind_spd)
shapeai.write("\nCurrent weather desc  : %s" %weather_desc)


shapeai.close()
print("")