---
source_image: page_392.png
page_number: 392
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 16.32
tokens: 6375
characters: 1397
timestamp: 2025-12-24T04:04:28.675077
finish_reason: stop
---

Любой последующий вывод после строчки ** Potential problems described below ** указывает на ошибки конфигурации или ошибки установки.

Указываем наш домен (замените домен своим доменом):
bbb-conf --setip bbb.example.com

Современные браузеры запрещают передачу видео и звука по открытым каналам, для нормальной работы нам нужен сертификат для работы https. проще всего его взять у Let's Encrypt. Хотя мы уже рассматривали, как это сделать, для полноты руководства рассмотрим еще раз в контексте настройки BBB.

Установим инструмент для работы с Let's Encrypt:

$ sudo add-apt-repository ppa:certbot/certbot
$ sudo apt-get install certbot

Генерируем набор данных:
$ sudo mkdir -p /etc/nginx/ssl
$ sudo openssl dhparam -out /etc/nginx/ssl/dhp-4096.pem 4096

На слабом компьютере выполнение данных команд может занять достаточно много времени.

Запрашиваем сертификат (укажите собственное доменное имя):

$ sudo certbot --webroot -w /var/www/bigbluebutton-default/ -d bigbluebutton.example.com certonly

В результате будут сгенерированы следующие файлы:

$ ls /etc/letsencrypt/live/bigbluebutton.example.com/
cert.pem chain.pem fullchain.pem privkey.pem

Теперь осталось отредактировать конфигурацию веб-сервера. Для упрощения этой главы будем считать, что мы используем nginx. Откройте файл nginx /etc/nginx/sites-available/bigbluebutton (это файл сайта для BBB) и добавьте в него следующие строки: