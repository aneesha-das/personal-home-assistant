import time
import mysql.connector
from mysql.connector import errorcode
import datetime
import texttospeech
import sharedvariable
from datetime import timedelta
from threading import Thread,Condition
import os
import stopomxthread

event=[]
eventTime=[]
today=datetime.datetime.now().date()
nearestEvent=0
eventCondition=Condition()
def checkEvent():
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
		try:
			print(str(today))
			query = ("select * from events where date=\'"+str(today)+"\' and useremail=\'"+sharedvariable.currentUser+"\';")
			cursor.execute(query)
			i=0
			while(i<len(event)):
				event.remove(event[i])
				eventTime.remove(eventTime[i])
				i=i+1
			for(eid,e,t,d,u) in cursor:
				if(datetime.datetime.now().strftime('%H:%M')<t):
					event.append(e)
					eventTime.append(t)
			cursor.close()
		except Exception as e:
			print("Exception"+str(e))
			cursor.close()
	cnx.close()

class eventCheck(Thread):
	def __init__(self):
		Thread.__init__(self)
	def run(self):
		if(sharedvariable.currentUser==""):
			return
		print(str(event))
		while(event):
			minimum=min(eventTime)
			index=eventTime.index(minimum)
			timeDifference=datetime.datetime.strptime(minimum+':00','%H:%M:%S')-datetime.datetime.strptime(datetime.datetime.now().strftime('%H:%M:%S'),'%H:%M:%S')
			print(timeDifference)
			pauseTime=1
			if('-1' in str(timeDifference)):
				event.remove(event[index])
				eventTime.remove(eventTime[index])
			elif(str(timeDifference)<='0:00:30'):
				pauseTime=1
			elif(str(timeDifference)<='0:01:00'):
				pauseTime=30
			elif(str(timeDifference)<='0:05:00'):
				pauseTime=60
			elif(str(timeDifference)<='0:10:00'):
				pauseTime=300
			elif(str(timeDifference)<='0:30:00'):
				pauseTime=10*60
			elif(str(timeDifference)<='1:00:00'):
				pauseTime=30*60
			else:
				pauseTime=60*60
			if(str(timeDifference)=='0:00:00'):
				string="You have an event! "+event[index]
				event.remove(event[index])
				eventTime.remove(eventTime[index])
				if(sharedvariable.omxOn):
					os.system('killall omxplayer.bin')
					print(sharedvariable.omxOn)
					sharedvariable.stopFlag=False
					time.sleep(.3)
					sharedvariable.omxOn=True
				texttospeech.convert(string)
				if(sharedvariable.playSongFlag):
					sharedvariable.stopFlag=True
					obj=stopomxthread.omxCheck()
					obj.start()
			eventCondition.acquire()
			eventCondition.wait(pauseTime)
			eventCondition.release()
		sharedvariable.eventCheckerObject=None
