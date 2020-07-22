import mysql.connector
from mysql.connector import errorcode
import sharedvariable
def insertmaxmatch(string, qid):
	newid=""
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
		query = ("insert into questions (question) values (\'"+string+"\');")
		cursor.execute(query)
		cnx.commit()
		newid=cursor.lastrowid
		cursor.close()
		cnx.close()
		rid=[]
		print(qid)
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
			query=("select * from qrmap where qid="+str(qid)+";");
			cursor.execute(query)
			print(qid)
			for(m,q,r) in cursor:
				rid.append(r)
			cursor.close()
			cnx.close()
			print("hochche 1.1")
			for r in rid:
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
					print(newid)
					query = ("insert into qrmap (qid,rid) values ("+str(newid)+","+str(r)+");")
					cursor.execute(query)
					cnx.commit()
					cursor.close()
					cnx.close()
					keyword=formKeywords(string)
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

def formKeywords(string):
	l=string.split(" ")
	customString=""
	i=0
	while(i<len(l)):
		if(l[i] not in sharedvariable.commonWords):
			customString=customString+l[i]+" "
		i=i+1
	if(len(customString)>0):
		customString=customString[0:len(customString)-1]
	return customString
	
