import mysql.connector
from mysql.connector import errorcode
import sharedvariable
import texttospeech
import os

def savepicture():
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
		count=0
		query = ("select count(*) from pictures;")
		cursor.execute(query)
		for(x) in cursor:
			count=str(x[0]+1)
		cursor.close();
		cnx.close();
		path="/var/www/html/pictures/"+count+".jpg "
		os.system("cp /var/www/html/pictures/temp.jpg "+path)
		try:
			cnx = mysql.connector.connect(user='project', password='rasproot', host='127.0.0.1',database='phpmyadmin')
			cursor = cnx.cursor()
		except mysql.connector.Error as err:
			pass
		else:
			user=sharedvariable.currentUser
			query = ("insert into pictures (username,path) values(\'"+user+"\',\'"+path+"\');")
			cursor.execute(query)
			cnx.commit()
			texttospeech.convert("The picture was saved successfully.");
			cursor.close()
			cnx.close()
			try:
				cnx = mysql.connector.connect(user='project', password='rasproot', host='127.0.0.1',database='phpmyadmin')
				cursor = cnx.cursor()
			except mysql.connector.Error as err:
				pass
			else:
				user=sharedvariable.currentUser
				query = ("delete from temppicture where 1;")
				cursor.execute(query)
				cnx.commit()
				cursor.close()
				cnx.close()
