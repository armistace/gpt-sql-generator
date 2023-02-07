FROM python:3.10

WORKDIR /intalgo

COPY requirements.txt .

ADD src src/

RUN pip install -r requirements.txt

ENTRYPOINT ["python", "src/flask/intalgo_web.py"]