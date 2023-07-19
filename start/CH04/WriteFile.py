#!/usr/bin/env python3
# Sample script that writes to a file
# By Alex 07/18/23

import os
dir_path = os.path.dirname(os.path.realpath(__file__))

#open file
f = open(dir_path + "/hackme.txt", "w")

#write to file
tname = input("Hello, what is your name?\n")
tcolor = input("Hello, " + tname + "! What is your favorite color?\n")
tpet = input("Great choice! What was the name of your first pet?\n")
tmm = input("So cute! What was your mother's maiden name?\n")
tes = input("Thanks for that! What was the name of your elementary school?\n")

f.write(tname + "\n")
f.write(tcolor + "\n")
f.write(tpet + "\n")
f.write(tmm + "\n")
f.write(tes + "\n")

print("All set!")

#close file
f.close()