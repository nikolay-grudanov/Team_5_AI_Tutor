---
source_image: page_347.png
page_number: 347
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 35.28
tokens: 7717
characters: 2318
timestamp: 2025-12-24T03:10:05.844592
finish_reason: stop
---

Перенаправим порт 5000 контейнера приложения (порт по умолчанию для приложений Flask) на порт 5000 локальной машины. Передаем контейнеру приложения команду manage.py runserver --host=0.0.0.0, чтобы гарантировать, что порт 5000 виден приложению Flask должным образом внутри контейнера.

Запустите сервис app с помощью команды docker-compose up -d, выполняя в то же время sops -d для содержащего DBPASS зашифрованного файла, затем перед вызовом docker-compose отправьте с помощью команды source содержимое расшифрованного файла в виртуальную среду:

source <(sops -d environment.secrets); docker-compose up -d app
postgres is up-to-date
Recreating flask-by-example_app_1 ... done

В возвращаемом командой docker ps списке находим новый контейнер Docker, в котором работает наше приложение:

$ docker ps
CONTAINER ID   IMAGE           COMMAND                  CREATED         STATUS          PORTS                 NAMES
d99168a152f1   flask-by-example "python app.py"         3 seconds ago   Up 2 seconds    0.0.0.0:5000->5000/tcp   flask-by-example_app_1
72327ab33073   flask-by-example "python worker.py"       16 minutes ago  Up 7 minutes    flask-by-example_worker_1
b11b03a5bcc3   redis:alpine     "docker-entrypoint.s..." 23 minutes ago  Up 9 minutes    0.0.0.0:6379->6379/tcp   flask-by-example_redis_1
83b54ab10099   postgres:11      "docker-entrypoint.s..." 23 hours ago   Up 17 hours     0.0.0.0:5432->5432/tcp   postgres

Просматриваем журналы контейнера приложения с помощью команды docker-compose logs:

$ docker-compose logs app
Attaching to flask-by-example_app_1
app_1        * Running on http://0.0.0.0:5000/ (Press CTRL+C to quit)

Выполнение команды docker-compose logs без аргументов позволяет просмотреть журналы всех сервисов, описанных в файле docker-compose.yaml:

$ docker-compose logs
Attaching to flask-by-example_app_1,
flask-by-example_worker_1,
flask-by-example_migrations_1,
flask-by-example_redis_1,
postgres
1:C 12 Jul 2019 20:17:12.966 # o000o000o000o Redis запускается o000o000o000o
1:C 12 Jul 2019 20:17:12.966 # Redis version=5.0.5, bits=64, commit=00000000,
modified=0, pid=1, just started
1:C 12 Jul 2019 20:17:12.966 # Предупреждение: файл конфигурации не указан, используем настройки по умолчанию. Для указания файла конфигурации примените команду redis-server /path/to/redis.conf