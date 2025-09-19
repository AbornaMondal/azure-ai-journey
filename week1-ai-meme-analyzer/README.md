# Week 1 — AI Meme Analyzer

**Project Name:** AI Meme Analyzer  
**Services Used:** Azure Computer Vision (OCR), Azure Content Safety (moderation)  
**Goal:** Extract text from memes and mark whether the meme is safe for sharing.  
**Architecture:** Image → Vision OCR → Content Safety → UI / Output screenshot

## Steps to run
1. Create Azure Vision resource + Content Safety resource and get keys.
2. Edit `code/config.example.py` with your endpoint & key (rename to `config.py`).
3. Run the script: `python code/run_ocr.py --image ./assets/meme1.png`
4. Screenshot the output and add to `assets/result1.png`.

## Output
- Extracted text string(s)
- Safety verdict (Safe / Unsafe)
- Sample screenshot in `assets/`

## What we learned
- OCR handles noisy fonts fairly well.
- Content filtering is essential if you publish user content.
- Quick integration with minimal code.

## Next steps
- Add Custom Vision to classify meme categories.
- Build a small UI to upload memes live.
