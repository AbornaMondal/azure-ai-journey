from azure.ai.translation.text import TextTranslationClient, TranslatorCredential
from azure.ai.translation.text.models import InputTextItem
from config import TRANSLATOR_ENDPOINT, TRANSLATOR_KEY ,REGION

credential = TranslatorCredential(TRANSLATOR_KEY,REGION)
client = TextTranslationClient(endpoint=TRANSLATOR_ENDPOINT, credential= credential)

source_language = "fr"
target_language = ["en"] 

input_text = "Salut ! Comment ça va ?"
documents =[InputTextItem(text=input_text)]
response = client.translate(content = documents, to=target_language, from_parameter=source_language)

print("Original Text: ", input_text)
for translation in response[0].translations:
    print("Translated Text:", translation.text)