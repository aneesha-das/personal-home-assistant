from random import randint
import texttospeech
def name(string):
	l1=string.split(" ")
	if(l1[3] in ['mr','mrs','miss'] and len(l1)>4):
		greet(l1[4])
	else:
		greet(l1[3])
def greet(string):
	greets=['Hello', 'Namaste', 'Hi', 'Nice to meet you']
	randomNumber=randint(0,3)
	texttospeech.convert(greets[randomNumber]+" "+string)	
