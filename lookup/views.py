# This is the views.py file
from django.shortcuts import render

def home(request):
	import json
	import requests

	if request.method =="POST":
		city = request.POST['city']
		api_request = requests.get("http://api.airvisual.com/v2/city?city=" + city + "&state=Uttar Pradesh&country=India&key=74d27ae2-c8b0-4aa2-896d-43f3add89e90")
		try:
			api = json.loads(api_request.content)

		except Exception as e:
			api = "Error..."

		return render(request, 'home.html', {'api': api})
	else:
		api_request = requests.get("http://api.airvisual.com/v2/city?city=Lucknow&state=Uttar Pradesh&country=India&key=74d27ae2-c8b0-4aa2-896d-43f3add89e90")
		try:
			api = json.loads(api_request.content)

		except Exception as e:
			api = "Error..."

		return render(request, 'home.html', {'api': api})

def base(request):
	import json
	import requests

	api_request = requests.get("http://samples.openweathermap.org/data/2.5/weather?q=Kolkata,in&appid=b6907d289e10d714a6e88b30761fae22")

	try:
		api = json.loads(api_request.content)

	except Exception as e:
		api = "Error..."

	return render(request, 'base.html', {'api': api})
