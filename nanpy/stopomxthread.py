import os
from threading import Thread
import time
import mysql.connector
from mysql.connector import errorcode
import sharedvariable
import musicmover
import removesong

class omxCheck(Thread):
	def __init__(self):
		Thread.__init__(self)
	def run(self):
		while(sharedvariable.stopFlag):
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
				time.sleep(0.5)
				query = ("select * from buffer;")
				cursor.execute(query)
				for(v,buff,t) in cursor:
					if(v==1 and buff.lower() in sharedvariable.stop):
						print('Stop thread')
						os.system('killall omxplayer.bin')
						sharedvariable.songFlag=True
						sharedvariable.omxOn=False
					elif(v==1 and buff.lower()=="next"):
						os.system('killall omxplayer.bin')
						sharedvariable.omxOn=False
					elif(v==1 and "remove this song" in buff.lower() and sharedvariable.usbFlag!=True):
						os.system('killall omxplayer.bin')
						sharedvariable.songFlag=True
						sharedvariable.omxOn=False
						removesong.remove("this song")
					elif(v==1 and sharedvariable.usbFlag==True and "add this song" in buff.lower()):
						os.system('killall omxplayer.bin')
						sharedvariable.songFlag=True
						sharedvariable.omxOn=False
						sharedvariable.doNotInterrupt=True
						musicmover.move()
						sharedvariable.doNotInterrupt=False
				cursor.close()
				if(sharedvariable.doNotInterrupt==False):
					query = ("update buffer set valid=0 where 1;")
					cursor = cnx.cursor()
					cursor.execute(query)
					cnx.commit()
					cursor.close()
					cnx.close()
		
