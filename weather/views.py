'''Search weather report by Area Code(pincode)'''
from django.shortcuts import render
# import json to load json data to python dictionary
import json
# urllib.request to make a request to api
import urllib.request
import time

def home(request):
	t = time.strftime('%a, %d %B %I:%M %p')
	if request.method == 'POST':
		pincode = request.POST['pincode']
		source = urllib.request.urlopen(
			"http://api.openweathermap.org/data/2.5/weather?zip=" + pincode + ",in&appid=4fd469e60845f8a9b05ac3ce695d6c0f").read()

		# converting JSON data to a dictionary
		r = json.loads(source)
		# data for variable city
		city = {
			'pincode': pincode,
			'name': r["name"],
			'desc': r['weather'][0]['description'],
			'temp': int(r["main"]["temp"] - 273),
			'wind': "%.2f" % ((r["wind"]["speed"]) * 1.609344),
			'humidity': r["main"]["humidity"],
			'cloud': r["clouds"]["all"],
			'icon': r['weather'][0]['icon'],
			'time': t
		}
	else:
		city = {}
		''' you can get your own api_key from https://openweathermap.org/price 
			for that you need to sign up and you will get your api on mail,
			place api_key in place of appid ="your_api_key_here " '''
	return render(request, "home.html", city)
