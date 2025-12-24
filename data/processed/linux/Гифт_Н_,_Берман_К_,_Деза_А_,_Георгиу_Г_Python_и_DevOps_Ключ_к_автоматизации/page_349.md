---
source_image: page_349.png
page_number: 349
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 22.80
tokens: 7320
characters: 1384
timestamp: 2025-12-24T03:09:58.318752
finish_reason: stop
---

image: "griggheo/flask-by-example:v1"
command: "manage.py runserver --host=0.0.0.0"
ports:
    - "5000:5000"
environment:
    APP_SETTINGS: config.ProductionConfig
    DATABASE_URL: postgresql://wordcount_dbadmin:$DBPASS@db/wordcount
    REDISTOGO_URL: redis://redis:6379
depends_on:
    - db
    - redis
worker:
    image: "griggheo/flask-by-example:v1"
    command: "worker.py"
    environment:
        APP_SETTINGS: config.ProductionConfig
        DATABASE_URL: postgresql://wordcount_dbadmin:$DBPASS@db/wordcount
        REDISTOGO_URL: redis://redis:6379
depends_on:
    - db
    - redis
migrations:
    image: "griggheo/flask-by-example:v1"
    command: "manage.py db upgrade"
    environment:
        APP_SETTINGS: config.ProductionConfig
        DATABASE_URL: postgresql://wordcount_dbadmin:$DBPASS@db/wordcount
depends_on:
    - db
db:
    image: "postgres:11"
    container_name: "postgres"
    ports:
        - "5432:5432"
    volumes:
        - dbdata:/var/lib/postgresql/data
redis:
    image: "redis:alpine"
    ports:
        - "6379:6379"
volumes:
    dbdata:

Для перезапуска локальных контейнеров Docker выполните команду docker-compose down, а затем docker-compose up -d:

$ docker-compose down
Stopping flask-by-example_worker_1 ... done
Stopping flask-by-example_app_1   ... done
Stopping flask-by-example_redis_1 ... done
Stopping postgres                ... done