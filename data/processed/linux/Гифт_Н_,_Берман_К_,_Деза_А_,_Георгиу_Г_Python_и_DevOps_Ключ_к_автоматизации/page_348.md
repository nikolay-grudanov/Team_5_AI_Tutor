---
source_image: page_348.png
page_number: 348
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 40.24
tokens: 7827
characters: 2409
timestamp: 2025-12-24T03:10:12.623074
finish_reason: stop
---

1:M 12 Jul 2019 20:17:12.967 * Запускаем mode=standalone, port=6379.
1:M 12 Jul 2019 20:17:12.967 # Предупреждение: невозможно воплотить значение 511 настройки очереди соединений TCP, поскольку параметр /proc/sys/net/core/somaxconn установлен в более низкое значение 128.
1:M 12 Jul 2019 20:17:12.967 # Сервер инициализирован
1:M 12 Jul 2019 20:17:12.967 * Готов к приему соединений
app_1      | * Running on http://0.0.0.0:5000/ (Press CTRL+C to quit)
postgres   | 2019-07-12 22:15:19.193 UTC [1]
LOG: listening on IPv4 address "0.0.0.0", port 5432
postgres   | 2019-07-12 22:15:19.194 UTC [1]
LOG: listening on IPv6 address "::", port 5432
postgres   | 2019-07-12 22:15:19.199 UTC [1]
LOG: listening on Unix socket "/var/run/postgresql/.s.PGSQL.5432"
postgres   | 2019-07-12 22:15:19.214 UTC [22]
LOG: database system was shut down at 2019-07-12 22:15:09 UTC
postgres   | 2019-07-12 22:15:19.225 UTC [1]
LOG: database system is ready to accept connections
migrations_1 | INFO [alembic.runtime.migration] Context impl PostgresqlImpl.
migrations_1 | INFO [alembic.runtime.migration] Will assume transactional DDL.
worker_1   | 22:15:20
RQ worker 'rq:worker:2edb6a54f30a4aae8a8ca2f4a9850303' started, version 1.0
worker_1   | 22:15:20 *** Listening on default...
worker_1   | 22:15:20 Cleaning registries for queue: default

Последний этап — тестирование приложения. Зайдите в браузере по адресу http://127.0.0.1:5000 и введите python.org в поле URL. При этом приложение отправит процессу-исполнителю задание на выполнение функции count_and_save_words для домашней страницы сайта python.org. Приложение будет периодически запрашивать у задания результаты, а по завершении отобразит на домашней странице частотность слов.

Чтобы повысить переносимость файла docker-compose.yaml, помещаем образ Docker flask-by-example в Docker Hub и ссылаемся там на него в разделах сервисов app и worker файла docker-compose.yaml.

Помечаем локальный образ Docker flask-by-example:v1 тегом, состоящим из названия, которому предшествует имя пользователя Docker Hub, после чего помещаем образ, только что получивший тег, в Docker Hub:

$ docker tag flask-by-example:v1 griggheo/flask-by-example:v1
$ docker push griggheo/flask-by-example:v1

Вносим в файл docker-compose.yaml изменения, ссылаясь на новый образ Docker. Вот окончательная версия файла docker-compose.yaml:

$ cat docker-compose.yaml
version: "3"
services:
    app: