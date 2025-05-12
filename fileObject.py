class fileObject:
    
    def __init__(self, basePath, filePath, hashValue = ""):
        self.basePath = basePath
        self.filePath = filePath
        self.hashValue = hashValue
        
        
    def csvOutput(self):
        return "\"" + self.hashValue + "\",\"" + self.basePath + "\",\"" + self.filePath + "\"\n"