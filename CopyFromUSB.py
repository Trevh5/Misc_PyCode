#!/bin/python

import subprocess
import time
import shutil
import errno
from os import listdir

#--
volumes_folder = "/Volumes/"
usb_name = "usb_pi"
usb_path = volumes_folder + usb_name
save_location = "/Users/tjh78349/Desktop/"
destination_path = save_location + "recentlyCopied/"
#--

while True:
    dirList = listdir(volumes_folder)
    for folder in dirList:
        if 'usb_pi' in folder:
            print(folder + " has been connected. Copying files.. PLEASE WAIT")
            filesToCopyList = listdir(usb_path)
            try:
                shutil.copytree(usb_path, destination_path)
            except EnvironmentError:
                print("Sorry there was an error. Please check file paths and make sure you aren't copying to an existing directory")
            print("Done! Please Remove the usb drive.")
    time.sleep(10)