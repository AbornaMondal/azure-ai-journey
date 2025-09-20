import requests
import time
import sys
from config import VISION_ENDPOINT, VISION_KEY, SAFETY_ENDPOINT, SAFETY_KEY


def analyze_image_read_api(image_path):
    """Extract text from image using Azure Vision Read API"""
    post_url = VISION_ENDPOINT.rstrip('/') + "/vision/v3.2/read/analyze"
    headers = {
        "Ocp-Apim-Subscription-Key": VISION_KEY,
        "Content-Type": "application/octet-stream"
    }
    with open(image_path, "rb") as f:
        data = f.read()

    resp = requests.post(post_url, headers=headers, data=data)
    if resp.status_code != 202:
        print("Vision Error:", resp.status_code, resp.text)
        return []

    # Poll for results
    op_location = resp.headers.get("operation-location")
    while True:
        r = requests.get(op_location, headers={"Ocp-Apim-Subscription-Key": VISION_KEY})
        rj = r.json()
        status = rj.get("status")
        if status == "succeeded":
            lines = []
            for read_result in rj.get("analyzeResult", {}).get("readResults", []):
                for line in read_result.get("lines", []):
                    lines.append(line.get("text"))
            return lines
        elif status == "failed":
            print("Read API failed:", rj)
            return []
        time.sleep(1)


def check_content_safety(text):
    """Check text safety using Azure AI Content Safety"""
    url = SAFETY_ENDPOINT.rstrip('/') + "/contentsafety/text:analyze?api-version=2023-04-30-preview"
    headers = {
        "Ocp-Apim-Subscription-Key": SAFETY_KEY,
        "Content-Type": "application/json"
    }
    payload = {
        "text": text,
        "categories": ["Hate", "SelfHarm", "Sexual", "Violence"]
    }

    resp = requests.post(url, headers=headers, json=payload)
    if resp.status_code != 200:
        print("Safety Error:", resp.status_code, resp.text)
        return {}

    result = resp.json()
    return result


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python run_ocr.py path/to/image.png")
        sys.exit(1)

    img = sys.argv[1]

    # Step 1: OCR
    print("🔍 Running OCR on image:", img)
    text_lines = analyze_image_read_api(img)

    if not text_lines:
        print("No text found in image.")
        sys.exit(0)

    extracted_text = " ".join(text_lines)
    print("\n📄 Extracted Text:")
    print(extracted_text)

    # Step 2: Content Safety
    print("\n🛡 Checking Content Safety...")
    safety_result = check_content_safety(extracted_text)

    print("\n✅ Safety Result:")
    print(safety_result)
