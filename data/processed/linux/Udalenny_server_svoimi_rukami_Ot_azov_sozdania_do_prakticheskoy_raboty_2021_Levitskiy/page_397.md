---
source_image: page_397.png
page_number: 397
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 10.92
tokens: 6323
characters: 1260
timestamp: 2025-12-24T04:04:30.950194
finish_reason: stop
---

Редактируем .env файл. Установите SECRET_KEY_BASE опцию на этот ключ.

Просмотрим секретный ключ bigbluebutton:

$ sudo bbb-conf -secret

Отредактируем .env файл, установите BIGBLUEBUTTON_ENDPOINT URL-адрес и установите BIGBLUEBUTTON_SECRET секретный ключ.

Проверяем настройку

docker run --rm --env-file .env bigbluebutton/greenlight:v2 bundle exec rake conf:check

Добавьте виртуальный каталог в nginx, Конфигурация Nginx для этого подкаталога хранится в образе Greenlight.

Чтобы добавить этот файл конфигурации на ваш сервер BigBlueButton, запустите:

docker run --rm bigbluebutton/greenlight:v2 cat ./greenlight.nginx | sudo tee /etc/bigbluebutton/nginx/greenlight.nginx

Поскольку на корневой странице ничего не будет, настроим перенаправление на Greenlight. Для этого добавим следующую запись в нижней части /etc/nginx/sites-available/bigbluebutton перед последним } символом.

location = / {
    return 307 /b;
}

Выполните команду:

docker run --rm bigbluebutton/greenlight:v2 cat ./docker-compose.yml > docker-compose.yml

Сгенерируем случайный пароль для базы данных:

export pass=$(openssl rand -hex 8); sed -i 's/POSTGRES_PASSWORD=password/POSTGRES_PASSWORD='$pass'/g' docker-compose.yml;sed -i 's/DB_PASSWORD=password/DB_PASSWORD='$pass'/g' .env