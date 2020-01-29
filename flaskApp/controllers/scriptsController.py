import views.scripts, sys
from models.model import Model
class ScriptController(object):
    def __init__(self):
        self.scripts = {}

    def loadView(self):
        return views.scripts.scriptsView(self.scripts)

    def displayDescription(self, scriptsDir):
        #Get the file list
        model = Model()
        self.scripts = model.getListOfScripts(scriptsPath=scriptsDir)
        