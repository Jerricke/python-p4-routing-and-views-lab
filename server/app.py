#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello_world():
    return f"<h1>Python Operations with Flask Routing and Views</h1>"


@app.route("/print/<string:parameter>")
def print_string(parameter):
    print(parameter)
    return f"{parameter}"


@app.route("/count/<int:parameter>")
def count(parameter):
    counter = f""
    for i in range(parameter):
        counter += f"{i}\n"
    return counter


@app.route("/math/<int:num1>/<string:operation>/<int:num2>")
def math(num1, operation, num2):
    dict = {
        "+": num1 + num2,
        "-": num1 - num2,
        "*": num1 * num2,
        "div": num1 / num2,
        "%": num1 % num2,
    }
    return f"{dict.get(operation)}"
    pass


if __name__ == "__main__":
    app.run(port=5555, debug=True)
