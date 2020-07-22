import mysql.connector
from mysql.connector import errorcode
import sys
import insertmaxmatch

keyword=insertmaxmatch.formKeywords(sys.argv[1])
newid=sys.argv[2]
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
	query = ("insert into keywords (qid,keyword) values ("+str(newid)+",\'"+keyword+"\');")	
	cursor.execute(query)
	cnx.commit()
	cursor.close()
	cnx.close()
	

