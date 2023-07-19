#!/usr/bin/env python3
# Script that encrypts/decrypts text using cryptography module
# By Alex 07/18/23

#message for encryption
source = input("What is your message?\n")
#change to lower case for simplicity
source = source.lower()
final = ""

#loop through each letter in message
for letter in source:
    #convert letter to number
    ascii = ord(letter)
    #check if letter is between a-z
    if ascii >= 97 and ascii <= 122:
        #add 13 to number
        ascii += 13
        #check if still a letter, if not, subtract 26
        if ascii > 122:
            ascii -= 26
    final = final + chr(ascii)

#print encrypted message
print(final)