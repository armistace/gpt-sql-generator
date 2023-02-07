FROM python:3.10

COPY dbt_profile/profiles.yml /root/.dbt/

WORKDIR /intalgo

COPY requirements.txt .

COPY entrypoint.sh .

ADD src src/

ADD data /data

RUN pip install -r requirements.txt

ENTRYPOINT ./entrypoint.sh
