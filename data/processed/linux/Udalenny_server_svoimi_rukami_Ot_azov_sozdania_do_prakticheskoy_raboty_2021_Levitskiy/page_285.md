---
source_image: page_285.png
page_number: 285
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 21.90
tokens: 6322
characters: 1147
timestamp: 2025-12-24T04:02:26.517770
finish_reason: stop
---

16.4.1. Установка клиента Let's Encrypt

Установим клиент с помощью команды:

sudo git clone https://github.com/certbot/certbot /opt/letsencrypt

Если git не установлен, то сначала нужно установить его, а потом уже устанавливает клиент для Let's Encrypt (далее certbot). Файлы будут загружены в каталог /opt/letsencrypt.

16.4.2. Каталог webroot-path/.well-known/acme-challenge/

Данный каталог позволяет серверу Let's Encrypt убедиться, что ваш сайт пытается получить бесплатный SSL-сертификат. Каталог нужно создавать в корне веб-сервера. Например, если корень у вас /var/www/shop, то в нем и нужно создать нужный каталог:

cd /var/www/shop
mkdir .well-known
mkdir .well-known/acme-challenge
find . -type d -exec chown www-data:www-data {} \;

16.4.3. Файл конфигурации

Теперь нужно создать файл конфигурации для вашего домена. Если ваш домен называется example.com, то файл будет называться /etc/letsencrypt/configs/example.com.conf. Содержимое файла:

# ваш домен (хотя и можно создать один сертификат для нескольких доменов
# мы рекомендуем создавать отдельные сертификаты и, следовательно, отдельные
# файлы конфигурации для разных доменов)