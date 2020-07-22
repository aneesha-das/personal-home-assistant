import mysql.connector
from mysql.connector import errorcode
import time
import parsequery
import sharedvariable
import texttospeech
import eventchecker
import credentialsloader
import reloadcredentials
import eventchecker


def start():
	obj=sharedvariable.loadSharedVariables()
	obj.start()
	obj.join()
	var=1
	texttospeech.convert("Hello! I am ready to talk.")
	while var==1:
		if(reloadcredentials.check()):
			credentialsloader.load();
			eventchecker.checkEvent()
			if(eventchecker.event):
				sharedvariable.eventCheckerObject=eventchecker.eventCheck()
				sharedvariable.eventCheckerObject.start()
		if(sharedvariable.doNotInterrupt==False):
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
				query = ("select * from buffer;")
				cursor.execute(query)
				for(v,buff,t) in cursor:
					if(v==1):
						print("Valid Value= "+str(v))
						print("Buffer Value= "+buff)
						print("Time Value is "+str(t))
						parsequery.parse(buff)
					else:
						print("talk to me")
				cursor.close()
				query = ("update buffer set valid=0 where 1;")
				cursor = cnx.cursor()
				cursor.execute(query)
				cnx.commit()
				cursor.close()
				cnx.close()
		time.sleep(2)
