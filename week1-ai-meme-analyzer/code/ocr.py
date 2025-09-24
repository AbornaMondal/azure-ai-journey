from azure.ai.vision.imageanalysis import ImageAnalysisClient
from azure.ai.vision.imageanalysis.models import VisualFeatures
from azure.core.credentials import AzureKeyCredential
from config import VISION_ENDPOINT, VISION_KEY


client = ImageAnalysisClient(endpoint=VISION_ENDPOINT, credential=AzureKeyCredential(VISION_KEY))

with open("../assets/meme1.png", "rb") as f:
    image_data = f.read()

result = client.analyze(
   image_data=image_data,
    visual_features=[VisualFeatures.READ]
)

for line in result.read.blocks[0].lines:
    print(f"Line: {line.text}")

result1 = client.analyze(
   image_data=image_data,
    visual_features=[VisualFeatures.CAPTION]
)
print("Image analysis results:")
print(" Caption:")  
if result1.caption is not None:
    print(f"   '{result1.caption.text}', Confidence {result1.caption.confidence:.4f}")  