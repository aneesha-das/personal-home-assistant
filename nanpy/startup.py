import os
import aarti
import texttospeech
try:
	aarti.start()
except Exception as e:
	texttospeech.convert("Something went wrong. Rebooting System.")
	os.system("sudo reboot")
