#!/bin/python
# Use to remove invalid names from onedrive folder

import os

path = "path not found"
for root, dirs, files in os.walk(os.path.expanduser("~/Documents/")):
	for f in dirs:
		if 'OneDrive - Creighton University' in f:
			path = os.path.join(root,f)

print("Fixing files in: " + path)
print("Please Wait...")
chars = ['\"', '*', ':', '<' ,'>', '?' ,'/' ,'\\' ,'|', '#', '%', '&', '$','\'','{','}','@','~']

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
