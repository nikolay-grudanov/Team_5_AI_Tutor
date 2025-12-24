---
source_image: page_351.png
page_number: 351
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 24.86
tokens: 7386
characters: 1595
timestamp: 2025-12-24T03:10:04.191226
finish_reason: stop
---

"deb [arch=amd64] https://download.docker.com/linux/ubuntu \
$(lsb_release -cs) \
stable"
$ sudo apt-get update
$ sudo apt-get install docker-ce docker-ce-cli containerd.io
$ sudo usermod -a -G docker ubuntu

# Скачиваем docker-compose
$ sudo curl -L \
"https://github.com/docker/compose/releases/download/1.24.1/docker-compose-\
$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
$ sudo chmod +x /usr/local/bin/docker-compose

Скопируйте на этот удаленный EC2-инстанс файл docker-compose.yml и сначала запустите сервис db, чтобы можно было создать базу данных для приложения:

$ docker-compose up -d db
Starting postgres ...
Starting postgres ... done

$ docker ps
CONTAINER ID   IMAGE       COMMAND       CREATED      STATUS      PORTS      NAMES
49fe88efdb45   postgres:11  "docker-entrypoint.s..."  29 seconds ago
    Up 3 seconds   0.0.0.0:5432->5432/tcp   postgres

Воспользуемся docker exec для выполнения команды psql -U postgres внутри работающего контейнера Docker для базы данных PostgreSQL. После появления приглашения PostgreSQL создайте базу данных wordcount и роль wordcount_dbadmin:

$ docker-compose exec db psql -U postgres
psql (11.4 (Debian 11.4-1.pgdg90+1))
Type "help" for help.

postgres=# create database wordcount;
CREATE DATABASE
postgres=# \q

$ docker exec -it 49fe88efdb45 psql -U postgres wordcount
psql (11.4 (Debian 11.4-1.pgdg90+1))
Type "help" for help.

wordcount=# CREATE ROLE wordcount_dbadmin;
CREATE ROLE
wordcount=# ALTER ROLE wordcount_dbadmin LOGIN;
ALTER ROLE
wordcount=# ALTER USER wordcount_dbadmin PASSWORD 'MYPASS';
ALTER ROLE
wordcount=# \q