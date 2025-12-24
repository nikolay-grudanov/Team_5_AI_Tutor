---
source_image: page_352.png
page_number: 352
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 40.98
tokens: 7645
characters: 2007
timestamp: 2025-12-24T03:10:22.147221
finish_reason: stop
---

Перед запуском контейнеров для сервисов, описанных в файле docker-compose.yml, нам понадобится сделать две вещи.

1. Выполнить команду docker login, чтобы извлечь из Docker Hub помещенный туда ранее образ Docker:

$ docker login

2. Задать правильное значение переменной среды DBPASS в текущей командной оболочке. Можно воспользоваться описанным в предыдущем разделе методом sops, но в этом примере мы зададим ее непосредственно в командной оболочке:

$ export DOCKER_PASS=MYPASS

Теперь запустите все необходимые для приложения сервисы с помощью команды docker-compose up -d:

$ docker-compose up -d
Pulling worker (griggheo/flask-by-example:v1)...
v1: Pulling from griggheo/flask-by-example
921b31ab772b: Already exists
1a0c422ed526: Already exists
ec0818a7bbe4: Already exists
b53197ee35ff: Already exists
8b25717b4dbf: Already exists
9be5e85cacbb: Pull complete
bd62f980b08d: Pull complete
9a89f908ad0a: Pull complete
d787e00a01aa: Pull complete
Digest: sha256:4fc554da6157b394b4a012943b649ec66c999b2acccb839562e89e34b7180e3e
Status: Downloaded newer image for griggheo/flask-by-example:v1
Creating fbe_redis_1    ... done
Creating postgres      ... done
Creating fbe_migrations_1 ... done
Creating fbe_app_1     ... done
Creating fbe_worker_1   ... done

$ docker ps
CONTAINER ID        IMAGE               COMMAND                  CREATED             STATUS              PORTS                    NAMES
f65fe9631d44        griggheo/flask-by-example:v1   "python3 manage.py r..."   5 seconds ago       Up 2 seconds         0.0.0.0:5000->5000/tcp   fbe_app_1
71fc0b24bce3        griggheo/flask-by-example:v1   "python3 worker.py"      5 seconds ago       Up 2 seconds         0.0.0.0:5000->5000/tcp   fbe_worker_1
a66d75a20a2d        redis:alpine          "docker-entrypoint.s..."   7 seconds ago       Up 5 seconds         0.0.0.0:6379->6379/tcp   fbe_redis_1
56ff97067637        postgres:11           "docker-entrypoint.s..."   7 seconds ago       Up 5 seconds         0.0.0.0:5432->5432/tcp   postgres