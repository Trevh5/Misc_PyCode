#!/bin/python

import os
import csv
import numpy as np
import pandas as pd

inputDir = 'D:\\Research\\Bigler\\Repeatability_Paper\\Final_Data\\'
fsFileName = 'FS_SelectData.csv'
antsFileName = 'ANTS_SelectData.csv'

fsData = []
fsFile = csv.reader(open(inputDir+fsFileName))

antsData = []
antsFile = csv.reader(open(inputDir+antsFileName))

for row in fsFile:
	fsData.append(row)

for row in antsFile:
	antsData.append(row)

Header_fs = fsData[0]
fsData.pop(0)

Header_ants = antsData[0]
antsData.pop(0)


print(antsData[0][0].replace(".nii.gz",""))