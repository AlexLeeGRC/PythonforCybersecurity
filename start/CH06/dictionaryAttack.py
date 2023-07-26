#!/usr/bin/env python3
# Script that performs a dictionary attack against known password hashes
# Needs a dictionary file, suggested to use https://github.com/danielmiessler/SecLists/tree/master/Passwords/Common-Credentials
# By Alex Lee 07/25/23

import crypt
import os

# create function to test passwords
def test_password(algorithm_salt, hashed_password, password_guess):
    #use salt to hash guess
    hashed_guess = crypt.crypt(password_guess, algorithm_salt)
    
    #compare salted guess against hashed password
    if hashed_guess == hashed_password:
        return True
    return False

# load dictionary file
dir_path = os.path.dirname(os.path.realpath(__file__))

#open dictionary file
dictionary = input("Which dictionary to load? 100/1000/1M\n")
if dictionary == "100":
    f = open(dir_path + "/10-million-top-100.txt", "r")
    passwords = f.readlines()
    f.close()
elif dictionary == "1000":
    f = open(dir_path + "/10-million-top-1000.txt", "r")
    passwords = f.readlines()
    f.close()
else:
    f = open(dir_path + "/10-million.txt", "r")
    passwords = f.readlines()
    f.close()

# open the shadow file
shadow = open(dir_path + "/shadow", "r")
shadow_string = shadow.readlines()
shadow.close()

unhashed = open(dir_path + "/unhashed.txt", "w")

#create empty lists for username and salted hash results
username = []
salted_hash = []
salt = []
hashed_password = []

for x in range(len(shadow_string)):
    line_parts = shadow_string[x].split(':')
    if line_parts[1].startswith("$6$"):
        dollarsplit = line_parts[1].split('$')
        username.append(line_parts[0])
        salted_hash.append(line_parts[1])
        salt.append("$6$" + dollarsplit[2])
        hashed_password.append(dollarsplit[3])


# prompt user for algo and salt
#algorithm_salt = input("What is the algorithm and salt?\n")

# prompt for salted hash
#hashed_password = input("What is the full hashed password?\n")

# loop through the username/hash combos to feed into passwords
for position, userhash in enumerate(username):
# loop through dictionary attack
    for password in passwords:
        password = password.strip()
        result = test_password(salt[position], salted_hash[position], password)
        if result:
            print("Match found: ", userhash, "{0}".format(password))
            unhashed.write(userhash + " " + password + "\n")
            break
        #else:
        #    print(userhash, "does not match", password)

unhashed.close()