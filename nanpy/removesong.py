import sharedvariable
import os
import texttospeech
import mysql.connector
from mysql.connector import errorcode
import time

def remove(string):
	maximum=0
	song_index=0
	if("this song" in string.lower()):
		song=sharedvariable.currentSongName
		path=sharedvariable.currentSongPath
		song_index=sharedvariable.songName.index(song)
	else:

		for a in sharedvariable.songName:
			if(a in string.lower()):
				if(maximum<len(a)):
					maximum=len(a)
					song_index=sharedvariable.songName.index(a)
		if(maximum==0):
			texttospeech.convert("No such song exists")
			return
		song=sharedvariable.songName[song_index]
		path=sharedvariable.songPath[song_index]	
	os.system("rm '"+path+"'")
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
		query=("delete from songs where name=\'"+song+"\';")
		cursor.execute(query)
		cnx.commit()
		cursor.close()
		sharedvariable.songName.remove(song)
		sharedvariable.songPath.remove(path)
		sharedvariable.songType.remove(sharedvariable.songType[song_index])
		texttospeech.convert("The song has been deleted")
			


