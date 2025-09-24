from azure.ai.textanalytics import TextAnalyticsClient
from azure.core.credentials import AzureKeyCredential
from config import TEXT_ANALYTICS_ENDPOINT, TEXT_ANALYTICS_KEY

client = TextAnalyticsClient(   
    endpoint=TEXT_ANALYTICS_ENDPOINT, 
    credential=AzureKeyCredential(TEXT_ANALYTICS_KEY))

documents = [
    "I had the best day of my life.",   
    "This was a waste of my time. The speaker put me to sleep." ,
    "No tengo dinero ni nada que dar..."
]
response = client.analyze_sentiment(documents=documents)
for result in response:
    print(f"Sentence: {result.sentences[0].text}")   
    print("Document Sentiment: {}".format(result.sentiment))
    print("Overall scores: positive={}; neutral={}; negative={} \n".format(   
        result.confidence_scores.positive,   
        result.confidence_scores.neutral,   
        result.confidence_scores.negative ))
 

    