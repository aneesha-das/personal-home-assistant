from threading import Thread
import mysql.connector
from mysql.connector import errorcode

stopFlag=False 	#Flag to verify whether the stop thread will execute or not. False means do not execute the thread
event=[]	#All the upcoming events will be stored here
stop=[]	#All the stop commands will be stored here
songPath=[]	#Array for storing song paths
songName=[]	#Array for storing song names
songFlag=False	#True when we say stop during a song
songType=[]	#The genre of the songs are stored here
omxOn=False	#This flag is used to verify whether the omx player is on or not. False means off
playSongFlag=False#	This flag is used to denote whether play song loop is active or not. False means loop not active
eventCheckerObject=None	#This object reference variable is used to store the event checker thread's reference
errorResponses=[]	#All the predefined responses will be populated in this array
commonWords=["a","an","if","the","it","aarti","on","of","then"]	#This is the common words array which are dropped from the query to be parsed
usbFlag=False	#This flag is used to check if song is being played from the USB Drive or not. False means not playing
currentSongPath=""	#This string stores the path of the current song being played
songGenres=["groovy","sad","romantic","soulful","happy","rap","spiritual"]
doNotInterrupt=False	#This flag is used to stop the main thread to interrupt
currentSongName="" #This variable contains the name of the current song being played
currentUser="" #This variable contains the current user's email ID
currentUserGmailPassword="" #This variable contains the user's gmail password
currentUserGmail="" #this variable stores the gmail id of the current user

class loadSharedVariables(Thread):
	def run(self):
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
			query = ("select * from specialwords where purpose=\'event\';")
			cursor.execute(query)
			for(keyword,purpose) in cursor:
				event.append(keyword)
			cursor.close()
			query = ("select * from specialwords where purpose=\'stop\';")
			cursor = cnx.cursor()
			cursor.execute(query)
			for(keyword,purpose) in cursor:
				stop.append(keyword)
			cursor.close()
			query = ("select * from songs;")
			cursor = cnx.cursor()
			cursor.execute(query)
			for(n,p,t) in cursor:
				songName.append(n.lower())
				songPath.append(p)
				songType.append(t.lower())
			cursor.close()
			query = ("select * from errorresponses;")
			cursor = cnx.cursor()
			cursor.execute(query)
			for(e,t) in cursor:
				templist=[]
				templist.append(e)
				templist.append(t)
				errorResponses.append(templist)
			cnx.close()
