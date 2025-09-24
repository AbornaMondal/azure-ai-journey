import streamlit as st
import json
from azure.ai.vision.imageanalysis import ImageAnalysisClient
from azure.ai.vision.imageanalysis.models import VisualFeatures
from azure.ai.contentsafety import ContentSafetyClient
from azure.ai.contentsafety.models import (
    AnalyzeImageOptions, ImageData,
    AnalyzeTextOptions
)
from azure.core.credentials import AzureKeyCredential
from config import VISION_ENDPOINT, VISION_KEY, SAFETY_ENDPOINT, SAFETY_KEY

# ---------- Streamlit UI ----------
st.set_page_config(page_title="Azure AI Meme Analyzer", page_icon="🖼️")
st.title("🖼️ Azure AI Meme Analyzer")
st.write("Upload a meme → Extract text → Check safety (image + text).")

# ---------- Clients ----------
vision_client = ImageAnalysisClient(
    endpoint=VISION_ENDPOINT,
    credential=AzureKeyCredential(VISION_KEY)
)

safety_client = ContentSafetyClient(
    endpoint=SAFETY_ENDPOINT,
    credential=AzureKeyCredential(SAFETY_KEY)
)

# ---------- Load image ----------
with open("../assets/meme1.png", "rb") as f:
    image_data = f.read()

# ---------- Step 1: OCR (extract text) ----------
ocr_result = vision_client.analyze(
    image_data=image_data,
    visual_features=[VisualFeatures.READ]
)

extracted_text = ""
if ocr_result.read is not None:
    for block in ocr_result.read.blocks:
        for line in block.lines:
            extracted_text += line.text + " "
else:
    extracted_text = None

# ---------- Step 2: Content Safety (image) ----------
image_request = AnalyzeImageOptions(
    image=ImageData(content=image_data)
)
image_response = safety_client.analyze_image(image_request)

image_analysis = [
    {"category": a.category, "severity": a.severity}
    for a in image_response.categories_analysis
]

# ---------- Step 3: Content Safety (text) ----------
text_analysis = []
if extracted_text:
    text_request = AnalyzeTextOptions(text=extracted_text)
    text_response = safety_client.analyze_text(text_request)
    text_analysis = [
        {"category": a.category, "severity": a.severity}
        for a in text_response.categories_analysis
    ]

# ---------- Step 4: Combined Result ----------
st.subheader("📊 Final Combined Result (JSON)")
result = {
    "ocr_text": extracted_text,
    "image_safety": image_analysis,
    "text_safety": text_analysis
}
st.code(json.dumps(result, indent=2, ensure_ascii=False), language="json")
#print(json.dumps(result, indent=2, ensure_ascii=False))
