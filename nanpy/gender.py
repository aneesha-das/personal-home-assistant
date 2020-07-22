import mysql.connector
from mysql.connector import errorcode
import sharedvariable

def gender():
		gender=""
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
			query = ("select gender from users where emailid=\'"+sharedvariable.currentUser+"\';")
			cursor.execute(query)
			for(g) in cursor:
				if(g[0].lower()=="male"):
					gender="sir"
				else:
					gender="mam"
			cursor.close()
			cnx.close()
			return gender
