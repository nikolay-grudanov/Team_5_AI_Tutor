---
source_image: page_338.png
page_number: 338
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 20.26
tokens: 7364
characters: 1640
timestamp: 2025-12-24T03:09:37.680204
finish_reason: stop
---

Начнем с клонирования репозитория «Flask в примерах» с GitHub (https://oreil.ly/M-pvc):

$ git clone https://github.com/realpython/flask-by-example.git

Для запуска нескольких контейнеров Docker, соответствующих различным частям приложения, применим команду compose. При использовании Compose описание и настройка составляющих приложение сервисов производятся в файле YAML, после чего эти сервисы, работающие в контейнерах Docker, создаются, запускаются и останавливаются с помощью утилиты командной строки docker-compose.

Первая зависимость для нашего примера приложения — PostgreSQL, как описывается в части 2 этого руководства (https://oreil.ly/iobKp).

Вот как можно описать внутри файла docker-compose.yaml запуск PostgreSQL в контейнере Docker:

$ cat docker-compose.yaml
version: "3"
services:
  db:
    image: "postgres:11"
    container_name: "postgres"
    ports:
      - "5432:5432"
    volumes:
      - dbdata:/var/lib/postgresql/data
volumes:
  dbdata:

Отметим несколько особенностей этого файла.

● В нем описывается сервис db, в основе которого лежит опубликованный в Docker Hub образ контейнера postgres:11.
● Задается соответствие локального порта 5432 порту 5432 контейнера.
● Задается том Docker для каталога, в котором PostgreSQL будет хранить свои данные, — /var/lib/postgresql/data. Благодаря этому хранимые в PostgreSQL данные не теряются при перезапуске контейнера.

Утилита docker-compose не входит в состав движка Docker, так что ее необходимо установить отдельно. Инструкции по ее установке на различных операционных системах вы можете найти в официальной документации (https://docs.docker.com/compose/install).