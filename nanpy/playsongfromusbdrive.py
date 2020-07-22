import sharedvariable
import os
import texttospeech
import stopomxthread
import time
import randomresponse

def playSong():
	os.system('sudo sh checkusb')
	try:
		musicList=open('musiclist','r')
		drivePath=open('drivepath','r')
		music_list=musicList.read().split('\n')
		drive_path=drivePath.read()
		drive_path=drive_path[0:len(drive_path)-1]
		musicList.close()
		drivePath.close()
		if(len(drive_path)==0 or len(music_list)<=0):
			texttospeech.convert("No music file found")
			return
	except:
		print("Exception")
		return
	sharedvariable.stopFlag=True
	obj=stopomxthread.omxCheck()
	obj.start()
	sharedvariable.songFlag=False
	for a in music_list:
		song=drive_path+'/'+a
		while(sharedvariable.omxOn):
			time.sleep(1)
		sharedvariable.omxOn=True
		sharedvariable.usbFlag=True
		sharedvariable.currentSongPath=song
		os.system('omxplayer -o hdmi '+"'"+song+ "'")
		sharedvariable.omxOn=False
		sharedvariable.usbFlag=False
		time.sleep(.5)
		if(sharedvariable.songFlag):
			break
	sharedvariable.stopFlag=False
