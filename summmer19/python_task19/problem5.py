#!/usr/bin/python3
import datetime
# input name from user
name=input("enter your name")
#condition for time to send  message according to it
x=datetime.datetime.now()
if x.hour in range(4,12):
        print("good morning",name)
elif x.hour in range(12,17):
        	print("good afternoon",name)
elif x.hour in range(17,21):
	            print("good evening",name)

#else it will send the message good night as none of time peroid is selected
else:
    print("good night")
