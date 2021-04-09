# Put your app in here.
from flask import Flask, request
from operations import add, sub, mult, div

app = Flask(__name__)

def return_math(op):
    a = int(request.args["a"])
    b = int(request.args["b"])
    num = op(a, b)
    return str(num)

@app.route("/add")
def return_add():
    return return_math(add)

@app.route("/sub")
def return_sub():
    return return_math(sub)

@app.route("/mult")
def return_mult():
    return return_math(mult)

@app.route("/div")
def return_div():
    return return_math(div)

# consolidated
functions = {
    "add": add,
    "sub": sub,
    "mult": mult,
    "div": div
}

@app.route("/math/<opr>")
def math(opr):
    return return_math(functions[opr])
