#!/usr/bin/env python3
# Script that scans web server logs for 404 errors
# By Alex Lee 07/25/23

import os

#open log file
dir_path = os.path.dirname(os.path.realpath(__file__))
log_file = input("What file to scan?\n")

f = open(dir_path + "/" log_file, "r")

#read through the file
while True:
    line = f.readline()
    if not line:
        break
    if "404" in line:
        print(line.strip())

f.close()