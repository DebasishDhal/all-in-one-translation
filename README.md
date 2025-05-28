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
****************************
<p align="center">
    Liked the setup? Put a like on top left, it takes only 2 seconds.
</p>

# Logs 
- 27/05/2025 - This app receieved bulk usage, in terms of data size. 63 requests with input text of size 3.3MB. The `https://detectlanguage.com/` API can only support 1MB/day. My personal API key was suspeded, making this app dysfunctional.
- 28/05/2025 - I have removed the need for an external API. Using `langdetect` library for the same purpose now. No limitations of usage (Theoretically).
****************************
Replication
 - Requirements
    - Free API Key from https://detectlanguage.com/ for automatic language detection from text.
    - GPU for `Whisper` model inference. It's slower in CPU.
 - Notes
    - `pytesseract` library (For image-to-text) is easier to install in linux machines.
    - If you have GPU, you can go for more sophisticated image-to-text models.
    - The image-to-text setup works best for non-decorative and normal sized fonts.
*******

The space consists of 3-4 parts: - 

- Text translator - Input (Input Text, Target language), Output (Translated text in target language, Source language name)
- Image translator - Input (Image with any text, Source language, Target language), Output (Image text in source language, Image text translated to target language)
- Audio translator - Input (Audio in any language, Model size, Target language), Output (Transcribed original text, Transcribed text translated to target language, Original language name)
- Video translator - Input (Video, Model size, Target language), Output (Translated text version of the audio) [Not yet implemented]

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