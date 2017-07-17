#!/bin/python

import os

count = 23536
wget = r'\Users\Trevor\Desktop\wget-1.19.1-win64\wget'
commands = ' --user-agent=Mozilla -e robots=off -r -l 1'
while(count < 60000):
	url = ' https://www.google.com/search?q=' + str(count)
	output = ' -O \\Users\\Trevor\\Desktop\\from_utahbar3\\test.txt' + str(count) + ".txt"
	os.system(wget + commands + url + output)
	count = count + 1


os.system(r'\Users\Trevor\Desktop\wget-1.19.1-win64\wget --user-agent=Mozilla --limit-rate=20k -e robots=off -r -l 1 https://services.utahbar.org/Member-Directory/Profile/customercd/9196 -O \Users\Trevor\Desktop\9196.txt')

os.system(wget + commands + url + output)


wget = r'\Users\Trevor\Desktop\wget-1.18-win64\wget'
commands = ' --user-agent=Mozilla -e robots=off -r -l 1'
url = ' https://services.utahbar.org/Member-Directory/Profile/customercd/' + str(count)
output = ' -O \\Users\\Trevor\\Desktop\\from_utahbar\\' + str(count) + ".txt"
os.system(wget + commands + url + output)


commands = ' --user-agent=Mozilla --limit-rate=20k -e robots=off -r -l 1'
