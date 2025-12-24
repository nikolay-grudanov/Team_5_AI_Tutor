---
source_image: page_345.png
page_number: 345
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 34.53
tokens: 7733
characters: 2139
timestamp: 2025-12-24T03:10:01.563326
finish_reason: stop
---

Часть 4 (https://oreil.ly/UY2yw) руководства «Flask в примерах» описывает развертывание процесса-исполнителя Python на основе Python RQ, взаимодействующего с экземпляром хранилища данных Redis.

Прежде всего необходимо запустить Redis. Добавьте его описание как сервиса redis в файл docker-compose.yaml и убедитесь, что его внутренний порт 6379 перенаправляется на порт 6379 локальной операционной системы:

redis:
    image: "redis:alpine"
    ports:
        - "6379:6379"

Запустите сервис redis, указав его в качестве аргумента команды docker-compose up -d:

$ docker-compose up -d redis
Starting flask-by-example_redis_1 ... done

Выполните команду docker ps, чтобы посмотреть на новый контейнер Docker, основанный на образе redis:alpine:

$ docker ps
CONTAINER ID   IMAGE       COMMAND   CREATED   STATUS    PORTS     NAMES
a1555cc372d6   redis:alpine "docker-entrypoint.s..." 3 seconds ago   Up 1 second   0.0.0.0:6379->6379/tcp   flask-by-example_redis_1
83b54ab10099   postgres:11  "docker-entrypoint.s..." 22 hours ago   Up 16 hours   0.0.0.0:5432->5432/tcp   postgres

Просмотрите журналы сервиса redis с помощью команды docker-compose logs:

$ docker-compose logs redis
Attaching to flask-by-example_redis_1
1:C 12 Jul 2019 20:17:12.966 # o000o000o000o Redis запускается o000o000o000o
1:C 12 Jul 2019 20:17:12.966 # Redis version=5.0.5, bits=64, commit=00000000, modified=0, pid=1, just started
1:C 12 Jul 2019 20:17:12.966 # Предупреждение: файл конфигурации не указан, используем настройки по умолчанию. Для указания файла конфигурации примените команду redis-server /path/to/redis.conf
1:M 12 Jul 2019 20:17:12.967 * Запускаем mode=standalone, port=6379.
1:M 12 Jul 2019 20:17:12.967 # Предупреждение: невозможно воплотить значение 511 настройки очереди соединений TCP, поскольку параметр /proc/sys/net/core/somaxconn установлен в более низкое значение 128.
1:M 12 Jul 2019 20:17:12.967 # Сервер инициализирован
1:M 12 Jul 2019 20:17:12.967 * Готов к приему соединений

Следующий шаг — создание сервиса worker для процесса-исполнителя на основе Python RQ в файле docker-compose.yaml:

worker:
    image: "flask-by-example:v1"