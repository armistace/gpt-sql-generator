FROM python:3.10

WORKDIR /intalgo

COPY requirements.txt .

#ADD src src/

RUN pip install --upgrade pip

RUN pip --default-timeout=1000 install -r requirements.txt

ENV FLASK_ENV development
ENV FLASK_DEBUG 1

ENTRYPOINT ["python", "src/flask/intalgo_web.py"]
