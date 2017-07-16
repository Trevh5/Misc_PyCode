#!/bin/python
# This web scraper was used to download a list of websites that were retrieved from a search engine
import os

inputDir = '\\Users\\Trevor\\Desktop\\webparsed\\'
outputDir = '\\Users\\Trevor\\Desktop\\--\\'

wget = r'\Users\Trevor\Desktop\wget-1.19.1-win64\wget'
commands = ' --user-agent=Mozilla -e robots=off -q '

for filename in os.listdir(inputDir):
	print("--------------------------------------------------------")
	print(filename)
	os.mkdir(outputDir+ filename.rpartition('.')[0])
	count = 1
	lines = []
	with open(inputDir + filename) as file:
		for line in file:
			print("Accessing Website: " + line)
			url = line
			print(' -O \"\\Users\\Trevor\\Desktop\\--\\' + filename.rpartition('.')[0] + str(count) + ".txt\"")
			output = ' -O \"' + outputDir + filename.rpartition('.')[0] + "\\" + str(count) + ".txt\" "
			print(wget + commands + output + url)
			os.system(wget + commands + output + url)
			count=count+1
	print("--------------------------------------------------------")

print("DONE!")
