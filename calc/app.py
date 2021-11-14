from flask import Flask, request
from calc.operations import *

app = Flask(__name__)


@app.route('/welcome')
def welcome():
    return 'Welcome'# Put your app in here.

operations = {
    "add": add,
    "sub": sub,
    "mult": mult,
    "div": div
}


@app.route('/<operation>')
def add_url(operation):
    a = int(request.args["a"])
    b = int(request.args["b"])
    return f'{operations[operation](a,b)}'



@app.route('/div')
def div_url():
    a = int(request.args["a"])
    b = int(request.args["b"])
    return f'{div(a,b)}'


@app.route('/add/<subreddit>')
def show_subreddit(subreddit):
    return f"<h1>Browsing the {subreddit} Subreddit</h1>"