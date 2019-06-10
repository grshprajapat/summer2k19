#!/usr/bin/python3
import os
#taking  input if it is in string form then user will create

username = input("Enter username: ")

if username.isalpha():
    password = 'hello' + username
    os.system('sudo adduser -p $(openssl passwd -1 {}) {}'.format(password, username))
    print('User created.')
    #if no string then it will print this mssge
else:
    print('Username must contain only alphabets.')
