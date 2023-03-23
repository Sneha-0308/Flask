import json
from flask import Flask,jsonify,request
from googletrans import Translator

app = Flask(__name__)


translator = Translator()


@app.route("/translate", methods=['GET', 'POST'])
def translateKN():
    content = request.get_json()
    value=content.get('content')
    result=translator.translate(value, src='en', dest='kn')
    result=result.text
    # result.text 
    return result

if __name__ == "__main__":
    app.run(debug=True)


# from flask import Flask, jsonify, request
# app = Flask(__name__)
# @app.route('/api/add_message/<uuid>', methods=['GET', 'POST'])
# def add_message(uuid):
#     content = request.get_json()
#     # print(content) 
#     return content



# if __name__ == "__main__":
#     app.run(debug=True)