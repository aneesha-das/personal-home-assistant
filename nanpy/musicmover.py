import sharedvariable
import os
import texttospeech
import mysql.connector
from mysql.connector import errorcode
import time

def move():
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
		path=sharedvariable.currentSongPath
		genre=""
		songName=""
		query = ("update buffer set valid=0 where 1;")
		cursor.execute(query)
		cnx.commit()
		cursor.close()
		texttospeech.convert("Under which category do you want me to put this song? Available categories are "+str(sharedvariable.songGenres))
		#print("Under which category do you want me to put this song? Available categories are "+str(sharedvariable.songGenres))
		emptyBufferFlag=True
		while(emptyBufferFlag):
			query = ("select * from buffer;")
			cnx = mysql.connector.connect(user='project', password='rasproot', host='127.0.0.1',database='phpmyadmin')
			cursor=cnx.cursor()
			cursor.execute(query)
			for(v,buff,t) in cursor:
				if(v==1):
					if(buff.lower() in sharedvariable.songGenres):
						genre=buff.lower()
						emptyBufferFlag=False
					elif(buff.lower()=="cancel operation"):
						query = ("update buffer set valid=0 where 1;")
						cnx = mysql.connector.connect(user='project', password='rasproot', host='127.0.0.1',database='phpmyadmin')
						cursor = cnx.cursor()
						cursor.execute(query)
						cnx.commit()
						cursor.close()
						return
					else:
						texttospeech.convert("Please choose a genre from the available choices")
			time.sleep(1)
			cursor.close()
		query = ("update buffer set valid=0 where 1;")
		cnx = mysql.connector.connect(user='project', password='rasproot', host='127.0.0.1',database='phpmyadmin')
		cursor = cnx.cursor()
		cursor.execute(query)
		cnx.commit()
		cursor.close()
		texttospeech.convert("What do you want to name this song?")
		emptyBufferFlag=True
		while(emptyBufferFlag):
			cnx = mysql.connector.connect(user='project', password='rasproot', host='127.0.0.1',database='phpmyadmin')
			cursor=cnx.cursor()
			query = ("select * from buffer;")
			cursor.execute(query)
			for(v,buff,t) in cursor:
				if(v==1 and buff.lower()=="cancel operation"):
					query = ("update buffer set valid=0 where 1;")
					cnx1 = mysql.connector.connect(user='project', password='rasproot', host='127.0.0.1',database='phpmyadmin')
					cursor1 = cnx1.cursor()
					cursor1.execute(query)
					cnx1.commit()
					cursor1.close()
					return
				elif(v==1):
					if(buff.lower() in sharedvariable.songName):
						query = ("update buffer set valid=0 where 1;")
						cnx1 = mysql.connector.connect(user='project', password='rasproot', host='127.0.0.1',database='phpmyadmin')
						cursor1 = cnx1.cursor()
						cursor1.execute(query)
						cnx1.commit()
						cursor1.close()
						texttospeech.convert("This song already exists in your playlist. Please choose another name for this song to save it.")
					else:
						emptyBufferFlag=False
						songName=buff.lower()
			time.sleep(1)
			cursor.close()
		try:
			destination="/home/pi/Desktop/nanpy/Final/songs/"+songName+".mp3"
			os.system('cp "'+path+'" ~/Desktop/nanpy/Final/songs/"'+songName+'".mp3')
			query = ("insert into songs values(\'"+songName+"\',\'"+destination+"\',\'"+genre+"\');")
			cnx = mysql.connector.connect(user='project', password='rasproot', host='127.0.0.1',database='phpmyadmin')
			cursor = cnx.cursor()
			cursor.execute(query)
			cnx.commit()
			cursor.close()
			texttospeech.convert("Song was added successfully")
			sharedvariable.songName.append(songName)
			sharedvariable.songPath.append(destination)
			sharedvariable.songType.append(genre)
		except:
			texttospeech.convert("I am sorry to say that this file cannot be copied")	
		query = ("update buffer set valid=0 where 1;")
		cnx = mysql.connector.connect(user='project', password='rasproot', host='127.0.0.1',database='phpmyadmin')
		cursor = cnx.cursor()
		cursor.execute(query)
		cnx.commit()
		cursor.close()





	
	
	



