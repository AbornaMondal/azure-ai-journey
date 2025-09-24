import streamlit as st
from azure.ai.translation.text import TextTranslationClient, TranslatorCredential
from azure.ai.translation.text.models import InputTextItem
from azure.ai.textanalytics import TextAnalyticsClient
from azure.core.credentials import AzureKeyCredential
from config import TRANSLATOR_ENDPOINT, TRANSLATOR_KEY, REGION, TEXT_ANALYTICS_ENDPOINT, TEXT_ANALYTICS_KEY


# Function: Translate + Sentiment
def translate_and_analyze(input_texts, target_lang="en"):
    # 1. Set up clients
    translation_client = TextTranslationClient(
        endpoint=TRANSLATOR_ENDPOINT,
        credential=TranslatorCredential(TRANSLATOR_KEY, REGION)
    )
    sentiment_client = TextAnalyticsClient(
        endpoint=TEXT_ANALYTICS_ENDPOINT,
        credential=AzureKeyCredential(TEXT_ANALYTICS_KEY)
    )

    # 2. Translate (auto-detect source language)
    documents = [InputTextItem(text=text) for text in input_texts]
    translation_result = translation_client.translate(
        content=documents,
        to=[target_lang]   # no `from_parameter` → auto-detect language
    )

    translated_texts, detected_langs = [], []
    for doc in translation_result:
        translated_texts.append(doc.translations[0].text)
        detected_langs.append(doc.detected_language.language)

    # 3. Sentiment analysis on translated text
    sentiment_result = sentiment_client.analyze_sentiment(documents=translated_texts)

    results = []
    for idx, sentiment in enumerate(sentiment_result):
        results.append({
            "original": input_texts[idx],
            "detected_lang": detected_langs[idx],
            "translated": translated_texts[idx],
            "sentiment": sentiment.sentiment,
            "positive": sentiment.confidence_scores.positive,
            "neutral": sentiment.confidence_scores.neutral,
            "negative": sentiment.confidence_scores.negative
        })
    return results


# ---------- Streamlit UI ----------
st.set_page_config(page_title="🌍 AI Translate + Sentiment", page_icon="🤖", layout="centered")

st.title("🌍 AI Translate + Sentiment Analyzer 🤖")
st.write("Paste text in any language, I’ll auto-detect it, translate to English, and analyze sentiment.")

# Input area (multi-line)
user_input = st.text_area("✍️ Enter text (any language):", "Hola, me llamo Aborna. Estoy aprendiendo inteligencia artificial.")

if st.button("🔎 Translate & Analyze"):
    if user_input.strip():
        with st.spinner("Translating and analyzing..."):
            results = translate_and_analyze([user_input], target_lang="en")

        # Display results
        for res in results:
            st.subheader("Results")
            st.write("🌐 **Detected Language:**", res["detected_lang"])
            st.write("📝 **Original Text:**", res["original"])
            st.write("🔤 **Translated (English):**", res["translated"])
            st.write("💡 **Sentiment:**", res["sentiment"])

            # Sentiment bars
            st.progress(res["positive"])
            st.write("😊 Positive:", round(res["positive"], 2))
            st.write("😐 Neutral:", round(res["neutral"], 2))
            st.write("😡 Negative:", round(res["negative"], 2))
    else:
        st.warning("⚠️ Please enter some text.")
