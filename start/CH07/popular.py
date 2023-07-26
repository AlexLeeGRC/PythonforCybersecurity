#!/usr/bin/env python3
# Script that scans web server logs for most popular pages and reports the results
# By Alex Lee 07/25/23

import os
import re

#open log file
dir_path = os.path.dirname(os.path.realpath(__file__))
f = open(dir_path + "/access.log", "r")
log_lines = f.readlines()
f.close()

#scan for resources being accessed and count
# get count

#regex pattern
regex_pattern = r"(?:GET)\s(.*?)\s(?:HTTP)"
result_dictionary = {}

for line in log_lines:
    #search for pattern, print and store if found
    m = re.search(regex_pattern, line)
    #print(m)
    if m:
        resource = m.group()
        resource = resource.split(' ')
        resource = resource[1]
        if resource in result_dictionary.keys():
            result_dictionary[resource] += 1
        else:
            result_dictionary[resource] = 1

#create report
pop = open(dir_path + "/popular.txt", "w")

# sort by most common result
for w in sorted(result_dictionary, key=result_dictionary.get, reverse=True):
    text = w + str(result_dictionary[w])
    pop.write(text)
