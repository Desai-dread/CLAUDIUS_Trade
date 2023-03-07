from flask import Flask
from flask import render_template, request
from jinja2 import *

app = Flask(__name__)

cards = ["Купон 1", "Купон 2", "Купон 3", "Купон 4"]
src = "static/image.jpg"
@app.route('/')
def trade():
    return render_template("trade.html", src=src, cards=cards)

    
