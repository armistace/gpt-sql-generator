
rm -rf src/dbt/intalgo/models/ai_query/*
docker-compose rm -f 
docker system prune -f 
docker-compose up --build -d
docker logs -f intalgo-web
