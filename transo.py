from googletrans import Translator


translator = Translator()


text = 'Hello'

translated_text = translator.translate(text, src='en', dest='kn')

print(translated_text.text)
