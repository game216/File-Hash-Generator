# -*- coding: utf-8 -*-
"""
Created on Mon Mar 20 13:26:00 2023

@author: DROFNATS
"""

import yaml #pip install PyYAML
import os
import readYAML #my personal file
import time
import io, hashlib, hmac
from datetime import datetime
import sys

def filesInDIR(dir):
    """
    uses os.scandir

    Returns
    -------
    None.

    """
    filesInPaths = ""
    spaces = ''
    BLOCK_SIZE = 1048576
    
    for entry in os.scandir(dir):
        try:
            #read the file
            if os.path.isdir(entry.path):
                filesInPaths += filesInDIR(entry.path)
            elif os.path.isfile(entry.path):
                #print(entry.path)
                print("\rfile: " + entry.path + " ", end="")
                spaces = " " * int(len(entry.path) + 6)
                with open(entry.path, "rb") as f:
                    file_hash = hashlib.sha256()
                    fb = f.read(BLOCK_SIZE)
                    while len(fb) > 0:
                        file_hash.update(fb)
                        fb = f.read(BLOCK_SIZE)
                    filesInPaths +=  file_hash.hexdigest() + "," + entry.path + "\n"
                #print("\b")
            else:  
                print("It is a special file (socket, FIFO, device file): " + entry.path )
                #TODO: if dir+path is too long, it reaches here
        except:
            print(datetime.today(), "#error Oops! I am unable to read file! The error returned is:", sys.exc_info()[0])
            print(datetime.today(), "#error", sys.exc_info()[1])

        #clear the line here
        #the leading \r is important
        print("\r" + spaces, end='\r')
    return filesInPaths

def countFiles(dir):
    """
    This function counts the number of files to generate hashes of.

    Returns
    -------
    An array of files with absolute path.

    """
    filePaths = []
    spaces = ''
    for entry in os.scandir(dir):
        
        try:
            # read the file
            if os.path.isdir(entry.path):
                filePaths += countFiles(entry.path)
                #filePaths.append(countFiles(entry.path))
            elif os.path.isfile(entry.path):
                print("\rfile: " + entry.path + "", end='')
                #compute hash here
                spaces = " " * int(len(entry.path) + 6)
                #print("file: " + entry.path + "", end="\n")
                #time.sleep(0.2) #sleep just to see the output
                filePaths.append(entry.path)
            else:
                print("It is a special file (socket, FIFO, device file): " + entry.path )
            #clear the line here
            #the leading \r is important
            print("\r" + spaces, end='\r') 
        except:
            print(datetime.today(), "#error Oops! I am unable to read file! The error returned is:", sys.exc_info()[0])
            print(datetime.today(), "#error", sys.exc_info()[1])
        

    #print("\r", end='\n')
    return filePaths
    
def writeFile(filesInPaths):
    print("Writing hashes to file now.")
    timeNow = datetime.today()
    fileName_time = timeNow.strftime("%Y%m%d_%H%M%S-%f")
    try:
        with open(fileName_time + "_fileHash.csv", "w") as file:
            file.write("Hash,File Path\n")
            file.write(filesInPaths)
    except:
        print(datetime.today(), "Oops! I am unable to write to file! The error returned is:", sys.exc_info()[0])
        print(datetime.today(), sys.exc_info()[1])
        sys.exit()

# configFile = sys.argv[1]
config = readYAML.readConfig(sys.argv[1])
print("begin os.scandir:")

filesInPaths = ""

filePaths = []
for directory in config["basePath"]:
    filePaths += countFiles(directory)

print("There are " + str(len(filePaths)) + " files", end="\n")

for directory in config["basePath"]:
    print("\nLooping through directory ", directory)
    filesInPaths += filesInDIR(directory)

#print(filesInPaths)
writeFile(filesInPaths)
