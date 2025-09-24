from azure.ai.translation.text import TextTranslationClient, TranslatorCredential
from azure.ai.translation.text.models import InputTextItem
from config import TRANSLATOR_ENDPOINT, TRANSLATOR_KEY ,REGION
from azure.ai.textanalytics import TextAnalyticsClient
from azure.core.credentials import AzureKeyCredential
from config import TEXT_ANALYTICS_ENDPOINT, TEXT_ANALYTICS_KEY


def translate_and_analyze(input_texts, source_lang="fr", target_lang="en"):
    #1. Set up client     
    credential = TranslatorCredential(TRANSLATOR_KEY,REGION)
    translation_client = TextTranslationClient(endpoint=TRANSLATOR_ENDPOINT, credential= credential)
    sentiment_client = TextAnalyticsClient(endpoint=TEXT_ANALYTICS_ENDPOINT, credential=AzureKeyCredential(TEXT_ANALYTICS_KEY))

    #2. Translate texts
    documents =[InputTextItem(text=text) for text in input_texts]   
    translation_result = translation_client.translate(content = documents, to=[target_lang], from_parameter=source_lang)
    translated_texts = [translation.text for doc in translation_result for translation in doc.translations]

    #3. Analyze sentiment of translated texts
    sentiment_result = sentiment_client.analyze_sentiment(documents=translated_texts)   

    # 4. Display combined results
    for idx, sentiment in enumerate(sentiment_result):
        print("Original ({}): {}".format(source_lang, input_texts[idx]))
        print("Translated ({}): {}".format(target_lang, translated_texts[idx]))
        print("Sentiment:", sentiment.sentiment)
        print("Scores: pos={}; neu={}; neg={}\n".format(
            sentiment.confidence_scores.positive,
            sentiment.confidence_scores.neutral,
            sentiment.confidence_scores.negative
        ))
        
# ---------- Example Run ----------
if __name__ == "__main__":
    input_sentences = [
        "Salut ! Comment ça va ?",
        "Je m'appelle Aborna et j'apprends l'intelligence artificielle.",
        "Il fait très beau aujourd'hui.",
        "J’aime écouter de la musique le soir."
    ]
    translate_and_analyze(input_sentences, source_lang="fr", target_lang="en")