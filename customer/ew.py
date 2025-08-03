
import googletrans
from googletrans import Translator
translator = Translator()
text_to_translate = translator.translate('Hello', src = 'en', dest = 'mr')
res=text_to_translate.text
print(text_to_translate.text)
