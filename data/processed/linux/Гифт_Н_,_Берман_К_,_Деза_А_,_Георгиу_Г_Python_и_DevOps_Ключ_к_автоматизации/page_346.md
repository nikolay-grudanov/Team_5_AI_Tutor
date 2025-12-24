---
source_image: page_346.png
page_number: 346
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 25.20
tokens: 7472
characters: 1768
timestamp: 2025-12-24T03:09:52.279242
finish_reason: stop
---

command: "worker.py"
environment:
    APP_SETTINGS: config.ProductionConfig
    DATABASE_URL: postgresql://wordcount_dbadmin:$DBPASS@db/wordcount
    REDISTOGO_URL: redis://redis:6379
depends_on:
    - db
    - redis

Запустите сервис worker аналогично сервису redis с помощью команды docker-compose up -d:

$ docker-compose up -d worker
flask-by-example_redis_1 is up-to-date
Starting flask-by-example_worker_1 ... done

Если выполнить команду docker ps, будет отображен контейнер worker:

$ docker ps
CONTAINER ID   IMAGE           COMMAND                  CREATED         STATUS          PORTS     NAMES
72327ab33073   flask-by-example "python worker.py"      8 minutes ago   Up 14 seconds   flask-by-example_worker_1
b11b03a5bcc3   redis:alpine     "docker-entrypoint.s..." 15 minutes ago Up About a minute 0.0.0.0:6379->6379/tcp flask-by-example_redis_1
83b54ab10099   postgres:11      "docker-entrypoint.s..." 23 hours ago  Up 17 hours     0.0.0.0:5432->5432/tcp postgres

Просмотрите журналы сервиса worker с помощью команды docker-compose logs:

$ docker-compose logs worker
Attaching to flask-by-example_worker_1
20:46:34 RQ worker 'rq:worker:a66ca38275a14cac86c9b353e946a72e' started, version 1.0
20:46:34 *** Listening on default...
20:46:34 Cleaning registries for queue: default

А теперь запустите основное приложение Flask в его собственном контейнере. Создайте новый сервис app в файле docker-compose.yaml:

app:
    image: "flask-by-example:v1"
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