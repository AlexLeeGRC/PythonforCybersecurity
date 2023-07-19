#!/usr/bin/env python3
# Sample script that reads from a file
# By Alex 07/18/23

import os
dir_path = os.path.dirname(os.path.realpath(__file__))

#open file
f = open(dir_path + "/hackme.txt", "r")

#read file
print("Here is someone to hack- information: ")
for line in f.readlines():
    tdata = line.rstrip()
    print(tdata)

#close file
f.close()