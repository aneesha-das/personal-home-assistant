import smtplib
import mysql.connector
from mysql.connector import errorcode
import sharedvariable
import texttospeech
import time

def check():
	#print("hello"+sharedvariable.currentUserGmail)	
	if(sharedvariable.currentUserGmail==""):
		return False
	else:
		return True

def send():
	matchcount=0#check the number of matches in the contacts
	if(check()):
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
			gmail_user=sharedvariable.currentUserGmail
			gmail_password=sharedvariable.currentUserGmailPassword
			sent_from=gmail_user
			email_list=[]
			name_list=[]
			texttospeech.convert("To whom should i send this email?")
			flag=True
			sendstring=""
			while(flag):
				try:
					cnx = mysql.connector.connect(user='project', password='rasproot', host='127.0.0.1',database='phpmyadmin')
					cursor = cnx.cursor()
				except:
					texttospeech.convert("Sorry i can't process your request at this moment")
					return
				else:	
					query=("select * from buffer")
					cursor.execute(query)
					for(v,s,t) in cursor:
						if(v==1):
							sendstring=s
							flag=False
				if("leave it" in sendstring.lower()):
					texttospeech.convert("Cancelling Email")
					return
				time.sleep(2)		
			cursor.close()	
			try:
				cnx = mysql.connector.connect(user='project', password='rasproot', host='127.0.0.1',database='phpmyadmin')
				cursor = cnx.cursor()
			except:
				texttospeech.convert("Sorry i can't process your request at this moment")
				return
			else:	
				query=("select * from contacts where useremail=\'"+sharedvariable.currentUser+"\';")
				cursor.execute(query)
				for(u,e,n) in cursor:
					if(n.lower() in sendstring.lower().split()):
						matchcount=matchcount+1
						name_list.append(n.lower())
						email_list.append(e)
				cursor.close()
			if(matchcount!=len(sendstring.lower().split())):
				texttospeech.convert("No matching contacts were found. Please add your contacts before sending an email.")
				return
			flag=True
			message=""
			texttospeech.convert("What is your message?")
			while(flag):
				try:
					cnx = mysql.connector.connect(user='project', password='rasproot', host='127.0.0.1',database='phpmyadmin')
					cursor = cnx.cursor()
				except:
					texttospeech.convert("Sorry i can't process your request at this moment")
					return
				else:	
					query=("select * from buffer")
					cursor.execute(query)
					for(v,s,t) in cursor:
						if(v==1):
							message=s
							flag=False
					cursor.close()
				if("leave it" in sendstring.lower()):
					texttospeech.convert("Cancelling Email")
					return
				time.sleep(2)			
			#subject="OMG SUPER IMPORTANT MESSAGE".
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
				texttospeech.convert('Your email has been sent successfully!')
			except Exception as e:
				texttospeech.convert("Something went wrong. I couldn't send your email."+str(e))
	else:
		texttospeech.convert('Please configure your Gmail account')
