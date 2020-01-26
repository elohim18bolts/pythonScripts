import views.scripts, sys
class ScriptController(object):
    def scripts(self):
        return views.scripts.scriptsView()

    def displayDescription(self, scriptName):
        try:
            with open(scriptName, "r") as script:
                content =  script.read()
            return content
        except:
            return sys.exc_info()[0]