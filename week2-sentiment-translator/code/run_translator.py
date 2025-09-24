import requests
from config import TRANSLATOR_ENDPOINT, TRANSLATOR_KEY, TEXT_ANALYTICS_ENDPOINT, TEXT_ANALYTICS_KEY

# translate text to English
def translate_text(text, to_language="en"):
    url = TRANSLATOR_ENDPOINT.rstrip("/") + "/translate?api-version=3.0&to=" + to_language
    headers = {
        "Ocp-Apim-Subscription-Key": TRANSLATOR_KEY,
        "Content-Type": "application/json"
    }
    body = [{ "text": text }]

    response = requests.post(url, headers=headers, json=body)
    response.raise_for_status()
    return response.json()

# analyze sentiment of text
def analyze_sentiment(text):
    url = TEXT_ANALYTICS_ENDPOINT.rstrip("/") + "/text/analytics/v3.1/sentiment"
    headers = {
        "Ocp-Apim-Subscription-Key": TEXT_ANALYTICS_KEY,
        "Content-Type": "application/json"
    }
    body = { "documents": [{ "id": "1", "language": "en", "text": text }] }

    response = requests.post(url, headers=headers, json=body)
    response.raise_for_status()
    return response.json()


# main program
if __name__ == "__main__":
    input_text = input("Enter text in any language: ")

    print("\n🔄 Translating...")
    translation_result = translate_text(input_text)
    translated_text = translation_result[0]['translations'][0]['text']
    print("Translated Text:", translated_text)

    print("\n📊 Analyzing Sentiment...")
    sentiment_result = analyze_sentiment(translated_text)
    sentiment = sentiment_result['documents'][0]['sentiment']
    scores = sentiment_result['documents'][0]['confidenceScores']
    print("Sentiment:", sentiment, "| Scores:", scores)
