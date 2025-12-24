---
source_image: page_342.png
page_number: 342
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 23.28
tokens: 7440
characters: 1877
timestamp: 2025-12-24T03:09:41.222023
finish_reason: stop
---

Следующий шаг из руководства «Flask в примерах» — запуск миграций Flask.

Опишите в файле docker-compose.yaml новый сервис migrations, задайте для него image, command, переменные среды (environment) и укажите, что для него требуется, чтобы сервис db был запущен и работал:

$ cat docker-compose.yaml
version: "3"
services:
  migrations:
    image: "flask-by-example:v1"
    command: "manage.py db upgrade"
    environment:
      APP_SETTINGS: config.ProductionConfig
      DATABASE_URL: postgresql://wordcount_dbadmin:$DBPASS@db/wordcount
    depends_on:
      - db
  db:
    image: "postgres:11"
    container_name: "postgres"
    ports:
      - "5432:5432"
    volumes:
      - dbdata:/var/lib/postgresql/data
volumes:
  dbdata:

В переменной DATABASE_URL в качестве хоста для базы данных PostgreSQL указано название db, поскольку именно оно задано в качестве названия сервиса в файле docker-compose.yaml и утилита docker-compose умеет связывать одно с другим посредством создания наложенной сети, в которой все описанные в файле docker-compose.yaml сервисы могут взаимодействовать друг с другом по названиям. См. подробности в справочном руководстве по утилите docker-compose (https://oreil.ly/Io80N).

Определение переменной DATABASE_URL ссылается на другую переменную — DBPASS, вместо того чтобы жестко «зашифровать» пароль пользователя wordcount_dbadmin. Обычно файл docker-compose.yaml вносится в систему контроля версий, и рекомендуется не отправлять в GitHub секретные данные, такие как учетные данные БД. Вместо этого для работы с файлами, содержащими секретные данные, стоит задействовать утилиты шифрования, например sops (https://github.com/mozilla/sops).

Вот пример создания с помощью sops зашифрованного посредством PGP файла.

Вначале установите gpg на macOS с помощью команды brew install gpg, после чего сгенерируйте новый ключ PGP с пустой парольной фразой: