import texttospeech
import mysql.connector
from mysql.connector import errorcode
import sharedvariable

def nickname(string):
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
		index=string.rindex(" me ")
		nickname=string[index+4:len(string)]
		query=("update users set nickname=\'"+nickname+"\' where emailid=\'"+sharedvariable.currentUser+"\';")
		cursor.execute(query)
		cnx.commit()
		cursor.close()
		cnx.close()
		texttospeech.convert("OK, "+nickname+". I will keep that in mind.")
def getNickname():
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
		query=("select nickname from users where emailid=\'"+sharedvariable.currentUser+"\';")
		cursor.execute(query)
		nickname=""		
		for(n) in cursor:
			nickname=n
		cursor.close()
		cnx.close()		
		return str(nickname[0])
