# 🖼️ Week 1 — AI Meme Analyzer  

[![Python](https://img.shields.io/badge/Python-3.9%2B-blue?logo=python&logoColor=white)](https://www.python.org/)  
[![Streamlit](https://img.shields.io/badge/Streamlit-App-red?logo=streamlit&logoColor=white)](https://streamlit.io/)  
[![Azure AI](https://img.shields.io/badge/Azure%20AI-OCR%20%7C%20Content%20Safety-0078D4?logo=microsoft-azure&logoColor=white)](https://azure.microsoft.com/en-in/services/ai-services/)  
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)  

---

**📌 Project Name:** *Azure AI Meme Analyzer*  

**🛠️ Services Used:**  
- 🔎 **Azure Vision (OCR)** → Extracts text from memes  
- 🛡️ **Azure Content Safety (Moderation)** → Analyzes text & image safety  
- 🎛️ **Streamlit (UI)** → Interactive web app  

**🎯 Goal:** Upload memes, extract text, and check whether they are safe for sharing.  

**🏗️ Architecture:**  
🖼️ Image → 🔎 Vision OCR → 🛡️ Content Safety (Image + Text) → 🎛️ Streamlit UI  

---

## 🚀 Steps to Run  

1. **🌐 Create Azure resources**  
   - 📷 Vision resource (for OCR)  
   - 🛡️ Content Safety resource (for moderation)  
   - Get their **🔑 endpoint** and **key** values  

2. **⚙️ Add configuration**  
   - Copy `config.example.py` → rename to `config.py`  
   - Add your Vision & Content Safety **keys** and **endpoints**  

3. **📦 Install dependencies**  
   ```bash
   pip install -r requirements.txt
   ```

4. **▶️ Run the app**  
   ```bash
   streamlit run app.py
   ```

5. **🖼️ Upload a meme**  
   - Select an image (`.png`, `.jpg`, `.jpeg`)  
   - The app will:  
     ✅ Extract text (OCR)  
     ✅ Check **image & text safety**  
     ✅ Show results in 📊 tables  

---

## 📊 Output  

- 📝 **Extracted text** → OCR strings  
- 🖼️ **Image Safety Verdict** → Categories + severity  
- 💬 **Text Safety Verdict** → Categories + severity  
- 📷 *(Optional)* Screenshot of Streamlit UI in `assets/`  

---

## 💡 What We Learned  

- 🔎 OCR works surprisingly well even with noisy meme fonts.  
- 🛡️ Moderation is **critical** for user-generated content.  
- ⚡ Streamlit + Azure AI = Fast, fun, and powerful app building.  

---

👤 **Created by:** Aborna Mondal  
🌟 Shared as part of my **Azure AI Learning Journey**  
