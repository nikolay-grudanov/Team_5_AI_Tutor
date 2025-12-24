---
source_image: page_154.png
page_number: 154
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 22.13
tokens: 6356
characters: 1227
timestamp: 2025-12-24T03:59:36.665508
finish_reason: stop
---

sudo apt install php php-cli openssl php-curl php-gd php-mcrypt php-xml php-intl php-zip php-mbstring php-soap php-mysql php-json libapache2-mod-php php-xsl composer

Она установит последнюю версию интерпретатора, доступную для вашего дистрибутива. Например, для Ubuntu 16.04 — это будет 7.0, для 18.04 — 7.2.

Узнать версию можно командой:

php -v

![Скриншот терминала с выводом версии PHP](../images/chapter8_4.png)

Рис. 8.4. Версия интерпретатора

Установим максимальный размер памяти для сценария. Откройте файл конфигурации (X — версия):

sudo mcedit /etc/php/7.X/apache2/php.ini

В нем нужно изменить лимит памяти и сразу сохраниться:

memory_limit = 512M

Добавим необходимые модули Apache (введите команду):

a2enmod rewrite

Также, чтобы normally работали SEF URL некоторых CMS нужно открыть /etc/apache2/sites-enabled/000-default.conf и добавить в секцию VirtualHost строки:

<Directory /var/www/html/magento_test>
Options Indexes FollowSymLinks MultiViews
AllowOverride All
</Directory>

Все, можно повторно перезапускать Apache.

8.5.5. Загрузка файлов с локальной системы на VPS

Загрузите ваши файлы в каталог /var/www/html или любой другой, который вы указали в DocumentRoot. Если для подключения по SSH вы ис-