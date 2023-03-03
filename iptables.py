# save this as app.py
from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello, World!"

@app.route("/index")
def start():
    return render_template("index.html")

@app.route("/alias")
def alias():
    return render_template("alias.html")

@app.route("/rules_filter")
def rules_filter():
    return render_template("rules_filter.html")

@app.route("/rules_nat")
def rules_nat():
    return render_template("rules_nat.html")
