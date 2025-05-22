# -*- coding: utf-8 -*-
"""
Created on Mon Mar 20 13:26:00 2023

@author: DROFNATS
"""

import yaml #pip install PyYAML
import os
import readYAML #my personal file
import fileObject #my personal file
import time
import io, hashlib, hmac
from datetime import datetime
import sys

def hashFile(filePath):
    """
    Generate a sha256 hash of a file, given the absolute directory of a file.

    Attributes
    ----------
    filePath : str
        The absolute path of the file to generate the hash value of.
    
    Returns
    -------
    str
        The sha256 has value of the file in string.

    """
    
    BLOCK_SIZE = 1048576
    try:
        with open(filePath, "rb") as f:
            file_hash = hashlib.sha256()
            fb = f.read(BLOCK_SIZE)
            while len(fb) > 0:
                file_hash.update(fb)
                fb = f.read(BLOCK_SIZE)
            return file_hash.hexdigest()
    except:
        print(datetime.today(), "#error Oops! I am unable to read file! The error returned is:", sys.exc_info()[0])
        print(datetime.today(), "#error", sys.exc_info()[1])
        print(datetime.today(), "#error If the total length of the path and name exceeds 256 characters, it might be the fault:" + str(len(filePath)))
        
        return ""

def hashFilesList(dirList):
    """
    Takes in an array of fileObject objects. All the files in the array will have its hash generated.

    Attributes
    ----------
    dirList : array
        An array of fileObject objects. Note that Python reads the parameter as a reference.
    
    Returns
    -------
    Nothing. The hashValue property of the fileObject objects inside the array will be updated with the hash value.
    The function uses the reference of the array.

    """
    for i in range(len(dirList)):
        dirList[i].hashValue = hashFile(dirList[i].basePath + dirList[i].filePath)


def countFiles(dir, basePath, recursive):
    """
    This function counts the number of files to generate hashes of.

    Returns
    -------
    An array of files with absolute path.

    """
    #print("Looping through directory " + dir)
    filePaths = []
    spaces = ''
    for entry in os.scandir(dir):
        
        try:
            # read the file
            if os.path.isdir(entry.path) and recursive:
                filePaths += countFiles(entry.path, basePath, recursive) #recursive function call.
            elif os.path.isfile(entry.path):
                print("\rfile: " + entry.path[len(basePath):] + "", end='')
                #print(entry.path[len(basePath):])
                
                #compute hash here
                spaces = " " * int(len(entry.path[len(basePath):]) + 6)

                #time.sleep(0.2) #sleep just to see the output
                path = entry.path[len(basePath):]
                
                newFile = fileObject.fileObject(basePath, path, "")
                filePaths.append(newFile)
                
                #filePaths.append(entry.path)
            elif os.path.isabs(entry.path):
                print("abs: " + entry.path[len(basePath):] + "", end="\n")
                # skip abs
                """
                spaces = " " * int(len(entry.path[len(basePath):]) + 6)
                path = entry.path[len(basePath):]
                newFile = fileObject.fileObject(basePath, path, "")
                filePaths.append(newFile)
                """
                
            elif os.path.isjunction(entry.path):
                print("os.path.isjunction " + entry.path )
            elif os.path.islink(entry.path):
                print("os.path.islink " + entry.path )
            elif os.path.ismount(entry.path):
                print("os.path.ismount " + entry.path )
            elif os.path.isdevdrive(entry.path):
                print("os.path.isdevdrive " + entry.path )
            elif os.path.isreserved(entry.path):
                print("os.path.isreserved " + entry.path )
            else:
                print("unknown file type: " + entry.path )
            #clear the line here
            #the leading \r is important
            print("\r" + spaces, end='\r') 
        except:
            print(datetime.today(), "#error Oops! I am unable to read file! The error returned is:", sys.exc_info()[0])
            print(datetime.today(), "#error", sys.exc_info()[1])
        

    #print("\r", end='\n')
    return filePaths
    
def writeFile(filesInPaths, fileEncoding):
    """
    Takes in an array of fileObject objects. 

    Attributes
    ----------
    filesInPaths : array
        An array of fileObject objects. Note that Python reads the parameter as a reference.
    
    Returns
    -------
    Nothing. A csv file is written out with the hash values and directories of the files.
    The function uses the reference of the array.

    """
    
    print("Writing hashes to file now.")
    timeNow = datetime.today()
    fileName_time = timeNow.strftime("%Y%m%d_%H%M%S-%f")
    
    try:
        with open(fileName_time + "_fileHash.csv", "w", encoding=fileEncoding) as file:
            file.write("Hash Value,Base Path,File Path\n")
            for i in range(len(filesInPaths)):
                try:
                    file.write(filesInPaths[i].csvOutput())
                except:
                    print(datetime.today(), "#error writeFile() Oops! I am unable to write to file! The error returned is:", sys.exc_info()[0])
                    print(datetime.today(), "#error writeFile()", sys.exc_info()[1])
                    print(datetime.today(), "#error writeFile() the file is:", filesInPaths[i].basePath, filesInPaths[i].filePath)
    except:
        print(datetime.today(), "#error writeFile() Oops! I am unable to write to file! The error returned is:", sys.exc_info()[0])
        print(datetime.today(), "#error writeFile()", sys.exc_info()[1])
        #sys.exit()

# configFile = sys.argv[1]
config = readYAML.readConfig(sys.argv[1])

# debugging output
"""
print("Paths to look at:")
for directory in config["basePath"]:
    print("Path: " + directory["path"] + "\n\tRecursive: " + directory["recursive"])

print("write file encoding: " + config["writeFileEncoding"])
"""
# debugging output end

print("begin os.scandir:")


filePaths = []
for directory in config["basePath"]:
    print("Looping through directory and sub-directories: " + directory["path"])
    recursive = False
    if(directory["recursive"] == "y"):
        recursive = True
    print("Recursive:", recursive)
    filePaths += countFiles(directory["path"], directory["path"], recursive)

print("There are " + str(len(filePaths)) + " files", end="\n")

hashFilesList(filePaths) #pass by reference note

writeFile(filePaths, config["writeFileEncoding"]) #pass by reference note
