FROM python:3.10 as base_image

WORKDIR /intalgo

COPY requirements.txt .

RUN apt-get update -y && apt-get upgrade -y && apt-get install -y libsasl2-dev python-dev libldap2-dev libssl-dev

RUN pip install --upgrade pip

RUN pip --default-timeout=1000 install -r requirements.txt

