---
source_image: page_340.png
page_number: 340
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 31.99
tokens: 7574
characters: 1917
timestamp: 2025-12-24T03:09:49.623814
finish_reason: stop
---

Чтобы подключиться к базе данных PostgreSQL, запущенной в соответствующем сервису db контейнере Docker, выполните команду docker-compose exec db, передав ей в командной строке опции psql -U postgres:

$ docker-compose exec db psql -U postgres
psql (11.4 (Debian 11.4-1.pgdg90+1))
Type "help" for help.

postgres=# 

Следуя «Flask в примерах, часть 2» (https://oreil.ly/iobKp), создаем базу данных wordcount:

$ docker-compose exec db psql -U postgres
psql (11.4 (Debian 11.4-1.pgdg90+1))
Type "help" for help.

postgres=# create database wordcount;
CREATE DATABASE

postgres=# \l

List of databases
<table>
  <tr>
    <th>Name</th>
    <th>Owner</th>
    <th>Encoding</th>
    <th>Collate</th>
    <th>Ctype</th>
    <th>Access privileges</th>
  </tr>
  <tr>
    <td>postgres</td>
    <td>postgres</td>
    <td>UTF8</td>
    <td>en_US.utf8</td>
    <td>en_US.utf8</td>
    <td>=c/postgres + postgres=CTc/postgres</td>
  </tr>
  <tr>
    <td>template0</td>
    <td>postgres</td>
    <td>UTF8</td>
    <td>en_US.utf8</td>
    <td>en_US.utf8</td>
    <td>=c/postgres + postgres=CTc/postgres</td>
  </tr>
  <tr>
    <td>template1</td>
    <td>postgres</td>
    <td>UTF8</td>
    <td>en_US.utf8</td>
    <td>en_US.utf8</td>
    <td>=c/postgres + postgres=CTc/postgres</td>
  </tr>
  <tr>
    <td>wordcount</td>
    <td>postgres</td>
    <td>UTF8</td>
    <td>en_US.utf8</td>
    <td>en_US.utf8</td>
    <td></td>
  </tr>
</table>

(4 rows)
postgres=# \q

Подключаемся к базе данных wordcount и создаем роль wordcount_dbadmin для использования нашим приложением Flask:

$ docker-compose exec db psql -U postgres wordcount
wordcount=# CREATE ROLE wordcount_dbadmin;
CREATE ROLE
wordcount=# ALTER ROLE wordcount_dbadmin LOGIN;
ALTER ROLE
wordcount=# ALTER USER wordcount_dbadmin PASSWORD 'MYPASS';
ALTER ROLE
postgres=# \q

Следующий этап — создание Dockerfile для установки всего, что необходимо для нашего приложения Flask.