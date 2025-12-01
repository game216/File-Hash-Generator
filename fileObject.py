class fileObject:
    
    def __init__(self, basePath, filePath, hashValue = "", mtime = "", ctime = ""):
        self.basePath = basePath
        self.filePath = ""
        self.fileName = ""
        fileDir = filePath.rsplit('\\', 1)
        self.fileMTime = mtime
        self.fileCTime = ctime
        
        if(len(fileDir) > 1):
            self.filePath = fileDir[0]
            self.fileName = fileDir[1]
        else:
            self.fileName = filePath
        self.hashValue = hashValue
        
        
    def csvOutput(self, delimiter):
        """
        lorem ipsum for csvOutput(self)

        Returns
        -------
        TYPE
            DESCRIPTION.

        """
        fileLine = "\"" + self.hashValue + "\"" + delimiter + "\"" + self.basePath + "\"" + delimiter 
        fileLine += "\"" + self.filePath + "\"" + delimiter + "\"" + self.fileName + "\"" + delimiter 
        fileLine += "\"" + self.fileMTime + "\"" + delimiter + "\"" + self.fileCTime + "\"" + "\n"
        return fileLine
    
    def fullFilePath(self):
        return self.basePath + "\\" + self.filePath + "\\" + self.fileName