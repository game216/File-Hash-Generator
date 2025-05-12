# -*- coding: utf-8 -*-
"""
Created on Fri Jun  4 16:10:28 2021

@author: DROFNATS

https://www.w3resource.com/python-exercises/python-basic-exercise-64.php
https://thispointer.com/python-get-last-modification-date-time-of-a-file-os-stat-os-path-getmtime/
"""

import yaml
import os
import readYAML #my personal file
import time



def version001():
    """
    Uses os.listdir

    Returns
    -------
    None.

    """
    config = readYAML.readConfig()
    #print("base path: ", config["basePath"][0])
    print("begin os.listdir:")
    for directory in config["basePath"]:
        print("\nLooping through directory ", directory)
        for filename in os.listdir(directory):
            #print(os.path.join(directory, filename)) #join() argument must be str, bytes, or os.PathLike object, not 'float'
            print(os.path.join(filename, " %s" % time.ctime( os.path.getmtime( os.path.join(directory, filename) ) ), " %s" %os.path.getmtime( os.path.join(directory, filename) ) ) )

def version002():
    """
    uses os.scandir

    Returns
    -------
    None.

    """
    config = readYAML.readConfig()
    print("begin os.scandir:")
    for directory in config["basePath"]:
        print("\nLooping through directory ", directory)
        for entry in os.scandir(directory):
            print(entry.path)
            
def filesInDIR(dir):
    """
    uses os.scandir

    Returns
    -------
    None.

    """
    for entry in os.scandir(dir):
        if os.path.isdir(entry.path):
            filesInDIR(entry.path)
        elif os.path.isfile(entry.path):
            print(entry.path)
        else:  
            print("It is a special file (socket, FIFO, device file)" )
            
#version001()

config = readYAML.readConfig()
print("begin os.scandir:")
for directory in config["basePath"]:
    print("\nLooping through directory ", directory)
    filesInDIR(directory)