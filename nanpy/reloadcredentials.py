import mysql.connector
from mysql.connector import errorcode
import sharedvariable

def check():
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
		query = ("select * from sessiontable;")
		cursor.execute(query)
		i=0
		flag=True
		for(u,a) in cursor:
			if(str(u)==sharedvariable.currentUser ):
				flag=False
			else:
				flag=True
			i=i+1
		if(i==0):
			return True
		elif(i==1 and flag==True):
			return True
		elif(i==1 and flag==False):
			return False
		
