import mysql.connector
from mysql.connector import errorcode
import datetime
import texttospeech
import sharedvariable
from datetime import timedelta
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
	elif(string.lower()=="today"):
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
		


def addToDoList(string):
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
		try:
			if(lst[len(lst)-1]=='today' ):
				rightIndex=string.rindex('today')-1
			elif(lst[len(lst)-1]=='tomorrow'):
				rightIndex=string.rindex('tomorrow')-1
			else:
				rightIndex=string.rindex(" on")
				rightIndexValue=string[rightIndex+4:len(string)]
		except Exception as e:
			print("7")
			randomresponse.generateResponse('todolistfail')	
			return
		i=len(lst)-1
		date=dayFinder(lst[len(lst)-1])
		if(str(date)=="-1"):
			print(str(rightIndexValue))
			date=dateFinder(str(rightIndexValue))
			if(date=="-1"):
				print("2")
				randomresponse.generateResponse('todolistfail')
				return

		try:
			todo=string[22:rightIndex]
		except Exception as e:
			print("5")
			#print("right index value: "+str(rightIndexValue))
			randomresponse.generateResponse('todolistfail')
			return
		#t=datetime.strptime(time,"%H:%M")
		try:
			if(datetime.datetime.strptime(str(date),"%Y-%m-%d").date()<datetime.datetime.now().date()):
				texttospeech.convert("The mentioned date as already passed.")	
				return
			query = ("insert into todolist (todo,date,useremail) values(\'"+str(todo)+"\',\'"+str(date)+"\',\'"+sharedvariable.currentUser+"\');")
			cursor.execute(query)
			cnx.commit()
			ackString="Job was added to the TO-DO list"
			texttospeech.convert(ackString)
			print("date: "+str(date)+"\n todo: "+todo)
		except Exception as e:
			print("6"+str(e))
			randomresponse.generateResponse('todolistfail')
		cursor.close()
	cnx.close()

def searchList(string):
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
		date=dayFinder(lst[len(lst)-1])
		if(date=="-1"):
			rightIndex=string.rindex(" of ")
			rightIndexValue=string[rightIndex+4:len(string)]
			date=dateFinder(rightIndexValue)
			if(date=="-1"):
				print("8")
				randomresponse.generateResponse('todolistfail')
				cursor.close()
				cnx.close()
				return
		query="select * from todolist where date=\'"+str(date)+"\' and useremail=\'"+sharedvariable.currentUser+"\';"
		cursor.execute(query)
		i=1
		toDoFlag=True
		for(t,d,u) in cursor:
			texttospeech.convert("Number "+str(i)+","+t)
			i=i+1
			toDoFlag=False
		if(toDoFlag):
			texttospeech.convert("You have not added anything to your list yet for "+str(date))
#string=input("Add To TO-DO-LIST: ")
#addToDoList(string)

