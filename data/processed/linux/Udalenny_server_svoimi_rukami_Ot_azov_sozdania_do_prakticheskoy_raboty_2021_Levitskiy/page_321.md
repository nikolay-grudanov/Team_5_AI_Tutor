---
source_image: page_321.png
page_number: 321
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 19.24
tokens: 6366
characters: 1430
timestamp: 2025-12-24T04:03:04.916735
finish_reason: stop
---

18.3.2. Настройка Apache

Файл конфигурации Apache называется /etc/apache2/apache2.conf. Это основной файл конфигурации. Если нужно изменить конфигурацию для определенного сайта, поищите его конфиг в папке /etc/apache2/sites-available.

По умолчанию модуль mod_deflate должен быть включен в apache. Но лучше убедиться и выполнить проверку и поискать следующую строку в конфиге веб-сервера apache:

LoadModule deflate_module modules/mod_deflate.so

Мы можем определить, какие типы файлов нужно сжать:

AddOutputFilterByType DEFLATE text/html text/plain text/css application/javascript

Установите следующую конфигурацию в виртуальный хост Apache и это включит сжатие mod_deflate для вашего сайта.

<Directory /var/www/html/>
<IfModule mod_mime.c>
    AddType application/x-javascript .js
    AddType text/css .css
</IfModule>
<IfModule mod_deflate.c>
    # Сжимаем HTML, CSS, JavaScript, Text, XML и шрифты
    AddOutputFilterByType DEFLATE application/javascript
    AddOutputFilterByType DEFLATE application/rss+xml
    AddOutputFilterByType DEFLATE application/vnd.ms-fontobject
    AddOutputFilterByType DEFLATE application/x-font
    AddOutputFilterByType DEFLATE application/x-font-opentype
    AddOutputFilterByType DEFLATE application/x-font-otf
    AddOutputFilterByType DEFLATE application/x-font-truetype
    AddOutputFilterByType DEFLATE application/x-font-ttf
    AddOutputFilterByType DEFLATE application/x-javascript