---
source_image: page_261.png
page_number: 261
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 19.35
tokens: 6288
characters: 1063
timestamp: 2025-12-24T04:01:50.594287
finish_reason: stop
---

Они подключают необходимый репозиторий и обновляют список пакетов. Теперь можно установить PHP:

sudo apt install php7.2 php7.2-cli

После установки введите команду php -v, чтобы убедиться, что установлена версия 7.2. Если все хорошо, тогда установите необходимые расширения, как было показано ранее.

Теперь нужно настроить PHP и Apache. Первым делом откройте файл конфигурации PHP (X — версия):
sudo mcedit /etc/php/7.x/apache2/php.ini

В нем нужно установить лимит памяти:

memory_limit = 512M

Можно установить и другие параметры, но об этом мы поговорим далее в этой книге, когда пойдет речь об оптимизации сервера.

Сохраните файл, выйдите из редактора и добавьте необходимые модули Apache:

sudo a2enmod rewrite

Также, чтобы normally работали SEF URL Magento нужно открыть ваш файл конфигурации /etc/apache2/sites-enabled/000-default.conf и добавьте в секцию VirtualHost строки:

<Directory /var/www/html/magento_test>
Options Indexes FollowSymLinks MultiViews
AllowOverride All
</Directory>

Все, можно перезапускать Apache:

sudo service apache2 restart