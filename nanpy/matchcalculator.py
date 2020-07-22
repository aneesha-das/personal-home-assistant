
def calculate(buff,databaseValue):
	l1=buff.split(" ")
	l2=databaseValue.split(" ")
	percentage=0
	if(len(l1)<=len(l2)):
		i=0
		for a in l1:
			if(a in l2):
				i=i+1
		percentage=i/float(len(l2))*100
	else:
		i=0
		for a in l2:
			if(a in l1):
				i=i+1
		percentage=i/float(len(l1))*100
	return percentage

def checkThreshold(customString,returnKeyword,percentage):
	print(str(percentage))
	print(customString)
	print(returnKeyword)
	l1=customString.split(" ")
	l2=returnKeyword.split(" ")
	if(len(l1)>len(l2)):
		maxValue=len(l1)
		minValue=len(l2)
	else:
		maxValue=len(l2)
		minValue=len(l1)
	ratio=minValue/float(maxValue)
	print(str(ratio))
	if(ratio<0.4):
		return False
	value=ratio*100
	x=abs(value-percentage)
	print(str(x))
	if(x<=25):
		return True
	else:
		return False
