import sys
import flaskApp.views.scripts as scriptViews
from flaskApp.models.model import Model
class ScriptController(object):
    def __init__(self):
        self.scripts = {}

    def loadView(self):
        return scriptViews.scriptsView(self.scripts)

    def displayContent(self, scriptsDir):
        #Get the file list
        model = Model()
        self.scripts = model.getListOfScripts(scriptsPath=scriptsDir)
        