from flask import Flask
import controllers.homeController as homeController
import controllers.scriptsController as scriptsController
app = Flask(__name__)
#The rest of your code goes here.#eg:app.route('/')#def home():#	return homeView()
@app.route("/home")
@app.route("/")
def home():
    controller = homeController.HomeController()
    return controller.home()
@app.route("/scripts")
def scripts():
    controller = scriptsController.ScriptController()
    return controller.scripts()


app.run(debug = True)