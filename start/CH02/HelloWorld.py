#!/usr/bin/env python3
# A simple "Hello World" script in python
# Created by Alex on July 11, 2023

#Get name
username = input("What is your name? ")

print("Hello " + username)
#print("Hello {0}".format(username))

age = input("How old are you today? ")
age = int(age)
print(username, ", you will be ", age+2, " in two years.")