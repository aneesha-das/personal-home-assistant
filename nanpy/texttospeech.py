from gtts import gTTS 
import os
import sharedvariable
import stopomxthread
import mysql.connector
from mysql.connector import errorcode

def responseUpdate(res):
	res1="";
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
		query = ("delete from responsebuffer where 1;")
		cursor.execute(query)
		cnx.commit()
		cursor.close()
		cnx.close()
		y=res.split("'",len(res))
		if(len(y)>1):
			for i in y:
				res1=res1+i
			res=res1
		print(res1)
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
		query = ("insert into responsebuffer values(1,\'"+res+"\',SYSDATE());")
		cursor.execute(query)
		cnx.commit()
		cursor.close()
		cnx.close()
	pass

def convert(string):
	tts=gTTS(text=string, lang='en')
	tts.save('response.mp3')
	print(string)
	responseUpdate(string)
	sharedvariable.stopFlag=True
	obj=stopomxthread.omxCheck()
	obj.start()
	sharedvariable.omxOn=True
	os.system('omxplayer -o hdmi /home/pi/Desktop/nanpy/Final/response.mp3')
	sharedvariable.stopFlag=False
	sharedvariable.omxOn=False
