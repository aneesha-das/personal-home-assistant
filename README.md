# ARTI, Your personal digital assistant

Arti is a home assistant designed for helping people with day to day tasks. Her brain has been uploaded in this repository to preserve her legacy. Arti runs on Raspberry pi along with Arduino UNO to perform autonomous activities. Some of its features include live surveillance, event reminders, music player and email sender. There is a large number of other features available too.

## Overview

This github code relies heavily on the hardware of ARTI. The following diagram gives a brief overview of ARTI's hardware needs.

![Hardware Design](/doc_images/hardware.JPG)

## Purpose of each component:

- **Raspberry Pi3 Model B(1):** This is the heart our project. Voice commands will be sent from mobile browser to the server running in raspberry pi which will process the commands and respond accordingly. The configuration of raspberry pi(quad core 1.2GHz CPU, 1GB RAM) helps in high speed processing of the commands given to it. Also, the wifi interface helps us to connect our mobile to the raspberry pi and send commands through a local network. Since we have loaded the OS Raspbian into the raspberry pi it exempts us from the tedious task of entering our code in machine language format. The OS is loaded into a 32GB memory card. The available USB ports helps us to connect external devices like pen drives when desired in our project. 

- **Arduino Uno(1):** The Arduino Uno acts as the slave of Raspberry Pi. Pi and Uno performs the commands in master-slave relationship. Pi sends commands to Uno which in turn forwards the commands to the motor controllers. This is mainly done so that too much load is not exerted on the Pi. If the Arduino Uno chip is damaged only the locomotion function of the robot will become inactive but if the Pi gets damaged then the entire system will get damaged which is certainly not desired. So the intermediary Arduino Uno acts as a safety zone for raspberry pi. Moreover the pins of raspberry pi are digital whereas the motor controller takes analog input. Arduino acts as an interface between the two converting the digital signal to analog.

- **L293D Motor Controller(2):** The motor controllers are supplied with external power source(12V) thus it does not put much load either on the Pi or the Arduino Uno. Motor controller also helps to control the speed of the motors. Two motor controllers are used, one for the left pair and other for the right.

- **10000maH power bank(1):** This is a 5V power supply used to supply power to the raspberry pi as well as the speakers. It has two outlets. The 2.1amp current flows into the raspberry pi and 1amp current flows into the speakers.

- **12V power supply(1):** It is used to supply power to the motor controllers.

- **200rpm motors(4):** Used for moving the robot

- **Pi Camera(1):** Pi Camera connected to raspberry pi fulfills the purpose of clicking pictures of the user and live surveillance

- **Speakers(1):** Voice outputs are given through the speakers

## Flowcharts

**Chatbot**

The personal digital assistant has chatting facilities. When the user gives a voice input through his mobile browser for example “How are you?” or “What are you doing?” etc it will give an appropriate reply. The conversation between the user and the robot will be very natural and human-like. Thus the user can build a friendship with the robot by chatting. The robot will try to understand the users language as much as she can and will try to give as much accurate reply as possible. In case she doesn’t know the reply to a particular command, she will try to learn and use it for the next time. This is how machine learning is applied.

![Chatbot](/doc_images/chatbot.png)

**Event Reminder**

The user can set event on a particular day at a particular time. The personal assistant will remind him of that particular event at that very moment. It must be noted that since the digital assistant has the facility of multiple user accounts, it will notify the user about the event only when he is logged in to his account. Event will be set only when the user inputs a valid date and time.

![Event Reminder](/doc_images/event_reminder.png)

**Live Surveillance**

When the user enters into the live surveillance panel of the website he can see the live video frames rendered by the surveillance process. When we exit the page the Pi camera will automatically be disabled within 10 seconds.

![Live Surveillance](/doc_images/live_surveillance.png)

There are a lot of other features as well which are: 
<br>
<br>***Send Mail***<br>
To send mail the user first has to configure his Gmail account. Once he has done this he will have to add contacts to his contact list. Now, when he gives the command to send mail, the robot asks to whom it should be sent. On giving a correct recipient list the robot then asks for the content of the message. When the user provides it the mail is sent to the desired receivers from the user’s Gmail account.	
<br>***Calculator***<br>
Users can easily ask ARTI to evaluate any arithmetic expression and ARTI will do it for them in the blink of an eye.
<br>***Google Search***<br>
ARTI also has the capability to search the web for answers of particular questions. It can search google and resolve any queries that the user might have.
<br>***To-Do List***<br>
We humans tend to forget a lot of things. The easiest solution to this problem is to create a to-do list which keeps track of all our work. In the old days we needed to manually write the tasks in a diary or mobile, but now ARTI can do it for you. Just say the word, and ARTI will keep track of all your upcoming tasks for the day.
<br>***Locomotion***<br>
A robot is simply not fun enough if it remains stationary. ARTI has wheels which help her move around the house easily. The main advantage of this feature is the surveillence part. Multiple cameras are not needed to monitor every room of the house. ARTI can act as a remote controlled security guard which moves around the house and sends surveillance data to the user's mobile phone.
<br>***Nickname***<br>
Obviously any virtual assistant should have a feature to set the nickname of its owner. ARTI is no exception. The user just needs to ask ARTI to save a nickname and she remembers it.
<br>***Play Music***<br>
Everyone loves music. ARTI does too. The user can ask ARTI to play any song that is already inbuilt in her memory, or plug in a USB drive with his/her custom playlist. ARTI can easily change, play, pause or shuffle music based on user's reqirement. ARTI keeps track of the songs by categorizing them based on the user's mood.
<br>***Take A Picture***<br>
Who loves a great picture? But often someone is left behind the lens to capture the perfect photograph. ARTI solves this problem by taking the cameraman's place, so that everyone can share one happy frame. The user can position ARTI by looking at the mobile screen which contains a preview of the photo to be taken. When the user is ready, ARTI takes the picture. Don't forget to smile when ARTI asks you to say CHEEESEEE.....
