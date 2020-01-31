import os
from flaskApp.models.scriptModel import Script
class Model(object):
    def getFiles(self, scriptsPath):
        if(not os.path.isdir(scriptsPath)):
            raise IOError("Scripts files not found at " + scriptsPath)
        else:
            return os.listdir(scriptsPath)
    
    def getListOfScripts(self,scriptsPath):
        
        files = self.getFiles(scriptsPath)
        scripts = []
        for file in files:
            filename = os.path.splitext(os.path.basename(file))[0]
            route = os.path.split(scriptsPath)[0]
            codePath = route + os.path.sep + "solutions" + os.path.sep + filename
            scripts.append(Script(scriptsPath + os.path.sep + file,codePath))
        return scripts