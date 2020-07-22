import onlinesearch
import weathersearch
import calculator
import event
import playsong
import todolist
import texttospeech
import mysql.connector
from mysql.connector import errorcode
from random import randint
import sharedvariable
import matchcalculator
import calender
import playsongfromusbdrive
import removesong
import sendmail
import nickname
import takepicture
import savepicture
import reloadcredentials
import credentialsloader
import poweroff
import randomresponse
import surveillance
import name
import changedate
import insertmaxmatch
import gender
import eventchecker
import nickname

def parse(buff):
	answer=False
	buff=buff.lower()
	if(buff.split(" ")[0].isnumeric()):
		calculator.calculate(buff)
	else:
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
			print("1")
			query = ("select * from questions where question=\'"+buff+"\';")
			cursor.execute(query)
			count=len(cursor.fetchall())
			if(count>0):
				print("2")
				query = ("select * from questions where question=\'"+buff+"\';")
				cursor.execute(query)
				for(qid,question) in cursor:
					print("3")
					query=("select qid,qrmap.rid,response from qrmap inner join responses on qrmap.rid=responses.rid where qid="+str(qid)+";")
					cursor.execute(query)
					count=len(cursor.fetchall())
					random=randint(1,count)
					query=("select qid,qrmap.rid,response from qrmap inner join responses on qrmap.rid=responses.rid where qid="+str(qid)+";")
					cursor.execute(query)
					i=1
					for(q,r,res) in cursor:
						print("7")
						if(random==i):
							print("8")
							answer=True
							if("tell me a joke" in buff):	
								texttospeech.convert(res)
							else:
								address=randint(0,2)
								if (address==0):
									texttospeech.convert(res)	
								elif (address==1):
									texttospeech.convert(res+" "+gender.gender())	
								elif (address==2):
									texttospeech.convert(res+" "+nickname.getNickname())	
						i=i+1
			else:
				#First check whether functuin exists or not
				l=buff.split(" ")
				customString=""
				query="select * from function_keywords where keyword like "
				i=0
				while(i<len(l)):
					customString=customString+" "+l[i]
					query=query+"\'%"+l[i]+"%\' or keyword like "
					i=i+1
				query=query[0:len(query)-17]
				query=query+" order by length desc;"
				print(query)
				query=(query)
				cursor.execute(query)
				i=0
				query2=""
				buff1=""
				for(kid,keyword,length,fid) in cursor:
					if(i==0):
						if(keyword in buff):
							i=1
							query2=("select * from function_table where id="+str(fid)+";")
							buff1=buff[buff.index(keyword):len(buff)]
				if(i==1):
					cursor.execute(query2)
					for(i,m,f,a) in cursor:
						if(str(a)=="0"):
							getattr(eval(m),f)()
							answer=True
						else:
							getattr(eval(m),f)(buff1)
							answer=True
				else:	
					#Now check for possible responses	
					l=buff.split(" ")
					i=0
					customString=""
					query="select * from keywords where keyword like "
					while(i<len(l)):
						if(l[i] not in sharedvariable.commonWords):
							customString=customString+l[i]+" "
							query=query+"\'%"+l[i]+"%\' or keyword like "
						i=i+1
					if(len(customString)>0):
						customString=customString[0:len(customString)-1]
					query=query[0:len(query)-17]
					query=query+";"
					print(query)
					query=(query)
					print("f")
					cursor.execute(query)
					print("g")
					returnKeyword=[]
					returnQid=[]
					percentageList=[]
					try:
						for(kid,qid,keyword) in cursor:
							print("a")
							returnKeyword.append(keyword)
							returnQid.append(qid)
							percentageList.append(matchcalculator.calculate(customString,keyword))
						maximum=max(percentageList)
						index=percentageList.index(maximum)
						if(matchcalculator.checkThreshold(customString,returnKeyword[index],percentageList[index])):
							print("b")							
							query=("select temp.response from keywords inner join (select qid,response from qrmap inner join responses on qrmap.rid=responses.rid ) temp on keywords.qid=temp.qid where keywords.qid="+str(returnQid[index])+";")
							cursor.execute(query)
							count=len(cursor.fetchall())
							random=randint(1,count)
							query=("select temp.response from keywords inner join (select qid,response from qrmap inner join responses on qrmap.rid=responses.rid ) temp on keywords.qid=temp.qid where keywords.qid="+str(returnQid[index])+";")
							print("hochche1")
							insertmaxmatch.insertmaxmatch(buff,returnQid[index])
							cursor.execute(query)
							print("c")
							i=0
							#print("Random number: "+str(random))
							for(r) in cursor:
								print("d")
								if(i==random):
									answer=True
									print ("res:"+str(r[0]))
									texttospeech.convert(str(r[0]))
								i=i+1
							print("e")
					except Exception as e:
						print("I do not understand your question "+ str(e))
						return
					cursor.close();
					if(answer==False):
						cursor=cnx.cursor();
						randomresponse.generateResponse('apology')
						query=("insert into unanswered values(\'"+buff+"\')")
						cursor.execute(query)
						cnx.commit()
			cursor.close()
