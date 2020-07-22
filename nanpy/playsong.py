import sharedvariable
import os
import texttospeech
import stopomxthread
import time
import randomresponse

def playCategory(string):
		i=0
		sharedvariable.stopFlag=True
		obj=stopomxthread.omxCheck()
		obj.start()
		sharedvariable.songFlag=False
		for a in sharedvariable.songPath:
			print(sharedvariable.omxOn)
			while(sharedvariable.omxOn):
				print('Sleeping')
				time.sleep(1)
			if(sharedvariable.songFlag):
				break
			if(sharedvariable.songType[i]==string):
				sharedvariable.omxOn=True
				sharedvariable.currentSongPath=a
				sharedvariable.currentSongName=sharedvariable.songName[i]
				os.system('omxplayer -o hdmi '+"'"+a+ "'")
				sharedvariable.omxOn=False
				time.sleep(.5)
			i=i+1
		sharedvariable.stopFlag=False

def playSong(string):
	sharedvariable.playSongFlag=True
	if("sad song" in string.lower()):
		playCategory("sad")		
	elif("happy song" in string.lower()):
		playCategory("happy")
	elif("rap song" in string.lower()):
		playCategory("rap")
	elif("romantic song" in string.lower()):
		playCategory("romantic")
	elif("soulful song" in string.lower()):
		playCategory("soulful")
	elif("spiritual song" in string.lower()):
		playCategory("spiritual")
	elif("groovy song" in string.lower()):
		playCategory("groovy")
	elif("play music" in string.lower()):
		sharedvariable.stopFlag=True
		obj=stopomxthread.omxCheck()
		obj.start()
		sharedvariable.songFlag=False
		for a in sharedvariable.songPath:
			while(sharedvariable.omxOn):
				time.sleep(1)
			sharedvariable.omxOn=True
			sharedvariable.currentSongPath=a
			sharedvariable.currentSongName=sharedvariable.songName[sharedvariable.songPath.index(a)]
			os.system('omxplayer -o hdmi '+"'"+a+ "'")
			sharedvariable.omxOn=False
			time.sleep(.5)
			if(sharedvariable.songFlag):
				break
		sharedvariable.stopFlag=False
	else:
		i=0
		while(i<len(sharedvariable.songName)):
			if(sharedvariable.songName[i] in string.lower()):
				while(sharedvariable.omxOn):
					time.sleep(1)
				sharedvariable.stopFlag=True
				obj=stopomxthread.omxCheck()
				obj.start()
				sharedvariable.omxOn=True
				sharedvariable.currentSongName=sharedvariable.songName[i]
				sharedvariable.currentSongPath=sharedvariable.songPath[i]
				os.system('omxplayer -o hdmi '+"'"+sharedvariable.songPath[i]+ "'")
				sharedvariable.omxOn=False
				time.sleep(.5)
				sharedvariable.stopFlag=False
				break
			i=i+1
		else:
			randomresponse.generateResponse('playfail')	

	sharedvariable.playSongFlag=False

