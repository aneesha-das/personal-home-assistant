import urllib.request
import json
import codecs
import texttospeech
def parseClimate(string):
	weatherList=['weather','climate','temperature','pressure','humidity','location','maximum teperature','minimum temperature']
	for a in weatherList:
		if a in string.lower():
			return a
	else:
		return '-1'
def parseString(string):
	try:
		index=string.rindex(" of ")
	except:
		try:
			index=string.rindex(" at ")
		except:
			try:
				index=string.rindex(" in ")
			except:
				return "-1"
	return string[index+4:len(string)]
def convertKelvinToCelsius(temp):
	return temp-273
def searchWeather(string):
	city=parseString(string)
	climate_type=parseClimate(string)
	if(climate_type=='-1'):
		print("Unable to process")
		return
	if(city=="-1" or city==""):
		print("Unable to process")
	else:
		url = "http://api.openweathermap.org/data/2.5/weather?q="+city.lower()+"&appid=ea0ec5cb289d3dd55e6593a4491c3930"
		reader = codecs.getreader("utf-8")
		response = urllib.request.urlopen(url)
		data = json.load(reader(response))
		city1=data['name']
		if(city.lower()==city1.lower()):
			if(climate_type=='weather' or climate_type=='climate'):
				t=round(convertKelvinToCelsius(data['main']['temp']),2)
				texttospeech.convert('The Temperature of '+city1+' is '+str(t)+' degree C.')
				texttospeech.convert('Humidity is '+str(data['main']['humidity'])+'%.')
				texttospeech.convert('Pressure is '+str(data['main']['pressure'])+' milli bar.')
				texttospeech.convert('Range of Temperature '+str(round(convertKelvinToCelsius(data['main']['temp_min']),2))+' degree C to '+str(round(convertKelvinToCelsius(data['main']['temp_max']),2))+'degree C.')
				texttospeech.convert('Weather condition '+data['weather'][0]['description'])
			else:
				if(climate_type=="temperature"):
					texttospeech.convert("The "+climate_type+" of "+city1+" is "+str(round(convertKelvinToCelsius(data['main']['temp']),2))+" degree C")
				elif(climate_type=="maximum temperature"):
					texttospeech.convert("The "+climate_type+" of "+city1+" is "+str(round(convertKelvinToCelsius(data['main']['temp_max']),2))+" degree C")
				elif(climate_type=="minimum temperature"):
					texttospeech.convert("The "+climate_type+" of "+city1+" is "+str(round(convertKelvinToCelsius(data['main']['temp_min']),2))+" degree C")
				elif(climate_type=="humidity"):
					texttospeech.convert("The "+climate_type+" of "+city1+" is "+str(data['main']['humidity'])+"%")
				elif(climate_type=="pressure"):
					texttospeech.convert("The "+climate_type+" of "+city1+" is "+str(data['main']['pressure'])+" milli bar")
				elif(climate_type=="location"):
					texttospeech.convert("The "+climate_type+" of "+city1+" is "+str(data['coord']))
		else:	
			print("City doesn't exist")



