---
source_image: page_028.png
page_number: 28
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 29.13
tokens: 8338
characters: 1392
timestamp: 2025-12-24T02:16:35.058526
finish_reason: stop
---

Кроме того, использование Dockerfile и файла docker-compose избавляет от необходимости загружать образы наших приложений и делиться ими. Новые версии наших приложений можно создавать из файла Dockerfile и развертывать с помощью файла docker-compose. Образы приложений также можно хранить и извлекать из Docker Hub. Это известно, как операция толкания и вытягивания.

Чтобы начать настройку, загрузите и установите Docker с https://docs.docker.com/install.

Dockerfile

Dockerfile содержит инструкции о том, как должен быть создан образ нашего приложения. Ниже приведен пример Dockerfile:

FROM PYTHON:3.8
# Set working directory to /usr/src/app
WORKDIR /usr/src/app
# Copy the contents of the current local directory into the container's working directory
ADD . /usr/src/app
# Run a command
CMD ["python", "hello.py"]

Далее мы создадим образ контейнера приложения и назовем getting_started следующим образом:

$ docker build -t getting_started .

Если Dockerfile отсутствует в каталоге, где запускается команда, путь к Dockerfile должен быть правильно добавлен следующим образом:

$ docker build -t api api/Dockerfile

Образ контейнера можно запустить с помощью следующей команды:

$ docker run getting-started

Docker — эффективный инструмент для контейнеризации. Мы рассмотрели только основные операции, и мы изучим больше практических операций в Главе 9. Развертывание приложений FastAPI.