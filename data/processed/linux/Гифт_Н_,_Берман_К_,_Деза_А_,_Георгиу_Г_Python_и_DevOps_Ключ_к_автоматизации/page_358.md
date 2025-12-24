---
source_image: page_358.png
page_number: 358
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 20.43
tokens: 7376
characters: 1565
timestamp: 2025-12-24T03:10:09.725696
finish_reason: stop
---

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

Воспользуемся утилитой Kompose для преобразования этого файла в формате YAML в набор манифестов Kubernetes.

Для установки свежей версии Kompose на машине под управлением macOS сначала скачайте ее из репозитория Git (https://oreil.ly/GUqaq), переместите скачанный файл в каталог /usr/local/bin/kompose и сделайте его исполняемым. Обратите внимание на то, что при использовании для установки Kompose системы управления пакетами операционной системы (например, apt в Ubuntu или yum в Red Hat) вы рискуете получить намного более старую версию, возможно несовместимую с приведенными далее инструкциями.