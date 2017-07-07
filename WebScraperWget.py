#!/bin/python
# This is a simple example of how to use wget from a python script.

import os

count = 0
wget = r'\Users\Trevor\Desktop\wget-1.19.1-win64\wget'
commands = ' --user-agent=Mozilla -e robots=off -r -l 1'
while(count < 60000):
	url = ' https://services.utahbar.org/Member-Directory/Profile/customercd/' + str(count)
	output = ' -O \\Users\\Trevor\\Desktop\\from_utahbar\\' + str(count) + ".txt"
	os.system(wget + commands + url + output)
	count = count + 1
