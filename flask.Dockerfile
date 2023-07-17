FROM base_image as flask

COPY dbt_profile/profiles.yml /root/.dbt/

COPY requirements.txt .

COPY entrypoint.sh .

ENV FLASK_ENV development
ENV FLASK_DEBUG 1

ENTRYPOINT ["python", "src/flask/intalgo_web.py"]
