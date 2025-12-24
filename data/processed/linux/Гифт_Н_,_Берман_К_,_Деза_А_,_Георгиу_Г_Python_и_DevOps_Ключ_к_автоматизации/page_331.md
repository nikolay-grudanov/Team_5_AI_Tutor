---
source_image: page_331.png
page_number: 331
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 26.27
tokens: 7339
characters: 1516
timestamp: 2025-12-24T03:09:30.514897
finish_reason: stop
---

версиями библиотек Python, перестает работать на сервере предэксплуатационного тестирования или промышленной эксплуатации с другими операционными системами, например Ubuntu или Red Hat Linux.

Docker предлагает изящный выход из этой ситуации. Разработка по-прежнему выполняется на локальной машине с помощью наших любимых редакторов и наборов программных средств, но зависимости приложения упаковываются во внешний переносимый контейнер Docker.

Вот Dockerfile с описанием будущего образа Docker:

$ cat Dockerfile
FROM python:3.7.3-alpine

ENV APP_HOME /app
WORKDIR $APP_HOME

COPY requirements.txt .

RUN pip install -r requirements.txt

ENTRYPOINT [ "python" ]
CMD [ "app.py" ]

Несколько примечаний относительно того, что делает этот Dockerfile.

• Использует заранее собранный образ Docker для Python 3.7.3, основанный на дистрибутиве Alpine, благодаря которому получаются меньше по размеру образы Docker. Данный образ Docker заранее включает такие исполняемые файлы, как python и pip.
• Устанавливает с помощью pip нужные пакеты.
• Задает ENTRYPOINT и CMD. Различие между ними состоит в том, что при запуске Docker собранного из Dockerfile образа он запускает программу ENTRYPOINT, за которой следуют все указанные в CMD аргументы. В данном случае выполняется команда python app.py.

Если не указать в Dockerfile ENTRYPOINT, будет использовано следующее значение по умолчанию: /bin/sh -c.

Чтобы создать образ Docker для этого приложения, выполните команду docker build:

$ docker build -t hello-world-docker .