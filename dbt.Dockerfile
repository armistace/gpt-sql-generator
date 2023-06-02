FROM python:3.10

COPY dbt_profile/profiles.yml /root/.dbt/

WORKDIR /intalgo

COPY requirements.txt .

COPY entrypoint.sh .

RUN pip install --upgrade pip

RUN pip --default-timeout=1000 install -r requirements.txt
#ENTRYPOINT ./entrypoint.sh
