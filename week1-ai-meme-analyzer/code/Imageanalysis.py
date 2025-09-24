from azure.ai.vision.imageanalysis import ImageAnalysisClient
from azure.ai.vision.imageanalysis.models import VisualFeatures
from azure.core.credentials import AzureKeyCredential
from config import VISION_ENDPOINT, VISION_KEY


client = ImageAnalysisClient(endpoint=VISION_ENDPOINT, credential=AzureKeyCredential(VISION_KEY))

with open("meme1.png", "rb") as f:
    image_data = f.read()

result = client.analyze(
   image_data=image_data,
    visual_features=[VisualFeatures.CAPTION]
)

# Print caption results to the console
print("Image analysis results:")
print(" Caption:")
if result.caption is not None:
    print(f"   '{result.caption.text}', Confidence {result.caption.confidence:.4f}")

