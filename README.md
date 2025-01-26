---
title: All In One Translation
emoji: 📚
colorFrom: gray
colorTo: green
sdk: gradio
sdk_version: 5.12.0
app_file: app.py
pinned: false
short_description: Convert text/image/audio/video from src language to English
---

The space consists of 3/4 parts: - 

- Text translator - Input (Text), Output (Translated text in English)
- Image translator - Input (Image with any text), Output (English Translated text version of the text in the image)
- Audio translator - Input (Audio in any language), Output (English Translated text version of the audio)
- Video translator - Input (Video), Output (English Translated text version of the audio) [Not yet implemented]
********************************************************

Demo

********
**Text translator**
- Simple `deep-translator` library usage.
![image/png](https://cdn-uploads.huggingface.co/production/uploads/6464bd1692773d5eeb585aa3/dgdsx-s3xlywdKv_FboEM.png)

![image/png](https://cdn-uploads.huggingface.co/production/uploads/6464bd1692773d5eeb585aa3/9UpNPwyOVCP92IA3MuglY.png)

![image/png](https://cdn-uploads.huggingface.co/production/uploads/6464bd1692773d5eeb585aa3/PKrHGfWw699i9oKLMmtiB.png)

![image/png](https://cdn-uploads.huggingface.co/production/uploads/6464bd1692773d5eeb585aa3/OsJ8zFlG79-Jmw92apWUg.png)

***********
**Image translator**
- Best works with simple fonts. Performance detoriates with decorative fonts.
- For now, you have to choose the language, choosing "English" can work for almost all Latin-script languages like (Spanish, Romanian etc.)
- Using `pytesseract` model for image-to-text conversion. It's installation is a bit complicated. [Follow this link for installation](https://stackoverflow.com/a/52231794/17820006)

![image/png](https://cdn-uploads.huggingface.co/production/uploads/6464bd1692773d5eeb585aa3/s77gfruSV_QhjGxizR7H_.png)

![image/png](https://cdn-uploads.huggingface.co/production/uploads/6464bd1692773d5eeb585aa3/xIBgIs-MLf1sXZLivJQfN.png)

![image/png](https://cdn-uploads.huggingface.co/production/uploads/6464bd1692773d5eeb585aa3/qY4UxOWWNcpcg_n8ZNUXO.png)

*************
**Audio translator**
- Since I am on a free-tier space, the inference takes a lot of time (1000 seconds for 10 seconds of audio)
- If one has HuggingFace pro, he/she can get a GPU and get reasonable inference time. But for now, this is just a demo.
- If you have an OpenAPI key, you can use whisper speech-to-text model via API call. But since I don't have it, I used the whisper library method, where you have to take care of the inference hardware yourself.
![image/png](https://cdn-uploads.huggingface.co/production/uploads/6464bd1692773d5eeb585aa3/LQx-1fl1UPC9auBSF_lSi.png)
- Here is a 10 seconds translation of the famous Russian song [Kukushka](https://youtu.be/fuPX8mjeb-E?si=RSlOLLfVnt52UUGG)

Check out the configuration reference at https://huggingface.co/docs/hub/spaces-config-reference