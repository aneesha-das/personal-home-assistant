import picamera
import time
import nickname
import texttospeech
import mysql.connector
from mysql.connector import errorcode

def takepicture():
	camera=None;
	try:
		camera=picamera.PiCamera()
		texttospeech.convert("Camera is ready. Are you ready to pose "+nickname.getNickname()+"?")
		flag=True
		while(flag):
				try:
					cnx = mysql.connector.connect(user='project', password='rasproot', host='127.0.0.1',database='phpmyadmin')
					cursor = cnx.cursor()
				except:
					pass
					return
				else:	
					query=("select * from buffer")
					cursor.execute(query)
					for(v,s,t) in cursor:
						print("1");
						if(v==1 and ('ready' in s.lower() or 'yes' in s.lower())):
							flag=False
						elif(v==1 and 'leave it' in s.lower()):
							camera.close()
							camera=None
							return
				time.sleep(2)		
				cursor.close()	
		texttospeech.convert("Say cheese in 3, 2, 1, 0")
		time.sleep(2)
		tempPath="/var/www/html/pictures/temp.jpg"
		camera.capture(tempPath)
		try:
			cnx = mysql.connector.connect(user='project', password='rasproot', host='127.0.0.1',database='phpmyadmin')
			cursor = cnx.cursor()
		except:
			camera.close()
			pass
		else:	
			query=("delete from temppicture where 1;")
			cursor.execute(query)
			cnx.commit()
			cursor.close()
			camera.close()
			texttospeech.convert("Your picture has been taken "+nickname.getNickname()+". Please preview it in the website.")
			camera=None
			try:
				cnx = mysql.connector.connect(user='project', password='rasproot', host='127.0.0.1',database='phpmyadmin')
				cursor = cnx.cursor()
			except:
				camera.close()
				pass
			else:	
				query=("insert into temppicture values(1,\'"+tempPath+"\');")
				cursor.execute(query)
				cnx.commit()
				cursor.close()
	except Exception as e:
		if(camera!=None):
			camera.close()
		texttospeech.convert("Camera not ready yet.Please try after some time."+str(e))

