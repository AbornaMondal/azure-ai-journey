from azure.ai.contentsafety import ContentSafetyClient
from azure.ai.contentsafety.models import AnalyzeImageOptions, ImageData
from azure.core.credentials import AzureKeyCredential
from config import SAFETY_ENDPOINT, SAFETY_KEY
import json

#create client
client = ContentSafetyClient(endpoint=SAFETY_ENDPOINT, credential=AzureKeyCredential(SAFETY_KEY))

#Load Image 
with open(r"meme1.png", "rb") as f:
    image_data = f.read()
    request = AnalyzeImageOptions(image=ImageData(content=image_data))    

# Analyze
response = client.analyze_image(request)    
    
# Transform response into your desired format
result = {
    "categoriesAnalysis": [
        {"category": analysis.category, "severity": analysis.severity}
        for analysis  in response.categories_analysis
    ]
}

# Pretty print JSON
print(json.dumps(result, indent=2))

