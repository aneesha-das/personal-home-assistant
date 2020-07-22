import mysql.connector
from mysql.connector import errorcode
import sharedvariable

def load():

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
		query=("select sessiontable.useremail, users.gmail, users.gmailpassword from sessiontable inner join users on sessiontable.useremail=users.emailid")
		cursor.execute(query)
		i=0
		for(u,g,p) in cursor:
			sharedvariable.currentUser=u
			sharedvariable.currentUserGmail=g
			sharedvariable.currentUserGmailPassword=p
			i=i+1
		if(i==0):
			sharedvariable.currentUser=""
			sharedvariable.currentUserGmail=""
			sharedvariable.currentUserGmailPassword=""
