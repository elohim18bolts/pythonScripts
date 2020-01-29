import os
from models.scriptModel import Script
class Model(object):
    def getFiles(self, scriptsPath):
        if(not os.path.isdir(scriptsPath)):
            raise IOError("Scripts files not found at " + scriptsPath)
        else:
            return os.listdir(scriptsPath)
    
    def getListOfScripts(self,scriptsPath):
        
        files = self.getFiles(scriptsPath)
        print(files)
        scripts = []
        for file in files:
            scripts.append(Script(scriptsPath + os.path.sep + file))
        return scripts