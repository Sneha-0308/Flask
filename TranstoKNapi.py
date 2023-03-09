import json
from flask import Flask,jsonify
from googletrans import Translator

app = Flask(__name__)


translator = Translator()


@app.route("/translate/<string:text>")
def translateKN(text):
    result=translator.translate(text, src='en', dest='kn')
    result=result.text
    return result

if __name__ == "__main__":
    app.run(debug=True)