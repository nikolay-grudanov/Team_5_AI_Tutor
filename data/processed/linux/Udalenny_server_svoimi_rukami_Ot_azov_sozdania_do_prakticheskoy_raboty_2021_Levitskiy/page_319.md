---
source_image: page_319.png
page_number: 319
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 24.52
tokens: 6439
characters: 1502
timestamp: 2025-12-24T04:03:06.598521
finish_reason: stop
---

# Выделяем буфер для gzip
    gzip_buffers 32 4k;
# Устанавливаем уровень сжатия, от 1-9
    gzip_comp_level 9;
# Убираем поддержку IE6
    gzip_disable «msie6»;
# Устанавливаем версию http для использования gzip (1.0 или 1.1)
    gzip_http_version 1.1;
# Разрешаем использовать статику
    gzip_static on;
    gzip_vary on;
# Определяем, какие типы файлов нужно сжимать
    gzip_types text/css text/javascript text/xml text/plain text/x-component application/javascript application/x-javascript application/json application/xml application/rss+xml font/truetype application/x-font-ttf font/opentype application/vnd.ms-fontobject image/svg+xml;

Теперь настроим кэширование. При настройке времени кэширования помните и об обратном эффекте кэширования. Если вы внесете изменения в ваши стили или скрипты, то пользователи увидят их только, когда загрузят новую версию. Чтобы увидеть изменения раньше, нужно будет очистить кэш браузера, а как это сделать, как показывает практика, знают не все пользователи. В любом случае приведенный конфиг предполагает хранения файлов в кэше 1 сутки (86400 секунд). Если вы вносите изменения в сайт редко, можно увеличить это время до 10-30 суток. Для статического контента, который никогда не меняется (выложили файл и забыли о нем) кэширование включено сроком на 1 год.

# Хранить кэш 24ч\1 сутки
    expires 86400s;
# Добавляем заголовки (хеадеры)
    add_header Pragma public;
    add_header Cache-Control "max-age=86400, public, must-revalidate, proxy-revalidate";