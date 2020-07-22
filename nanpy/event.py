import time
import mysql.connector
from mysql.connector import errorcode
import datetime
import texttospeech
import sharedvariable
from datetime import timedelta
import eventchecker
import randomresponse

def dayFinder(string):
	dayArray=["monday","tuesday","wednesday","thursday","friday","saturday","sunday"]
	if(string.lower() in dayArray):
		for s in dayArray:
			if(s==string.lower()):
				day=dayArray.index(s)
				break
		i=0
		a=datetime.datetime.today().weekday()
		while(a != day):
			a=(a+1) % 7
			i=i+1
		return (datetime.datetime.now()+timedelta(i)).date()
	elif(string.lower()=="today" or string.lower()=="p.m" or string .lower()=="a.m" or string.lower()=="p.m." or string .lower()=="a.m."):
		return datetime.datetime.now().date()
	elif(string.lower()=="tomorrow"):
		return (datetime.datetime.now()+timedelta(1)).date()
	else:
		return "-1"

def dateFinder(string):
	monthArray=["january","february","march","april","may","june","july","august","september","october","november","december"]
	shortMonArray=["jan","feb","mar","apr","may","jun","jul","aug","sept","oct","nov","dec"]
	year=datetime.datetime.now().year
	month=datetime.datetime.now().month
	l=string.split(" ")
	print(string)
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
		

def parseTime(t,m):
	if(m.lower()=="p.m." or m.lower()=="p.m"):
		l=t.split(":")
		try:
			if(int(l[0])<=12):
				if(int(l[0])==12):
					t=l[0]
				else:
					l[0]=int(l[0])+12
					t=l[0]
				if(len(l)>1):
					if(int(l[1])<=59):
						t=str(t)+":"+str(l[1])
					else:
						return "-1"
				else:
					t=str(t)+":"+"00"
				return t
			else:
				return "-1"
		except Exception as e:
			return "-1"
	elif(m.lower()=="a.m." or m.lower()=="a.m"):
		l=t.split(":")
		try:
			if(int(l[0])<=12):
				if(int(l[0])==12):
					l[0]=0
					t=l[0]
				else:
					t=l[0]
				if(len(l)>1):
					if(int(l[1])<=59):
						t=str(t)+":"+str(l[1])
					else:
						return "-1"
				else:
					t=str(t)+":"+"00"
				return t
			else:
				return "-1"
		except Exception as e:
			return "-1"
	else:		
		return "-1"
def addEvent(string):
	try:
		cnx = mysql.connector.connect(user='project', password='rasproot', host='127.0.0.1',database='phpmyadmin')
		cursor = cnx.cursor()
	except mysql.connector.Error as err:
		if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
			print("Something is wrong with your user name or password")
		elif err.errno == errorcode.ER_BAD_DB_ERROR:
			print("Database does not exist")
		else:
			print(err)
	else:
		print("Connected")
		print()
		lst=string.split(" ")
		i=len(lst)-1
		atFlag=False
		timeIndex=0
		date=dayFinder(lst[len(lst)-1])
		if(str(date)=="-1"):
			try:
				rightIndexValue=string[string.rindex("on")+3:len(string)]
			except Exception as e:
				print("1")
				randomresponse.generateResponse('eventfail')	
				return
			date=dateFinder(rightIndexValue)
			if(date=="-1"):
				print("2")
				randomresponse.generateResponse('eventfail')	
				return
		while(i>0):
			try:
				if(lst[i].lower()=="at" and not atFlag):
					atFlag=True
					time=parseTime(lst[i+1],lst[i+2])
					if(time=="-1"):
						ackString="Please provide a valid time"
						texttospeech.convert(ackString)
						return
					print(time)
					timeIndex=i
			except Exception as e:
				print("3")
				randomresponse.generateResponse('eventfail')	
				return
			i=i-1
		try:
			length=0
			for a in sharedvariable.event:
				if(a in string.lower() and string.index(a)==0):
					length=len(a.split(" "))
					break
			if(length>0):
				i=length
				event=""
				while(i<timeIndex):
					event=event+" "+lst[i]
					i=i+1
			else:
				print("4")
				randomresponse.generateResponse('apology')	
				return
		except Exception as e:
			print("5")
			randomresponse.generateResponse('eventfail')	
			return
		#t=datetime.strptime(time,"%H:%M")
		try:
			if(datetime.datetime.strptime(str(date),"%Y-%m-%d").date()<datetime.datetime.now().date()):
				texttospeech.convert("The mentioned date as already passed.")	
				return
			else:
				if(datetime.datetime.strptime(time,"%H:%M").time()<datetime.datetime.now().time()):
					texttospeech.convert("The mentioned time as already passed.")	
					return
			query = ("insert into events (event,time,date,useremail) values(\'"+str(event)+"\',\'"+str(time)+"\',\'"+str(date)+"\',\'"+sharedvariable.currentUser+"\');")
			cursor.execute(query)
			cnx.commit()
			ackString="Event was added to the reminder list"
			eventchecker.checkEvent()
			if(not (sharedvariable.eventCheckerObject is None)):
				eventchecker.eventCondition.acquire()
				eventchecker.eventCondition.notify()
				eventchecker.eventCondition.release()
			else:
				sharedvariable.eventCheckerObject=eventchecker.eventCheck()
				sharedvariable.eventCheckerObject.start()
			print("date: "+str(date)+"\n time: "+str(time)+"\n event: "+event)
			texttospeech.convert(ackString)
		except Exception as e:
			print("6"+(str(e)))
			randomresponse.generateResponse('eventfail')	
		cursor.close()
		

#string=input("Enter your event: ")
#addEvent(string)

