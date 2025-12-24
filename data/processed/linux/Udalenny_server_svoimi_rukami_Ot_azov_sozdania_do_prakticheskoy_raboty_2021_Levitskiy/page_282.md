---
source_image: page_282.png
page_number: 282
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 19.97
tokens: 6314
characters: 1221
timestamp: 2025-12-24T04:02:20.645989
finish_reason: stop
---

</VirtualHost>

<VirtualHost *:443>
    ServerAdmin admin@example.com
    ServerName example.com
    ServerAlias www.example.com xxx.xxx.xxx.xxx
    DocumentRoot /srv/www/example.com/htdocs
    ErrorLog /srv/www/example.com/logs/error_log
    CustomLog /srv/www/example.com/logs/access_log combined env=!loopback

    SSLEngine on
    SSLCertificate /etc/ssl/example.pem
    SSLCertificateKeyFile /etc/ssl/server.key
</VirtualHost>

Разберемся, что и к чему. Сначала мы создаем виртуальный хост для порта 80, который будет работать как перенаправление — на https-версию сайта. Можно было бы сделать это и через .htaccess, но поскольку у нас есть доступ к конфигу сервера, то можно сделать это прямо здесь.

Далее мы описываем виртуальный хост для порта 443 (используется SSL). Настройки такие же, как и для обычной версии сайта (ServerName, DocumentRoot и т.д.). Отличие заключается только в наличии трех SSL-директив. Первая включает SSL, вторая задает PEM-файл, третья — KEY-файл (имена файлов, понятное дело, у вас будут отличаться).

После этого нужно сохранить файл конфигурации и перезапустить Apache:

sudo systemctl restart apache2.service

или (в зависимости от вашего дистрибутива)

sudo service apache2 restart