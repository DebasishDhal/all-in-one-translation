FROM python:3.11-slim

WORKDIR /app

RUN apt-get update && \
    apt-get install -y tesseract-ocr && \
    apt-get install -y tesseract-ocr-* && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# RUN apt-get install -y ffmpeg \
#     && apt-get install -y libsndfile1

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 7860

CMD ["python", "app.py"]
