import googletrans
from googletrans import Translator

# print(googletrans.LANGUAGES)
# print(googletrans.LANGCODES)

# text1="suscríbete a mi canal"

# translator = Translator()


# print(translator.translate(text1))
text1 = "subscribe my channel"
 
text2 = "suscríbete a mi canal"
 
text3 = "kanalıma abone ol"
 
 
 
translator = Translator()
 
 
print("Translate English to ESP : ", translator.translate(text1, src='en', dest='es'))
 
print("Translate En to Tur : ", translator.translate(text1, src='en', dest='tr'))
 