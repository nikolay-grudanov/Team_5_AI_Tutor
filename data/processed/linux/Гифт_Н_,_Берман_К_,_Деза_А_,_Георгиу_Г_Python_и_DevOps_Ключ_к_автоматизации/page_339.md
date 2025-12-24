---
source_image: page_339.png
page_number: 339
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 31.67
tokens: 7554
characters: 1888
timestamp: 2025-12-24T03:09:49.253998
finish_reason: stop
---

Для загрузки описанного в файле docker-compose.yml сервиса db выполните команду docker-compose up -d db, которая запустит в фоновом режиме (флаг -d) контейнер Docker для сервиса db¹:

$ docker-compose up -d db
Creating postgres ... done

Загляните в журналы сервиса db с помощью команды docker-compose logs db:

$ docker-compose logs db
Creating volume "flask-by-example_dbdata" with default driver
Pulling db (postgres:11)...
11: Pulling from library/postgres
Creating postgres ... done
Attaching to postgres
postgres | PostgreSQL init process complete; ready for start up.
postgres |
postgres | 2019-07-11 21:50:20.987 UTC [1]
LOG:  listening on IPv4 address "0.0.0.0", port 5432
postgres | 2019-07-11 21:50:20.987 UTC [1]
LOG:  listening on IPv6 address ":::", port 5432
postgres | 2019-07-11 21:50:20.993 UTC [1]
LOG:  listening on Unix socket "/var/run/postgresql/.s.PGSQL.5432"
postgres | 2019-07-11 21:50:21.009 UTC [51]
LOG:  database system was shut down at 2019-07-11 21:50:20 UTC
postgres | 2019-07-11 21:50:21.014 UTC [1]
LOG:  database system is ready to accept connections

При выполнении команды docker ps вы увидите контейнер, в котором запущена база данных PostgreSQL:

$ docker ps
dCONTAINER ID   IMAGE       COMMAND       CREATED      STATUS      PORTS      NAMES
83b54ab10099    postgres:11  "docker-entrypoint.s..."  3 minutes ago  Up 3 minutes  0.0.0.0:5432->5432/tcp  postgres

А выполнение команды docker volume ls продемонстрирует том dbdata Docker, смонтированный к каталогу /var/lib/postgresql/data PostgreSQL:

$ docker volume ls | grep dbdata
local        flask-by-example_dbdata

¹ Чтобы все работало, мне понадобилось также задать общий пароль для PostgreSQL либо настроить ее использование без пароля, что можно сделать, например, внеся в вышеупомянутый файл docker-compose.yml следующее:
environment:
    POSTGRES_HOST_AUTH_METHOD: "trust". — Примеч. пер.