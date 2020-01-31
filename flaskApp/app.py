from flask import Flask
import os
import flaskApp.controllers.homeController as homeController
import flaskApp.controllers.scriptsController as scriptsController

app = Flask(__name__)
#The rest of your code goes here.#eg:app.route('/')#def home():#	return homeView()
@app.route("/home")
@app.route("/")
def home():
    controller = homeController.HomeController()
    return controller.loadView()\
        
@app.route("/scripts")
def scripts():
    scriptsPath = "./resources/files/codingQuestions"
    controller = scriptsController.ScriptController()
    controller.displayContent(scriptsPath)
    return controller.loadView()

