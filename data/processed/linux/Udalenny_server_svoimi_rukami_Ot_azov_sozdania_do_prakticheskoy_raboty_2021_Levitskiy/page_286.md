---
source_image: page_286.png
page_number: 286
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 15.63
tokens: 6223
characters: 812
timestamp: 2025-12-24T04:02:20.571192
finish_reason: stop
---

domains = example.com

# размер ключа
rsa-key-size = 2048 # или 4096

# сервер сертификации
server = https://acme-v01.api.letsencrypt.org/directory

# адрес, на который будут приходить напоминание об обновлении
email = my-email

# отключаем ncurses UI
text = True

# задаем путь к каталогу .well-known (см. выше)
authenticator = webroot
webroot-path = /var/www/shop/

16.4.4. Заказ сертификата

Настало время запросить сам сертификат. Во второй команде вам нужно заменить точное имя файла конфигурации:

cd /opt/letsencrypt
$ ./certbot-auto --config /etc/letsencrypt/configs/example.com.conf certonly

В результате в каталоге /etc/letsencrypt/live/<название сайта>/ будет сгенерировано два файла — fullchain.pem и privkey.pem. Их и нужно будет прописать в конфигурационном файле сервера, как было показано ранее.