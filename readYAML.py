"""
https://stackabuse.com/reading-and-writing-yaml-to-a-file-in-python

"""
from datetime import datetime
import yaml
import sys

def readConfig(configFile):
    """
    Reads the config file. Make sure it is located in the same directory as this script.

    Returns
    -------
    config : Key/Value dictionary.
        DESCRIPTION.

    """
    
    try:
        with open(configFile, "r") as file:
            #config = yaml.load(file, Loader=yaml.FullLoader)
            #print(config)
            return yaml.load(file, Loader=yaml.FullLoader)
    except:
        print(datetime.today(), "Oops! I am unable to read the config file! The error returned is:", sys.exc_info()[0])
        print(datetime.today(), sys.exc_info()[1])
        sys.exit()