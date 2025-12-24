---
source_image: page_323.png
page_number: 323
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 18.90
tokens: 6360
characters: 1378
timestamp: 2025-12-24T04:03:06.860809
finish_reason: stop
---

Удаленный сервер своими руками

mod_gzip_item_include mime ^text/.*
mod_gzip_item_include mime ^application/x-javascript.*
mod_gzip_item_exclude mime ^image/.*
mod_gzip_item_exclude rspheader ^Content-Encoding:.*gzip.*
</ifModule>
</Directory>

Для включения кэширования можно вынести конфигурацию за пределы основного файла и создать файл .htaccess в корневом каталоге документов. Содержимое этого файла будет следующим:

# кеширование в браузере на стороне пользователя
<IfModule mod_expires.c>
#Включаем поддержку директивы Expires
ExpiresActive On
# Задаем время для хранения файлов (картинок) в кэше для каждого типа
ExpiresDefault "access 7 days"
ExpiresByType application/javascript "access plus 1 year"
ExpiresByType text/javascript "access plus 1 year"
ExpiresByType text/css "access plus 1 year"
ExpiresByType text/html "access plus 7 day"
ExpiresByType text/x-javascript "access 1 year"
ExpiresByType image/gif "access plus 1 year"
ExpiresByType image/jpeg "access plus 1 year"
ExpiresByType image/png "access plus 1 year"
ExpiresByType image/jpg "access plus 1 year"
ExpiresByType image/x-icon "access 1 year"
ExpiresByType application/x-shockwave-flash "access 1 year"
</IfModule>
# Cache-Control
<ifModule mod_headers.c>
# Задаем 30 дней для данного типа файла
<filesMatch «\.(ico|pdf|flv|jpg|jpeg|png|gif|swf)$»>
Header set Cache-Control "max-age=2592000, public"