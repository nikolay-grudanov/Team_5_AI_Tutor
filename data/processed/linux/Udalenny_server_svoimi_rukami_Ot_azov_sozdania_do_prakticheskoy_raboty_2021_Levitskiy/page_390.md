---
source_image: page_390.png
page_number: 390
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 17.23
tokens: 6355
characters: 1227
timestamp: 2025-12-24T04:04:26.954338
finish_reason: stop
---

Для BigBlueButton необходимы два приложения: ffmpeg (создание записей) и yq (обновление файлов YAML). Версия по умолчанию ffmpeg в Ubuntu 16.04 устарела и yq не существует в репозиториях по умолчанию.

Поэтому перед установкой BigBlueButton необходимо добавить следующие личные архивы пакетов (PPA) на сервер, чтобы убедиться, что установлены правильные версии.

$ sudo add-apt-repository ppa:bigbluebutton/support -y
$ sudo add-apt-repository ppa:rmescandon/yq -y

Затем обновляем сервер до последних пакетов.

$ sudo apt update
$ sudo apt full-upgrade

HTML5-клиент BigBlueButton использует MongoDB, устанавливаем его:

$ wget -qO - https://www.mongodb.org/static/pgp/server-3.4.asc | sudo apt-key add -
$ echo "deb [ arch=amd64,arm64 ] http://repo.mongodb.org/apt/ubuntu xenial/mongodb-org/3.4 multiverse" | sudo tee /etc/apt/sources.list.d/mongodb-org-3.4.list
$ sudo apt-get update
$ sudo apt-get install -y mongodb-org curl

HTML5-клиент BigBlueButton требует наличия сервера nodejs, установим его:

$ curl -sL https://deb.nodesource.com/setup_8.x | sudo -E bash -
$ sudo apt-get install -y nodejs

Скачиваем и добавляем ключ репозитория BigBlueButton. Поскольку Роскомнадзор закрыл доступ до репозитория, используем tor: