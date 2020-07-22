from random import randint
import sharedvariable
import os
import stopomxthread

def generateResponse(t):
	templist=[]
	for a in sharedvariable.errorResponses:
		if(a[1]==t):
			templist.append(a[0])
	if(len(templist)>0):
		random=randint(0,len(templist)-1)
		sharedvariable.stopFlag=True
		obj=stopomxthread.omxCheck()
		obj.start()
		sharedvariable.omxOn=True
		os.system('omxplayer -o hdmi '+templist[random] )
		sharedvariable.stopFlag=False
		sharedvariable.omxOn=False
