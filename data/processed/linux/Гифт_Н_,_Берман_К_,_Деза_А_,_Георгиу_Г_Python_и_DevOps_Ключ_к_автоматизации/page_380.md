---
source_image: page_380.png
page_number: 380
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 34.77
tokens: 7523
characters: 1566
timestamp: 2025-12-24T03:10:56.964787
finish_reason: stop
---

$ kubectl logs db-6b4fbb57d9-8h978
PostgreSQL init process complete; ready for start up.

2019-08-03 18:12:01.108 UTC [1]
LOG:  listening on IPv4 address "0.0.0.0", port 5432
2019-08-03 18:12:01.108 UTC [1]
LOG:  listening on IPv6 address "::", port 5432
2019-08-03 18:12:01.114 UTC [1]
LOG:  listening on Unix socket "/var/run/postgresql/.s.PGSQL.5432"
2019-08-03 18:12:01.135 UTC [50]
LOG:  database system was shut down at 2019-08-03 18:12:01 UTC
2019-08-03 18:12:01.141 UTC [1]
LOG:  database system is ready to accept connections

Создаем базу данных wordcount и роль wordcount_dbadmin:

$ kubectl exec -it db-6b4fbb57d9-8h978 -- psql -U postgres
psql (11.4 (Debian 11.4-1.pgdg90+1))
Type "help" for help.

postgres=# create database wordcount;
CREATE DATABASE
postgres=# \q

$ kubectl exec -it db-6b4fbb57d9-8h978 -- psql -U postgres wordcount
psql (11.4 (Debian 11.4-1.pgdg90+1))
Type "help" for help.

wordcount=# CREATE ROLE wordcount_dbadmin;
CREATE ROLE
wordcount=# ALTER ROLE wordcount_dbadmin LOGIN;
ALTER ROLE
wordcount=# ALTER USER wordcount_dbadmin PASSWORD 'MYNEWPASS';
ALTER ROLE
wordcount=# \q

Создаем сервис db:

$ kubectl create -f db-service.yaml
service/db created

$ kubectl describe service db
Name:                db
Namespace:           default
Labels:              io.kompose.service=db
Annotations:         kompose.cmd: kompose convert
                     kompose.version: 1.16.0 (0c01309)
Selector:            io.kompose.service=db
Type:                ClusterIP
IP:                  10.59.241.181
Port:                5432   5432/TCP