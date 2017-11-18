#!/usr/bin/python

import os
from random import *
import fileinput

directory = "C:/Program Files/Adobe/"										# path to adobe folder
directorylen = len(directory)

appXmlDirs = []
xmlfileNum = 0
totalFileNum = 0

print "Searching for application.xml files...\n"

for root, dirs, files in os.walk(directory):								# find all application.xml files
    for file in files:
		print file
		totalFileNum+=1
		if file.endswith('application.xml'):
			dirs = root + "\\" + file
			appXmlDirs.append(dirs)
			xmlfileNum+=1

print "\nSearched " + str(totalFileNum) + " files"

print "Found " + str(xmlfileNum) + " application.xml\n\n"

for pathToXml in appXmlDirs:
	
	finalContents = []
	
	fileToOpen = open(pathToXml, 'r')										# open the application.xml to read contents
	fileContents = fileToOpen.read()
	fileToOpen.close()
	
	
	if fileContents.find("TrialSerialNumber") != -1:						# search for the string "TrialSerialNumber" in the application.xml file
		locationOfSerial = fileContents.find("TrialSerialNumber") + 19		# search for the 24-digit serial number in the application.xml file 
		print pathToXml + "\n"
		serialNumber = fileContents[locationOfSerial:locationOfSerial+24]
		print "Found Serial Number: " + serialNumber
		
		fileToOpen.close()
		
		changedSerial = serialNumber[:-2]
		changedSerial = changedSerial + str(randint(10, 99))				# change the last 2-digits of the serial number
		print "Changed Serial Number: " + changedSerial + "\n"
		
		appName = pathToXml[directorylen:]									# find name of app in directory name
		appNameList = appName.split("\\")
		appName = appNameList[0]
		
		oldContents = open("OLD_" + appName + ".xml", 'w')					# create a backup of the application.xml file before overwriting the original
		oldContents.write(fileContents)
		oldContents.close()
		
		f1 = open(pathToXml, 'r')
		
		for line in f1:
			finalContents.append(line.replace(serialNumber, changedSerial))	# writes application.xml file contents to a list
																			# and replaces original serial number with changed serial number
		f1.close()
		
		finalContents = "".join(finalContents)								# joins the list to a string	
		
		print "Writing to file..."
		
		f2 = open(pathToXml, 'w')											
		f2.write(finalContents)												# writes the string to application.xml
		f2.close()
		
		print "Successfully changed Serial Number in Application.xml for " + appName
		
		print "\n\n"

#raw_input("")
os.system("pause")
		
		

