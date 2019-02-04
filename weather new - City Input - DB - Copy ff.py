#from win10toast import ToastNotifiers
#from win32api import GetModuleHandle

import requests
import threading
import json
from win10toast import *
from win32api import *
from pprint import pprint

def get_weather_type(json_data):
	weather=json_data['weather'][0]['description']
	return weather

def get_temperature(json_data):
	temp=json_data['main']['temp']
	return temp

def get_wind_speed(json_data):
	speed=json_data['wind']['speed']
	return speed

def weather_data(json_data, city):
	weather_type=get_weather_type(json_data)
	weather_temp=get_temperature(json_data)
	weather_speed=get_wind_speed(json_data)
	#print("Weather in {} is {} with temperature of {} °C blowing wind speed at {} mps".format(city,weather_type,(weather_temp-273.15),weather_speed))
	print1=str("Weather in {} is {} with temperature of ".format(city,weather_type))
	print2=str("{0:.2f}".format(weather_temp-273.15))
	print3=str("°C blowing wind speed at {} mps".format(weather_speed))
	finalprint=print1+print2+print3
	notifier = ToastNotifier()
	notifier.show_toast("Weather",str(finalprint),duration=10)
	threading.Timer(15,weather_data(json_data,city)).start()

def main ():
	city=input("Enter City: ")
	lowercity=city.lower()
	with open('city.list.json', 'r',encoding="utf8") as f:
		data=json.load(f)
		for i in data:
			cityname=i['name']
			if ((cityname.lower()) == lowercity):
				cityid_get=str(i['id'])
	api_location='https://api.openweathermap.org/data/2.5/weather?id=cityid&appid=6eadbe87ddf48f24cd3be8d7dd3e54e9'
	api_location=api_location.replace('cityid',cityid_get)
	json_data=requests.get(api_location).json()
	weather_main=weather_data(json_data,city)

main ()
