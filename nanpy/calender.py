import datetime
from datetime import timedelta
import texttospeech
def find_date(string):
	now=datetime.datetime.now()
	dayArray=["monday","tuesday","wednesday","thursday","friday","saturday","sunday"]
	if("today" in string.lower()):
		texttospeech.convert("Today is "+str(now.date()))
	elif("tomorrow" in string.lower()):
		texttospeech.convert("Tomorrow is "+str((now+timedelta(1)).date()))
	else:
		for a in dayArray:
			if(a in string.lower()):
				weekday=now.weekday()
				i=0
				while(weekday != dayArray.index(a)):
					weekday=(weekday+1) % 7
					i=i+1
				texttospeech.convert("The day is on "+str((now+timedelta(i)).date()))
				break
def get_time():
	texttospeech.convert(datetime.datetime.now().strftime("%H:%M"))
def build_date(string):
	try:
		string=string[string.rindex("is")+3:len(string)]
	except Exception as e:
		texttospeech.convert("I am unable to understand your query")
		return "0"
	monthArray=["january","february","march","april","may","june","july","august","september","october","november","december"]
	shortMonArray=["jan","feb","mar","apr","may","jun","jul","aug","sept","oct","nov","dec"]
	year=datetime.datetime.now().year
	month=datetime.datetime.now().month
	l=string.split(" ")
	if(l[0]=="today"):
		return str(datetime.datetime.now().date())
	if(l[0]=="tomorrow"):
		return str((datetime.datetime.now()+timedelta(1)).date())
	#print("l[0]=="+l[0])
	#print("l[1]=="+l[1])
	if(l[0][0].isnumeric() and l[0][1].isnumeric()):
		day=l[0][0]+l[0][1]
	elif(l[0][0].isnumeric()):
		day="0"+l[0][0]
	else:
		print("2.1")
		return "-1"
	if(len(l)==1):
		return str(year)+"-"+str(month)+"-"+day
	elif(len(l)>=2):
		if(len(l)==3):
			if(l[2].isnumeric()):
				year=l[2]
			else:
				print("2.2")
				return "-1"
		if(l[1].isnumeric()):
			return str(year)+"-"+l[1]+"-"+day
		else:
			i=0
			while(i<len(monthArray)):
				if(l[1].lower()==monthArray[i] or l[1].lower()==shortMonArray[i]):
					if(i<10):
						month="0"+str(i+1)
					else:
						month=str(i+1)
					return str(year)+"-"+month+"-"+day
				i=i+1
def get_day(string):
	dayArray=["monday","tuesday","wednesday","thursday","friday","saturday","sunday"]
	date=build_date(string)
	if(date!="-1" and date!="0"):
		try:
			req_date=datetime.datetime.strptime(date,"%Y-%m-%d")
			#print(date+" is on "+str(dayArray[req_date.weekday()]))
			texttospeech.convert(date+" is on "+str(dayArray[req_date.weekday()]))
		except Exception as e:
			texttospeech.convert("Please enter a proper date")
	elif(date=="-1"  and date!="0"):
		texttospeech.convert("Please enter a proper date")
#string=input("Enter query:")
#get_day(string)
				
