#!/bin/python

import os
import sys

inputDir = 'C:\\Users\\Trevor\\Desktop\\webparsed\\'
outputDir = 'C:\\Users\\Trevor\\Desktop\\attorneyWebsites\\'

wget = r'C:\Users\Trevor\Desktop\wget-1.19.1-win64\wget'
commands = ' --user-agent=Mozilla -e robots=off -r -l 1 -q '

oldPercentage = 1000
currentNum = 0
numDirectories = len(os.listdir(inputDir))

absolutely_unused_variable = os.system("cls")
print ('---------------------------------------------------')
print ('---------------------------------------------------')
print("-- \t\t Please wait.. \t" + str(0) + " % \t\t --",)
print ('---------------------------------------------------')
print ('---------------------------------------------------')
print ("\t Current Progresss: " + str(currentNum) + "/" + str(numDirectories))

for filename in os.listdir(inputDir):
	#print("--------------------------------------------------------")
	#print(filename)
	os.mkdir(outputDir+ filename.rpartition('.')[0])
	count = 1
	lines = []
	with open(inputDir + filename) as file:
		for line in file:
			#print("Accessing Website: " + line)
			url = line
			#print(' -O \"\\Users\\Trevor\\Desktop\\attorneyWebsites\\' + filename.rpartition('.')[0] + str(count) + ".txt\"")
			output = ' -O \"' + outputDir + filename.rpartition('.')[0] + "\\" + str(count) + ".txt\" "
			#print(wget + commands + output + url)
			os.system(wget + commands + output + url)
			count=count+1
	currentNum = currentNum + 1
	percentDone = 100 * (currentNum/numDirectories)
	#if round(percentDone) != oldPercentage:
			#oldPercentage = round(percentDone)
	absolutely_unused_variable = os.system("cls")
	print ('---------------------------------------------------')
	print ('---------------------------------------------------')
	print ("-- \t\t Please wait.. \t" + str(round(percentDone)) + " % \t\t --",)
	print ('---------------------------------------------------')
	print ('---------------------------------------------------')
	print ("\t Current Progresss: " + str(currentNum) + "/" + str(numDirectories))
	sys.stdout.flush()
	#print("--------------------------------------------------------")

print("DONE!")
