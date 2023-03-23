# from googletrans import Translator


# translator = Translator()


# text = 'Hello'

# translated_text = translator.translate(text, src='en', dest='kn')

# print(translated_text.text)



from flask import Flask, jsonify, request
app = Flask(__name__)
@app.route('/api/add_message/<uuid>', methods=['GET', 'POST'])
def add_message(uuid):
    content = request.get_json()
    # print(content)
    #  
    return content.get('key')



if __name__ == "__main__":
    app.run(debug=True)