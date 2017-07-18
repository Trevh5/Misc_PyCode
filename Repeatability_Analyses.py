#!/bin/python

import os
import csv
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import statistics as s

inputDir = 'D:\\Research\\Bigler\\Repeatability_Paper\\Final_Data\\'
outputDir = 'D:\\Research\\Bigler\\Repeatability_Paper\\figures\\'
fsFileName = 'FS_SelectData.csv'
antsFileName = 'ANTS_SelectData.csv'
csvOutputData_FS = "Label, Average Difference, Standard Deviation, Max Difference, Min Difference, Average Percent Difference \n"
csvOutputData_ANTS = "Label, Average Difference, Standard Deviation, Max Difference, Min Difference, Average Percent Difference \n"

fsData = []
fsFile = csv.reader(open(inputDir+fsFileName))
fsFilePandas = pd.read_csv(inputDir+fsFileName)

antsData = []
antsFile = csv.reader(open(inputDir+antsFileName))
antsFilePandas = pd.read_csv(inputDir+antsFileName)

for row in fsFile:
	fsData.append(row)

for row in antsFile:
	antsData.append(row)

Header_fs = fsData[0]
fsData.pop(0)

Header_ants = antsData[0]
antsData.pop(0)

i = 0
antsSubj1 = []
antsSubj2 = []
antsSubj3 = []
antsSubj4 = []
antsSubj5 = []
antsSubj6 = []
antsSubj7 = []
antsSubj8 = []
antsSubj9 = []
for scanName in antsFilePandas['subj']:
	if "0001" in scanName:
		antsFilePandas.iloc[i,antsFilePandas.columns.get_loc('subj')] = "0001"
	if "0002" in scanName:
		antsFilePandas.iloc[i,antsFilePandas.columns.get_loc('subj')] = "0002"
	if "0003" in scanName:
		antsFilePandas.iloc[i,antsFilePandas.columns.get_loc('subj')] = "0003"
	if "0004" in scanName:
		antsFilePandas.iloc[i,antsFilePandas.columns.get_loc('subj')] = "0004"
	if "0005" in scanName:
		antsFilePandas.iloc[i,antsFilePandas.columns.get_loc('subj')] = "0005"
	if "0006" in scanName:
		antsFilePandas.iloc[i,antsFilePandas.columns.get_loc('subj')] = "0006"
	if "0007" in scanName:
		antsFilePandas.iloc[i,antsFilePandas.columns.get_loc('subj')] = "0007"
	if "0008" in scanName:
		antsFilePandas.iloc[i,antsFilePandas.columns.get_loc('subj')] = "0008"
	if "0009" in scanName:
		antsFilePandas.iloc[i,antsFilePandas.columns.get_loc('subj')] = "0009"
		
	i = i + 1
antsSubj1 = antsFilePandas.loc[antsFilePandas.subj=='0001']
antsSubj2 = antsFilePandas.loc[antsFilePandas.subj=='0002']
antsSubj3 = antsFilePandas.loc[antsFilePandas.subj=='0003']
antsSubj4 = antsFilePandas.loc[antsFilePandas.subj=='0004']
antsSubj5 = antsFilePandas.loc[antsFilePandas.subj=='0005']
antsSubj6 = antsFilePandas.loc[antsFilePandas.subj=='0006']
antsSubj7 = antsFilePandas.loc[antsFilePandas.subj=='0007']
antsSubj8 = antsFilePandas.loc[antsFilePandas.subj=='0008']
antsSubj9 = antsFilePandas.loc[antsFilePandas.subj=='0009']

i = 0
fsSubj1 = []
fsSubj2 = []
fsSubj3 = []
fsSubj4 = []
fsSubj5 = []
fsSubj6 = []
fsSubj7 = []
fsSubj8 = []
fsSubj9 = []
for scanName in fsFilePandas['volume']:
	if "0001" in scanName:
		fsFilePandas.iloc[i,fsFilePandas.columns.get_loc('volume')] = "0001"
	if "0002" in scanName:
		fsFilePandas.iloc[i,fsFilePandas.columns.get_loc('volume')] = "0002"
	if "0003" in scanName:
		fsFilePandas.iloc[i,fsFilePandas.columns.get_loc('volume')] = "0003"
	if "0004" in scanName:
		fsFilePandas.iloc[i,fsFilePandas.columns.get_loc('volume')] = "0004"
	if "0005" in scanName:
		fsFilePandas.iloc[i,fsFilePandas.columns.get_loc('volume')] = "0005"
	if "0006" in scanName:
		fsFilePandas.iloc[i,fsFilePandas.columns.get_loc('volume')] = "0006"
	if "0007" in scanName:
		fsFilePandas.iloc[i,fsFilePandas.columns.get_loc('volume')] = "0007"
	if "0008" in scanName:
		fsFilePandas.iloc[i,fsFilePandas.columns.get_loc('volume')] = "0008"
	if "0009" in scanName:
		fsFilePandas.iloc[i,fsFilePandas.columns.get_loc('volume')] = "0009"
		
	i = i + 1

