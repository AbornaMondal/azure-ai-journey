# Week 1 — AI Meme Analyzer

**Project Name:** Azure AI Meme Analyzer  
**Services Used:** Azure Vision (OCR), Azure Content Safety (Moderation), Streamlit (UI)  
**Goal:** Upload memes, extract text, and check whether they are safe for sharing.  
**Architecture:** Image → Vision OCR → Content Safety (Image + Text) → Streamlit UI

## Steps to Run
1. **Create Azure resources**  
   - Vision resource (for OCR)  
   - Content Safety resource (for moderation)  
   - Get their **endpoint** and **key** values.

2. **Add configuration**  
   - Copy `config.example.py` → rename to `config.py`.  
   - Add your Vision & Content Safety keys and endpoints.  

3. **Install dependencies**
   - pip install -r requirements.txt

4. **Run the app**
   - streamlit run app.py  

5. **Upload a meme**  
   - Choose an image from your system (`png`, `jpg`, `jpeg`).  
   - The app will:  
     - Extract text (OCR)  
     - Check safety for both **image** and **text**  
     - Display results in tables  
---
## Output
- **Extracted text string(s)** (from OCR)  
- **Image Safety verdict** (categories + severity)  
- **Text Safety verdict** (categories + severity)  
- Optional: Add a screenshot of the app UI inside `assets/`
---
## What We Learned
- OCR extracts meme text surprisingly well, even with noisy fonts.  
- Content moderation is crucial when handling **user-generated content**.  
- Streamlit + Azure AI makes it possible to build a working AI app with minimal code.  
---
👤 **Created by:** Aborna Mondal  
📌 Shared as part of my **Azure AI Learning Journey**
