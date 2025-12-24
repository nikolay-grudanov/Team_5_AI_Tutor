---
source_image: page_192.png
page_number: 192
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 21.51
tokens: 8175
characters: 753
timestamp: 2025-12-24T02:20:45.234694
finish_reason: stop
---

Содержимое файла манифеста docker-compose будет следующим:

docker-compose.yml

version: "3"

services:
    api:
        build: .
        image: event-planner-api:latest
        ports:
            - "8080:8080"
        env_file:
            - .env.prod

    database:
        image: mongo
        ports:
            - "27017"
        volumes:
            - data:/data/db

volumes:
    data:

В разделе services у нас есть служба api и служба database. В службе api применяется следующий набор инструкций:

• Поле build указывает Docker на создание образа event-planner-api:latest для службы api из файла Dockerfile, расположенного в текущем каталоге, обозначенном ..

• Порт 8080 открыт из контейнера, чтобы мы могли получить доступ к службе через HTTP.