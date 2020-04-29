from flask import Flask
from template import Template

app = Flask(__name__)
template = Template("My FirstProject")

@app.route("/")
def index():
    return "<h1 style='color:red'>hello world!!!</h1>"

@app.route("/<string:name>")
def hello(name):
    return template.header('MyFirstProject', 'This is my first project', "white", "black")