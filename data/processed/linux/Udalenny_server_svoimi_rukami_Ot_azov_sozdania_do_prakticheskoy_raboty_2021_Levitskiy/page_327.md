---
source_image: page_327.png
page_number: 327
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 17.72
tokens: 6269
characters: 1114
timestamp: 2025-12-24T04:03:11.174672
finish_reason: stop
---

18.4.2. Настройка Memcached

Демон Memcached позволяет добиться существенного ускорения загрузки страниц. Он доступен из репозитариев Ubuntu:

sudo apt install memcached

После установки демона нужно узнать порт, на котором он работает. Введите команду:

netstat -tap | grep memcached

Порт будет выведен после слова localhost, например, localhost:11211. Это стандартный порт для Memcached, который нужно указать в конфигурации mod_pagespeed.

Для ускорения PHP-приложений нужно установить пакет php-memcached:

apt install php-memcached

Осталось настроить mod_pagespeed на работу с помощью Memcached. Для этого откройте файл /etc/apache2/mods-available/pagespeed.conf:

mcedit /etc/apache2/mods-available/pagespeed.conf

Произведите поиск по строке ModPagespeedMemcachedServers. Раскомментируйте строку:

# ModPagespeedMemcachedServers localhost:11211

Она должна быть такой:

ModPagespeedMemcachedServers localhost:11211

Перезапустите Apache:

sudo service apache2 restart

После этого можете наблюдать некоторое ускорение работы вашего сайта. Для более тонкой настройки обратитесь к документации по memcached.