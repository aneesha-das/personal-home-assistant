import os

def changedate(string):
	string=string[12:len(string)]
	os.system("sudo date --set \'"+string+"\'")
	print("done")
