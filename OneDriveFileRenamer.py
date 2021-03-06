#!/bin/python

# Removes invalid characters from folder/file names so that files can be uploaded to OneDrive.
# Note: As is, you may need to run this several times. I was too lazy to come up with a better solution
# so as the program changes folder names, it can get stuck since it isn't updating the reference paths.

import os

path = "path not found"
for root, dirs, files in os.walk(os.path.expanduser("~/Documents/")):
	for f in dirs:
		if 'OneDrive' in f: #This should be adjusted to match the name of the OneDrive Folder if it has been changed.
			path = os.path.join(root,f)

print("Fixing files in: " + path)
print("Please Wait...")
chars = ['\"', '*', ':', '<' ,'>', '?' ,'/' ,'\\' ,'|', '#', '%', '&', '$','\'','{','}','@','~']

# Change file names
changes=0
for root,dirs,files in os.walk(path):
	for f in files:
		length = len(os.path.join(root,f))
		if length >= 400:
			print(f + "  is too long : " + str(length))
		for char in chars:
			if char in f:
				changes = changes + 1
			os.rename(os.path.join(root,f),os.path.join(root,f.replace(char,'').strip()))
			f=f.replace(char,'')
		os.rename(os.path.join(root,f),os.path.join(root,f.strip()))
	
print(str(changes) + " changes made to file names")

# Change folder names
changes = 0
for root,dirs,files in os.walk(path):	
	for f in dirs:
		length = len(os.path.join(root,f))
		if length >= 400:
			print(f + "  is too long : " + str(length))
		for char in chars:
			if char in f:
				changes = changes + 1
			os.rename(os.path.join(root,f),os.path.join(root,f.replace(char,'').strip()))
			f=f.replace(char,'')
		os.rename(os.path.join(root,f),os.path.join(root,f.strip()))

print(str(changes) + " changes made to folder names")
