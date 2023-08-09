#!/user/bin/env python3
# Script that checks a generated password against haveibeenpwned API
#By Alex Lee 08/08/23

# import modules
import requests
import json
import secrets
import crypt
import hashlib
import string

# create password
def passgenr():
    letters = string.ascii_letters
    digits = string.digits
    special_chars = string.punctuation
    alphabet = letters + digits + special_chars
    pwd_length = input("How long should the password be? (6-30)")
    pwd_length = int(pwd_length)
    pwd = ''
    for i in range(pwd_length):
        pwd += ''.join(secrets.choice(alphabet))
    return pwd


prompt = input("Do you want to: \n 1: Check a password\n 2: Create a password and check it \n")
if prompt == "1":
    passgen = input("What password would you like to check?\n")
elif prompt == "2":
    passgen = passgenr()
else:
    print("Invalid input!")



# hash password
encPass = passgen.encode()
pass_hash = hashlib.sha1(encPass).hexdigest()

# split hash for api call
hash5 = pass_hash[0:5]
sans5 = pass_hash[5:].upper()

# print(pass_hash, "\n", hash5, "\n", sans5)

# check generated passord against hibp API
def hibp_passcheck(hash5):
    url = "https://api.pwnedpasswords.com/range/" + hash5
    pwnd_dict = {}
    response = requests.get(url)
    pwnd_list = response.text.split("\r\n")
    for pwnd_pass in pwnd_list:
        temp_pass = pwnd_pass.split(":")
        pwnd_dict[temp_pass[0]] = temp_pass[1]
    return pwnd_dict

pwnd_dict = hibp_passcheck(hash5)

#check results
if sans5 in pwnd_dict.keys():
    print("Password has been compromsed {0} times.".format(pwnd_dict[sans5]))
else:
    print("Password", passgen, "is secure!")