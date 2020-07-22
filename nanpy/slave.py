from nanpy import (ArduinoApi, SerialManager)
from time import sleep
import mysql.connector
from mysql.connector import errorcode

m1pin1=2
m1pin2=3
m2pin1=4
m2pin2=5
m1enable=6
m3pin1=7
m3pin2=8
m2enable=9
m3enable=10
m4enable=11
m4pin1=12
m4pin2=13

def updateMovement():
	try:
		cnx1 = mysql.connector.connect(user='project', password='rasproot', host='127.0.0.1',database='phpmyadmin')
		cursor1 = cnx1.cursor()
	except mysql.connector.Error as err:
		if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
			print("Something is wrong with your user name or password")
		elif err.errno == errorcode.ER_BAD_DB_ERROR:
			print("Database does not exist")
		else:
			print(err)
	else:	
		query = ("update movebot set direction=\'stop\' where 1;")
		cursor1.execute(query)
		cnx1.commit()
		cursor1.close()
		cnx1.close()

def moveBot(x):
	x=x.lower()
	try:
		connection=SerialManager()
		a=ArduinoApi(connection = connection)
	except:

		print('Failed To Connect')
	a.pinMode(m1pin1,a.OUTPUT)
	a.pinMode(m1pin2,a.OUTPUT)
	a.pinMode(m2pin1,a.OUTPUT)
	a.pinMode(m2pin2,a.OUTPUT)
	a.pinMode(m3pin1,a.OUTPUT)
	a.pinMode(m3pin2,a.OUTPUT)
	a.pinMode(m4pin1,a.OUTPUT)
	a.pinMode(m4pin2,a.OUTPUT)
	a.pinMode(m1enable,a.OUTPUT)
	a.pinMode(m2enable,a.OUTPUT)
	a.pinMode(m3enable,a.OUTPUT)
	a.pinMode(m4enable,a.OUTPUT)
	

	try:
		if(x=="left"):
			print("left dhukche");
			a.analogWrite(m1enable,200)
			a.digitalWrite(m1pin1,a.HIGH)
			a.digitalWrite(m1pin2,a.LOW)
			a.analogWrite(m2enable,200)
			a.digitalWrite(m2pin1,a.HIGH)
			a.digitalWrite(m2pin2,a.LOW)
			a.analogWrite(m3enable,200)
			a.digitalWrite(m3pin1,a.HIGH)
			a.digitalWrite(m3pin2,a.LOW)
			a.analogWrite(m4enable,200)
			a.digitalWrite(m4pin1,a.HIGH)
			a.digitalWrite(m4pin2,a.LOW)
			sleep(1)
			updateMovement()
		elif(x=="right"):
			print("right dhukche");
			a.analogWrite(m1enable,255)
			a.digitalWrite(m1pin1,a.HIGH)
			a.digitalWrite(m1pin2,a.LOW)
			a.analogWrite(m2enable,150)
			a.digitalWrite(m2pin1,a.LOW)
			a.digitalWrite(m2pin2,a.HIGH)
			a.analogWrite(m3enable,255)
			a.digitalWrite(m3pin1,a.HIGH)
			a.digitalWrite(m3pin2,a.LOW)
			a.analogWrite(m4enable,150)
			a.digitalWrite(m4pin1,a.LOW)
			a.digitalWrite(m4pin2,a.HIGH)
			sleep(1)
			updateMovement()
		elif(x=="front"):
			print("front dhukche");
			a.analogWrite(m1enable,250)
			a.digitalWrite(m1pin1,a.HIGH)
			a.digitalWrite(m1pin2,a.LOW)
			a.analogWrite(m2enable,100)
			a.digitalWrite(m2pin1,a.HIGH)
			a.digitalWrite(m2pin2,a.LOW)
			a.analogWrite(m3enable,250)
			a.digitalWrite(m3pin1,a.HIGH)
			a.digitalWrite(m3pin2,a.LOW)
			a.analogWrite(m4enable,100)
			a.digitalWrite(m4pin1,a.HIGH)
			a.digitalWrite(m4pin2,a.LOW)
			sleep(1)
			updateMovement()
		elif(x=="back"):
			print("dhukche");
			a.analogWrite(m1enable,200)
			a.digitalWrite(m1pin1,a.LOW)
			a.digitalWrite(m1pin2,a.HIGH)
			a.analogWrite(m2enable,200)
			a.digitalWrite(m2pin1,a.LOW)
			a.digitalWrite(m2pin2,a.HIGH)
			a.analogWrite(m3enable,200)
			a.digitalWrite(m3pin1,a.LOW)
			a.digitalWrite(m3pin2,a.HIGH)
			a.analogWrite(m4enable,200)
			a.digitalWrite(m4pin1,a.LOW)
			a.digitalWrite(m4pin2,a.HIGH)
			sleep(1)
			updateMovement()
		else:
			a.digitalWrite(m1pin1,a.LOW)
			a.digitalWrite(m1pin2,a.LOW)
			a.digitalWrite(m2pin1,a.LOW)
			a.digitalWrite(m2pin2,a.LOW)
			a.digitalWrite(m3pin1,a.LOW)
			a.digitalWrite(m3pin2,a.LOW)
			a.digitalWrite(m4pin1,a.LOW)
			a.digitalWrite(m4pin2,a.LOW)
	except:
		pass


while True:
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
		query = ("select * from movebot;")
		cursor.execute(query)
		for(d) in cursor:
			if(len(d)>0):
				print("calling movebot"+str(d[0]))
				moveBot(str(d[0]))
				#moveBot("front")
			else:
				print("not moving")
		cursor.close()
		cnx.close()
	#sleep(1)
	
