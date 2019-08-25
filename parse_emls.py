#!/bin/python3

import os
import re

# Create a list to store results of parsing emails
scanlist = []

# Loop through all .eml files in directory and store the interesting lines into scanlist
for file in os.listdir("/path/to/your/emails/"):
    if file.endswith(".eml"):
        f = open(file)
        scanlist.append(re.findall(r"Time   : .*|Memo   : .*|Source IP: .*|User-agent: .*", f.read()))

# Create an output file
o = open("/path/to/your/output.csv", "w")

# Write headers to output file (CSV)
o.write("Time" + "," + "Memo" + "," + "Source IP" + "," + "User-Agent" + "\n")

# Loop through scanlist and drop values into CSV format
for list in scanlist:
    for element in list:
        if re.findall("Time   : .*", element):
            o.write(re.findall("Time   : (.*)", element)[0] + ",")
        elif re.findall("Memo   : .*", element):
            o.write(re.findall("Memo   : (.*)", element)[0] + ",")
        elif re.findall("Source IP: .*", element):
            o.write(re.findall("Source IP: (.*)", element)[0] + ",")
        else:
            o.write(re.findall("User-agent: (.*)", element)[0] + "\n")
