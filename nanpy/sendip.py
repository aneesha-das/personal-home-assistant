import os
import smtplib
ip_addr=os.popen("hostname -I|cut -d \' \' -f1").read()
gmail_user='projectrasppi@gmail.com'
gmail_password='projectrasppi123'
sent_from=gmail_user
email_list=['projectrasppi@gmail.com','das.aneesha.ad@gmail.com','parkouramit@gmail.com','asitroy193@gmail.com']
message="\nThe ip address of raspberry pi is: "+ip_addr+"The username is:pi\nThe password is:raspberry"
email_text = """\  
		From: %s  
		To: %s  
		%s
		""" % (sent_from, ", ".join(email_list), message)
try:
		server=smtplib.SMTP_SSL("smtp.gmail.com",465)
		server.ehlo()
		server.login(gmail_user, gmail_password)
		server.sendmail(sent_from, email_list, email_text)
		server.close()
		os.system('omxplayer -o hdmi /home/pi/Desktop/nanpy/Final/startuptune.mp3')

except Exception as e:
		print("error"+str(e))


