---
source_image: page_341.png
page_number: 341
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 23.20
tokens: 7437
characters: 1719
timestamp: 2025-12-24T03:09:41.119669
finish_reason: stop
---

Внесите в файл requirements.txt следующие изменения:

• поменяйте версию пакета psycopg2 с 2.6.1 на 2.7 для поддержки PostgreSQL 11;
• поменяйте версию пакета redis с 2.10.5 на 3.2.1 для улучшения поддержки Python 3.7;
• поменяйте версию пакета rq с 0.5.6 на 1.0 для улучшения поддержки Python 3.7.

Вот как выглядит теперь Dockerfile:

$ cat Dockerfile
FROM python:3.7.3-alpine

ENV APP_HOME /app
WORKDIR $APP_HOME

COPY requirements.txt .

RUN \
apk add --no-cache postgresql-libs && \
apk add --no-cache --virtual .build-deps gcc musl-dev postgresql-dev && \
python3 -m pip install -r requirements.txt --no-cache-dir && \
apk --purge del .build-deps

COPY . .

ENTRYPOINT [ "python" ]
CMD ["app.py"]

Между этим Dockerfile и использованной в первом примере версией hello-world-docker есть важное различие. Здесь содержимое текущего каталога, в котором находятся файлы приложения, копируется в образ Docker, чтобы проиллюстрировать сценарий, отличный от технологического процесса разработки, показанного ранее. В данном случае нас больше интересует максимально переносимый вариант запуска приложения, например, в среде предэксплуатационного тестирования или промышленной эксплуатации, где не нужно модифицировать файлы приложения через смонтированные тома, как в сценарии разработки. Для целей разработки docker-compose можно использовать со смонтированными локально томами, но здесь нас интересует переносимость контейнеров Docker между различными средами, например разработки, предэксплуатационного тестирования и промышленной эксплуатации.

Выполните команду docker build -t flask-by-example:v1 . для сборки локального образа Docker. Выводимые этой командой результаты приводить не станем из-за их большого объема.