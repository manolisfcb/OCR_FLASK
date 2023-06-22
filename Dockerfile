FROM  python:3.10.0-alpine3.15
WORKDIR /app


COPY . /app

RUN apt-get update && apt-get install -y \
    tesseract-ocr \
    tesseract-ocr-por
RUN pip install -r requirements.txt

COPY src .
EXPOSE 5001


CMD [ "flask", "run","--host","0.0.0.0","--port","5001"]
