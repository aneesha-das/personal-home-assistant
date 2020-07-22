import texttospeech
import randomresponse
import gender

def processExpression(e):
	i=0
	lst=e.split(' ')
	string=''
	while(i<len(lst)):
		#CODE FOR INSERTING * IN PLACE OF ´MULTIPLIED BY´
		if(lst[i].lower()=='multiplied' or lst[i].lower()=='x' or lst[i].lower()=='into'):
			if(lst[i+1].lower()=='by'):
				string=string+' * '
				i=i+1
			else:
				string=string+' * '
		#CODE FOR INSERTING / IN PLACE OF ´DIVIED BY´
		elif(lst[i].lower()=='divided'):
			if(lst[i+1].lower()=='by'):
				string=string+' / '
				i=i+1
			else:
				string=string+' / '
		#CODE FOR INSERTING / IN PLACE OF ´BY´
		elif(lst[i].lower()=='by'):
			string=string+' / '
		#CODE FOR INSERTING - IN PLACE OF ´MINUS´
		elif(lst[i].lower()=='minus'):
			string=string+' - '
		elif(lst[i].lower()=='plus'):
			string=string+' + '
		#CODE FOR INSERTING / IN PLACE OF ´÷´
		elif(lst[i].lower()=='by' or lst[i]=='÷'):
			string=string+' / '
		#CODE FOR APPENDING THE REMAINING EXPRESSION IN STRING VARIABLE
		else:
			string=string+' '+lst[i]	
			#print('PROCESS '+string)

		i=i+1
	return string

def parseExpression(ex):
	lst=ex.split(' ')
	print('Expression '+ex)
	lstLength=len(lst)
	numList=[]
	
	i=0
	while(i<len(lst)):
		if(lst[i].lower()=='minus'):
			lst[i]='-'
		i=i+1
	i=0
	#print('Before While '+ str(lst))
	while(i<len(lst)):
		if(lst[i].isnumeric()):
			numList.append(lst[i])
		elif(lst[i]=='-'):
	#		print('This is num list '+str(numList))
			try:
				if(lst[i+1].isnumeric()):
					numList.append('-'+lst[i+1])
					i=i+1
					#print(str(numList))
			except Exception as e:
					pass
		i=i+1
	expression=''
#ADDITION CODE(IF ADDITION IS SPECIFIED)
	if(lst[0].lower() == 'add' or lst[0].lower() == 'addition'):
		for n in numList:
			expression=expression+n+ ' + '
		expression=expression[0:len(expression)-3]
#SUBTRACTION CODE(IF SUBTRACTION IS SPECIFIED)
	elif(lst[0].lower() == 'subtraction' or lst[0].lower() == 'subtract'):
		if(lst[2].lower()=='from'):
			expression=numList[1]+' - '+numList[0]
		else:
			for n in numList:
				expression=expression+n+ ' - '
			expression=expression[0:len(expression)-3]
#MULTIPLICATION CODE(IF MULTIPLY IS SPECIFIED)
	elif(lst[0].lower() == 'multiplication' or lst[0].lower() == 'multiply'):
		for n in numList:
			expression=expression+n+ ' * '
		expression=expression[0:len(expression)-3]
#DIVISION CODE(IF DIVISION IS SPECIFIED)
	elif(lst[0].lower() == 'division' or lst[0].lower() == 'divide'):
		for n in numList:
			expression=expression+n+ ' / '
		expression=expression[0:len(expression)-3]
#PROCESSING EXPRESSION(IF CALCULATE IS SPECIFIED)
	elif(lst[0].lower()=='calculate'):
		expression=processExpression(ex[10:len(ex)])
	#	print('CALCULATE '+expression)
	else:
		expression=processExpression(ex)
	#	print('EXP ELSE '+expression)
	return expression

def calculate(expression):
	parsedExpression=parseExpression(expression)
	try:
		print('Parsed Expression '+parsedExpression)
		result=eval(parsedExpression)
		texttospeech.convert('The value of the expression is '+str(result)+", "+str(gender.gender()))
	except Exception as e:
		print(str(e))
		randomresponse.generateResponse('calculatorfail')