fsSubj1 = fsFilePandas.loc[fsFilePandas.volume=='0001']
fsSubj2 = fsFilePandas.loc[fsFilePandas.volume=='0002']
fsSubj3 = fsFilePandas.loc[fsFilePandas.volume=='0003']
fsSubj4 = fsFilePandas.loc[fsFilePandas.volume=='0004']
fsSubj5 = fsFilePandas.loc[fsFilePandas.volume=='0005']
fsSubj6 = fsFilePandas.loc[fsFilePandas.volume=='0006']
fsSubj7 = fsFilePandas.loc[fsFilePandas.volume=='0007']
fsSubj8 = fsFilePandas.loc[fsFilePandas.volume=='0008']
fsSubj9 = fsFilePandas.loc[fsFilePandas.volume=='0009']

antsSeparatedData = [antsSubj1,antsSubj2,antsSubj3,antsSubj4,antsSubj5,antsSubj6,antsSubj7,antsSubj8,antsSubj9]
fsSeparatedData = [fsSubj1,fsSubj2,fsSubj3,fsSubj4,fsSubj5,fsSubj6,fsSubj7,fsSubj8,fsSubj9]

fsColumns = ["Left-Amygdala","Right-Amygdala","Amygdala","Left-Hippocampus","Right-Hippocampus","Hippocampus","CorticalWhiteMatterVol","TotalGrayVol"]
antsColumns = ["left_amygdala","right_amygdala","amygdala_total","left_hippocampus","right_hippocampus","hippocampus_total"]
for column in fsColumns:
	difList = []
	perDifList=[]
	print("")
	print("--------------------")
	print(column)
	print("--------------------")
	for fsSub in fsSeparatedData:
		difference = float(fsSub[column].max()) - float(fsSub[column].min())
		percentDifference = 100*(abs(fsSub[column].max() - fsSub[column].min())/fsSub[column].min())
		perDifList.append(percentDifference)
		difList.append(difference)
		print("Difference: " + str(difference))
		print("Mean: " + str(fsSub[column].mean()) + " (" + str(fsSub[column].std()) + ")")
		subjName = fsSub.iloc[0,fsSub.columns.get_loc('volume')]
		subPlot = fsSub.plot(title = "Subject " + subjName +" " + column, x='scan' , y = column,figsize=(8,5))
		subPlot.set_xlabel("Scan Number")
		subPlot.set_ylabel("Volume (mm cubed)")
		plt.savefig(outputDir + "fs\\"+ subjName + column +".png")
		plt.close()
	print("")
	print("Average difference: " + str(s.mean(difList)) + " (" + str(s.stdev(difList)) +")")
	print("Max difference: " + str(max(difList)))
	print("Min difference: " + str(min(difList)))
	print("Average percent difference: " + str(s.mean(perDifList)))
	csvOutputData_FS = csvOutputData_FS + column + "," + str(s.mean(difList)) + "," + str(s.stdev(difList)) + "," + str(max(difList)) + "," + str(min(difList)) + "," + str(s.mean(perDifList)) + "\n"

for column in antsColumns:
	difList = []
	perDifList=[]
	print("")
	print("--------------------")
	print(column)
	print("--------------------")
	for antsSub in antsSeparatedData:
		difference = float(antsSub[column].max()) - float(antsSub[column].min())
		percentDifference = 100*(abs(antsSub[column].max() - antsSub[column].min())/antsSub[column].min())
		perDifList.append(percentDifference)
		difList.append(difference)
		print("Difference: " + str(difference))
		print("Mean: " + str(antsSub[column].mean()) + " (" + str(antsSub[column].std()) + ")")
		subjName = antsSub.iloc[0,antsSub.columns.get_loc('subj')]
		subPlot = antsSub.plot(title = "Subject " + subjName +" " + column, x='scan' , y = column,figsize=(8,5))
		subPlot.set_xlabel("Scan Number")
		subPlot.set_ylabel("Volume (mm cubed)")
		plt.savefig(outputDir + "ants\\" + subjName + column +".png")
		plt.close()
	print("")
	print("Average difference: " + str(s.mean(difList)) + " (" + str(s.stdev(difList)) +")")
	print("Max difference: " + str(max(difList)))
	print("Min difference: " + str(min(difList)))
	print("Average percent difference: " + str(s.mean(perDifList)))
	csvOutputData_ANTS = csvOutputData_ANTS + column + "," + str(s.mean(difList)) + "," + str(s.stdev(difList)) + "," + str(max(difList))+ "," + str(min(difList)) + "," + str(s.mean(perDifList)) + "\n"


file = open(outputDir + "fs_results.csv", "w")
file.write(csvOutputData_FS)
file.close()

file = open(outputDir + "ants_results.csv", "w")
file.write(csvOutputData_ANTS)
file.close()

