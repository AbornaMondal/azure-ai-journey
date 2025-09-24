import streamlit as st
import azure.cognitiveservices.speech as speechsdk
from azure.ai.translation.text import TextTranslationClient, TranslatorCredential
from azure.ai.translation.text.models import InputTextItem
from azure.ai.textanalytics import TextAnalyticsClient
from azure.core.credentials import AzureKeyCredential
from config import SPEECH_KEY, SPEECH_REGION, TRANSLATOR_ENDPOINT, TRANSLATOR_KEY, REGION, TEXT_ANALYTICS_ENDPOINT, TEXT_ANALYTICS_KEY


# Function: Speech to Text (English)
def speech_to_text():
    speech_config = speechsdk.SpeechConfig(subscription=SPEECH_KEY, region=SPEECH_REGION)
    speech_config.speech_recognition_language = "en-US"  # force English
    recognizer = speechsdk.SpeechRecognizer(speech_config=speech_config)

    st.info("🎙️ Speak now... (listening in English)")
    result = recognizer.recognize_once_async().get()

    if result.reason == speechsdk.ResultReason.RecognizedSpeech:
        return result.text
    elif result.reason == speechsdk.ResultReason.NoMatch:
        return "❌ No speech could be recognized."
    else:
        return f"⚠️ Error: {result.reason}"


# Function: Translate (English → French) + Sentiment
def translate_and_analyze(input_texts, source_lang="en", target_lang="fr"):
    # Translation client
    translation_client = TextTranslationClient(
        endpoint=TRANSLATOR_ENDPOINT,
        credential=TranslatorCredential(TRANSLATOR_KEY, REGION)
    )

    # Sentiment client
    sentiment_client = TextAnalyticsClient(
        endpoint=TEXT_ANALYTICS_ENDPOINT,
        credential=AzureKeyCredential(TEXT_ANALYTICS_KEY)
    )

    # Translate English → French
    documents = [InputTextItem(text=text) for text in input_texts]
    translation_result = translation_client.translate(
        content=documents,
        to=[target_lang],
        from_parameter=source_lang
    )

    translated_texts = [doc.translations[0].text for doc in translation_result]

    # Sentiment on French text
    sentiment_result = sentiment_client.analyze_sentiment(documents=translated_texts)

    results = []
    for idx, sentiment in enumerate(sentiment_result):
        results.append({
            "original": input_texts[idx],
            "translated": translated_texts[idx],
            "sentiment": sentiment.sentiment,
            "positive": sentiment.confidence_scores.positive,
            "neutral": sentiment.confidence_scores.neutral,
            "negative": sentiment.confidence_scores.negative
        })
    return results


# ---------- Streamlit UI ----------
st.set_page_config(page_title="🎙️ English → French Translator", page_icon="🇫🇷")

st.title("🎙️ Speak English → Get French Translation 🇫🇷")
st.write("Speak in **English**, I’ll convert it into **French**, and also analyze sentiment of the French text.")

if st.button("🎤 Start Recording"):
    spoken_text = speech_to_text()
    st.success(f"🗣️ You said (English): {spoken_text}")

    if spoken_text and "❌" not in spoken_text and "⚠️" not in spoken_text:
        with st.spinner("Translating & analyzing..."):
            results = translate_and_analyze([spoken_text], source_lang="en", target_lang="fr")

        for res in results:
            st.subheader("Results")
            st.write("📝 **Original (English):**", res["original"])
            st.write("🔤 **Translated (French):**", res["translated"])
            st.write("💡 **Sentiment (on French text):**", res["sentiment"])

            st.progress(res["positive"])
            st.write("😊 Positive:", round(res["positive"], 2))
            st.write("😐 Neutral:", round(res["neutral"], 2))
            st.write("😡 Negative:", round(res["negative"], 2))
