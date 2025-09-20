import requests
import time
import sys
from config import VISION_ENDPOINT, VISION_KEY

def analyze_image_read_api(image_path):
    post_url = VISION_ENDPOINT.rstrip('/') + "/vision/v3.2/read/analyze"
    headers = { 
        "Ocp-Apim-Subscription-Key": VISION_KEY,
        "Content-Type": "application/octet-stream"
    }
    with open(image_path, "rb") as f:
        data = f.read()
    resp = requests.post(post_url, headers=headers, data=data)
    if resp.status_code != 202:
        print("Error:", resp.status_code, resp.text)
        return

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
            print("OCR Text:\n", "\n".join(lines))
            return lines
        elif status == "failed":
            print("Read API failed:", rj)
            return
        time.sleep(1)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python run_ocr.py path/to/image.png")
        sys.exit(1)
    img = sys.argv[1]
    analyze_image_read_api(img)
