---
source_image: page_396.png
page_number: 396
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 10.70
tokens: 6298
characters: 1198
timestamp: 2025-12-24T04:04:30.679652
finish_reason: stop
---

Перезапускаем все компоненты bigbluebutton

$ sudo bbb-conf -restart

Дальше нам понадобится установить панель управления greenlight. Установим docker и docker-compose

$ curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -
$ sudo add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable"
$ sudo apt update
$ sudo apt install docker-ce docker-ce-cli containerd.io
$ sudo curl -L "https://github.com/docker/compose/releases/download/1.25.4/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
$ sudo chmod +x /usr/local/bin/docker-compose
$ sudo ln -s /usr/local/bin/docker-compose /usr/bin/docker-compose

Примечание. Greenlight - приложение на Ruby on Rails, предоставляющее простой интерфейс для пользователей, чтобы создавать комнаты, начинать конференции, управлять записями конференций.

Создайте каталог Greenlight для его конфигурации

mkdir ~/greenlight && cd ~/greenlight

Сгенерируйте образ Greenlight

docker run --rm bigbluebutton/greenlight:v2 cat ./sample.env > .env

docker нужен секретный ключ для запуска, генерируем его:

docker run --rm bigbluebutton/greenlight:v2 bundle exec rake secret