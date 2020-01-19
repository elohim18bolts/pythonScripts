#!/usr/bin/python3
import os, sys 

try:
    projectName = sys.argv[1]
except:
    projectName = "flaskApp"


#Create the project directory
try:
    if(not os.path.exists(projectName)):
        os.mkdir(projectName)
    os.chdir(projectName)
except:
    print("Project creation failed.")
    print("Deleting folders...")
    if(os.path.exists(projectName)):
        os.rmdir(projectName)
    print(sys.exc_info()[0])
    raise

#Create the rest of the files
try:
    with open("__init__.py","wb") as init:
        init.write(b"from flask import Flask\n\n\n")
        init.write(b"app = Flask(__name__)")
        init.writelines([b"\n\n#The rest of your code goes here.",b"#eg:app.route('/')",b"#def home():",b"#\treturn homeView()"])
    dirs = ["views", "controllers", "templates", "statics"]
    for d in dirs:
        os.mkdir(d)
except:
    print("Error in creating directories and files...")
    print(sys.exc_info())
    raise  


