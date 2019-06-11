#!/usr/bin/python3
from googlesearch import search
import time
#import speech_recognition as sr
#r = sr.Recognizer()
#with sr.Microphone() as source:
'''
#take input from user  to  search on web
    print('speak anything:')
    audio=r.listen(source)
try:
    text = r.recognize_google(audio)
    print('you said: {}'.formate(text))
except:
    print('sory ')
    '''
web=input('pls enter topic:')
# search and   store in list form
list1 = []
for i in search(web,stop=10):
	print(i) # i will only print the url
	time.sleep(1)
	list1.append(i)
print(list1)
f = open('url.txt','a+')# store in this file so that later we can find

for i in list1:
	f.write(i+'\n')
f.close()
