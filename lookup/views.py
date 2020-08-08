from django.shortcuts import render



# Create your views here.
def home(request):
	import json
	import requests



	if request.method == "POST":
		zipcode = request.POST['zipcode']
		api_request = requests.get('http://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode='+ zipcode +'&distance=5&API_KEY=5D6254D7-9600-491A-861A-3A8E8F41647F')
		try:
			api = json.loads(api_request.content)

		except Exception as e:
			api = 'error'


		if api[1]['Category']['Name'] == "Good" :
			cat_desription= '(0-50) Air Quality is considered satisfactory, and air pollution poses little or no risk.'
			cat_color = 'good'
		elif api[1]['Category']['Name'] == "Moderate": 
			cat_desription = '(51-100) If you are unusually sensitive to particle pollution, consider reducing your activity level or shorten the amount of time you are active outdoors.'
			cat_color = 'moderate '
		elif api[1]['Category']['Name']== "Unhealthy for Sensitve Groups": 
			cat_desription = '(101-150) People with lung disease are at risk for health effects.'
			cat_color = 'usg'
		elif api[1]['Category']['Name'] == "Unhealthy":
			cat_desription = '(151-200) Everyone may experience health effects, members of sensitve groups may experience more serious health effects.'
			cat_color = 'unhealthy'
		elif api[1]['Category']['Name'] == "Very Unhealthy":
			cat_desription ='(201-300) Health alert: everyone may experience more serious health effects.'
			cat_color = 'veryunhealthy'
		elif api[1]['Category']['Name'] == "Hazardous" :
			cat_desription = '(301-500) Health warnings of emergency conditions. The entire population is more likely to be effected.'
			cat_color = 'hazardous'



		return render(request, 'home.html', 
			{'api' : api, 
			'cat_desription': cat_desription, 
			'cat_color' : cat_color,})


	else:

		api_request = requests.get('http://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=37890&distance=5&API_KEY=5D6254D7-9600-491A-861A-3A8E8F41647F')
		try:
			api = json.loads(api_request.content)

		except Exception as e:
			api = 'error'


		if api[1]['Category']['Name'] == "Good" :
			cat_desription= '(0-50) Air Quality is considered satisfactory, and air pollution poses little or no risk.'
			cat_color = 'good'
		elif api[1]['Category']['Name'] == "Moderate": 
			cat_desription = '(51-100) If you are unusually sensitive to particle pollution, consider reducing your activity level or shorten the amount of time you are active outdoors.'
			cat_color = 'moderate '
		elif api[1]['Category']['Name']== "Unhealthy for Sensitve Groups": 
			cat_desription = '(101-150) People with lung disease are at risk for health effects.'
			cat_color = 'usg'
		elif api[1]['Category']['Name'] == "Unhealthy":
			cat_desription = '(151-200) Everyone may experience health effects, members of sensitve groups may experience more serious health effects.'
			cat_color = 'unhealthy'
		elif api[1]['Category']['Name'] == "Very Unhealthy":
			cat_desription ='(201-300) Health alert: everyone may experience more serious health effects.'
			cat_color = 'veryunhealthy'
		elif api[1]['Category']['Name'] == "Hazardous" :
			cat_desription = '(301-500) Health warnings of emergency conditions. The entire population is more likely to be effected.'
			cat_color = 'hazardous'



		return render(request, 'home.html', 
			{'api' : api, 
			'cat_desription': cat_desription, 
			'cat_color' : cat_color,})

def about(request):
	import json
	import requests

	api_request = requests.get('http://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=37890&distance=5&API_KEY=5D6254D7-9600-491A-861A-3A8E8F41647F')
	try:
		api = json.loads(api_request.content)

	except Exception as e:
		api = 'error'
	return render(request, 'about.html', {'api' : api})