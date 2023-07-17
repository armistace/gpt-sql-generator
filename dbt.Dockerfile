FROM base_image as dbt

COPY dbt_profile/profiles.yml /root/.dbt/

WORKDIR /intalgo

COPY requirements.txt .

COPY entrypoint.sh .

