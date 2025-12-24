---
source_image: page_332.png
page_number: 332
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 30.81
tokens: 7570
characters: 2080
timestamp: 2025-12-24T03:09:39.288789
finish_reason: stop
---

Чтобы проверить, что образ Docker был сохранен на локальной машине, выполните команду docker images с названием образа:

$ docker images hello-world-docker
REPOSITORY           TAG      IMAGE ID       CREATED             SIZE
hello-world-docker   latest   dbd84c229002   2 minutes ago      97.7MB

Для запуска образа Docker как контейнера Docker предназначена команда docker run:

$ docker run --rm -d -v `pwd`:/app -p 5000:5000 hello-world-docker c879295baa26d9dff1473460bab810cbf6071c53183890232971d1b473910602

Несколько примечаний относительно аргументов команды docker run.

• Аргумент --rm указывает серверу Docker на необходимость удалить этот контейнер по завершении его выполнения. Удобная возможность для предотвращения захламления локальной файловой системы.
• Аргумент -d указывает серверу Docker, что этот контейнер нужно запустить в фоновом режиме.
• С помощью аргумента -v текущий каталог (pwd) привязывается к каталогу /app внутри контейнера Docker, что важно для технологического процесса локальной разработки, поскольку позволяет редактировать файлы приложения на локальной машине с автоматической перезагрузкой их сервером для разработки Flask, запущенным внутри контейнера.
• Аргумент -p 5000:5000 привязывает первый (локальный) из указанных портов (5000) ко второму порту (5000) внутри контейнера.

Вывести список запущенных контейнеров можно с помощью команды docker ps. Запомните идентификатор контейнера, он будет использоваться в других наших командах docker:

$ docker ps
CONTAINER ID   IMAGE                                      COMMAND                  CREATED             STATUS              NAMES
c879295baa26   hello-world-docker:latest   "python app.py"   4 seconds ago     Up 2 seconds        flamboyant_germain

Просмотреть журналы для конкретного контейнера можно с помощью команды docker logs, указав название или идентификатор этого контейнера:

$ docker logs c879295baa26
* Serving Flask app "app" (lazy loading)
* Running on http://0.0.0.0:5000/ (Press CTRL+C to quit)
* Restarting with stat
* Debugger is active!
* Debugger PIN: 647-161-014