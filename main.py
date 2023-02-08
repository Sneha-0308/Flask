# https://flask.palletsprojects.com/en/2.2.x/quickstart/#:~:text=A%20Minimal%20Application%20%C2%B6%20A%20minimal%20Flask%20application,%3D%20Flask%28__name__%29%20%40app.route%28%22%2F%22%29%20def%20hello_world%28%29%3A%20return%20%22%3Cp%3EHello%2C%20World%21%3C%2Fp%3E%22

from flask import Flask, jsonify
app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/sum/<int:a>/<int:b>")
def sum(a,b):
    return str(a+b)

if __name__ == "__main__":
    app.run(debug=True)