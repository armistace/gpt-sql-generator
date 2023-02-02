FROM python:3.11

WORKDIR /intalgo

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY src/ .


