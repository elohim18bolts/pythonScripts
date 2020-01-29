import os, re

class Script(object):
    """Read and proccess the scripts files(script description and script solution.)"""
    def __init__(self, scriptPath):
        self.content = None; self.title = None; self.name = None; self.path  = scriptPath
        if(not os.path.exists(scriptPath)):
            self.content = "Failed to load content"
            self.title = "Not item found"
            self.name = "notItemFound"
        else:
            self.loadContent()
            self.buildTitle()
    
    def loadContent(self):
        try:
            with open(self.path, "r") as script:
                self.content = script.read()
        except:
            self.content = "Failed To Read Script File"

    def getName(self):
        self.name = os.path.splitext(os.path.basename(self.path))[0]

    def buildTitle(self):
        self.getName()
        
        regex = re.compile(r"[A-Z][a-z]*")
        result = regex.findall(self.name)
        self.title = " ".join(result)