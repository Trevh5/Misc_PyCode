#!/bin/python

import os
import sys
import time

#################################################################################
# This program was written to search downloaded HTML files for certain terms    #
# and then rank the sites based on the number of hits.							#
#################################################################################

absolutely_unused_variable = os.system("cls")
CURSOR_UP_ONE = '\x1b[1A'
ERASE_LINE = '\x1b[2K'

inputDir = '\\Users\\Trevor\\Desktop\\attorneyWebsites\\'
searchTerms = ["Personal Injury", "Personal injury", "personal injury", "Workers Compensation","workers compensation","Workers compensation"]

csvFileString = "Name, Number of Hits, Adjusted Hits \n"

highestNumHits = 0
lowestNumHits = 1000
totalNumPeople = 0
totalNumHits = 0
oldPercentage = 1000

print ('---------------------------------------------------')
print ('---------------------------------------------------')
print("-- \t\t Please wait.. \t" + str(0) + " % \t\t --",)
print ('---------------------------------------------------')
print ('---------------------------------------------------')
sys.stdout.flush()
numDirectories = len(os.listdir(inputDir))
for folderName in os.listdir(inputDir):
	if ".ini" not in folderName:
		totalNumPeople = totalNumPeople + 1
		numWebsites = 0
		numSearchTermHits = 0

		for websiteFile in os.listdir(inputDir + folderName):
			if ".txt" in websiteFile:
				fileString = ""
				if os.stat(inputDir + folderName + "\\" + websiteFile).st_size > 0:
					f = open(inputDir + folderName + "\\" + websiteFile, encoding='latin-1')
					fileString = f.read()
					f.close()
				numWebsites = numWebsites + 1
				for term in searchTerms:
					numSearchTermHits = numSearchTermHits + int(fileString.count(term))
					totalNumHits = totalNumHits + int(fileString.count(term))

		if numSearchTermHits > highestNumHits:
			highestNumHits = numSearchTermHits
		if numSearchTermHits < lowestNumHits:
			lowestNumHits = numSearchTermHits

		if numWebsites > 0:
			adjustedHits = numSearchTermHits/numWebsites
		else:
			adjustedHits = numSearchTermHits

		csvFileString = csvFileString + folderName.replace(" Attorney","").replace(" Utah","").replace(" -","").replace(" Bing","").replace(" Law","") + "," + str(numSearchTermHits) + "," + str(adjustedHits) + "\n"

		percentDone = 100 * (totalNumPeople/numDirectories)

		if round(percentDone) != oldPercentage:
			oldPercentage = round(percentDone)
			absolutely_unused_variable = os.system("cls")
			print ('---------------------------------------------------')
			print ('---------------------------------------------------')
			print ("-- \t\t Please wait.. \t" + str(round(percentDone)) + " % \t\t --",)
			print ('---------------------------------------------------')
			print ('---------------------------------------------------')
			sys.stdout.flush()


averageNumHits = totalNumHits/totalNumPeople

file = open("\\Users\\Trevor\\Desktop\\SearchResults.csv", "w")
file.write(csvFileString)
file.close()

print("")
print("")
print("--  --  --  --  --  --  --  --  --  --  --  --  --  --")
print("Results:")
print("\t Total number of Lawyers: " + str(totalNumPeople))
print("\t Highest number of Hits: " + str(highestNumHits))
print("\t Lowest number of Hits: " + str(lowestNumHits))
print("\t Average hits per lawyer: " + str(averageNumHits))
print("--  --  --  --  --  --  --  --  --  --  --  --  --  --")

print("DONE!")
