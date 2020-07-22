import smtplib
import mysql.connector
from mysql.connector import errorcode
import sys
from random import randint


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
	gmail_user='projectrasppi@gmail.com'
	gmail_password='projectrasppi123'
	sent_from=gmail_user
	email_list=[]
	email_list.append(str(sys.argv[1]))
	randomNumber=randint(1000,9999)
	message="Your otp is: "+str(randomNumber)+". It will expire within 10 minutes."
	email_text = """\  
		From: %s  
		To: %s  
		%s
		""" % (sent_from, ", ".join(email_list), message)
	try:
		server=smtplib.SMTP_SSL("smtp.gmail.com",465)
		server.ehlo()
		server.login(gmail_user, gmail_password)
		server.sendmail(sent_from, email_list, email_text)
		server.close()
		query=("update users set otp=\'"+str(randomNumber)+"\',otptime=SYSDATE() where emailid=\'"+str(sys.argv[1])+"\'")
		cursor.execute(query)
		cnx.commit()
		cursor.close()
		cnx.close()
		print("sent")
	except Exception as e:
		print("error"+str(e))
	
