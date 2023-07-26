#!/usr/bin/env python3
# Script that creates a password
# By Alex Lee 07/25/23

import random
import secrets
import string

#ask for the rules
passlen = input("How many characters long should the password be?\n")
passlen = int(passlen)
lower = input("Should lowercase letters be allowed? y/n\n")
upper = input("Should upper case letters? y/n\n")
numbers = input("Numbers? y/n\n")
symbols = input("Symbols like !@#? y/n\n")
unicode = input("Unicode characters, like altcode? y/n\n")
similar = input("Exclude similar characters like iIlL etc? y/n\n")
ambiguous = input("Ambiguous characters like []{\}? y/n\n")
first = input("Force the first character to be a letter? y/n\n")
multi = input("How many passwords to generate? 1-10\n")
multi = int(multi)

# define the alphabet
if lower.casefold() == "y":
    lower = string.ascii_lowercase
else:
    lower = ""
if upper.casefold() == "y":
    upper = string.ascii_uppercase
else:
    upper = ""
if numbers.casefold() == "y":
    numbers = string.digits
else:
    numbers = ""
if symbols.casefold() == "y":
    symbols = string.punctuation
else:
    symbols = ""
if unicode.casefold() == "y":
    unicode = input("Please input the unicode characters you would like to include below:\n")
else:
    unicode = ""
if similar.casefold() == "y":
    similar = "iIlL1!|oO0"
else:
    similar = ""
if ambiguous.casefold() == "y":
    ambiguous = r"[]{}()/\\`\"'~;:<>,"
else:
    ambiguous = ""

characters = lower + upper + numbers + symbols + unicode

#remove excess characters
for i in similar:
    characters = string.replace(i, '')
for i in ambiguous:
    characters = string.replace(i, '')

password = []
#generate based on alphabet
for x in multi:
    temp = random.sample(characters, passlen)
    password[x] = "".join(secrets.choice(characters) for i in range passlen)


# color code the result
# this code is beyond me. I think I would have to use a for loop to go through each character of the password, then embed the print color with each character. the resulting print would be horrendous to look at.




# print the result
for position, result in enumerate(password):
    for position, character in password:
        if character.ascii == True:
            print(password[position])
