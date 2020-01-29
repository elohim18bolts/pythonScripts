from flask import render_template

def scriptsView(scriptsList):
    return render_template("Scripts.html",scripts=scriptsList)