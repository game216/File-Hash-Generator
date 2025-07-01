class fileObject:
    
    def __init__(self, basePath, filePath, hashValue = ""):
        self.basePath = basePath
        fileDir = filePath.rsplit('\\', 1)
        self.filePath = fileDir[0]
        self.fileName = fileDir[1]
        self.hashValue = hashValue
        
        
    def csvOutput(self, delimiter):
        """
        lorem ipsum for csvOutput(self)

        Returns
        -------
        TYPE
            DESCRIPTION.

        """
        return "\"" + self.hashValue + "\"" + delimiter + "\"" + self.basePath + "\"" + delimiter + "\"" + self.filePath + "\"" + delimiter + "" + self.fileName + "\n"
    
    def fullFilePath(self):
        return self.basePath + "\\" + self.filePath + "\\" + self.fileName