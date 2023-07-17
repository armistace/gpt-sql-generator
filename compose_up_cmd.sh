
rm -rf src/dbt/intalgo/models/ai_query/*
docker-compose rm -f 
docker system prune -f
docker volume prune -f
docker volume rm intalgo-app_broker intalgo-app_zkdata
docker build -t base_image -f base.Dockerfile .
docker-compose up --remove-orphans --build -d
docker logs -f intalgo-web
