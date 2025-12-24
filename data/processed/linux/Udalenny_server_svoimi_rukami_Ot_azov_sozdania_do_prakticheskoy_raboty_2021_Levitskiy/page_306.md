---
source_image: page_306.png
page_number: 306
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 23.13
tokens: 6273
characters: 1046
timestamp: 2025-12-24T04:02:53.044120
finish_reason: stop
---

по умолчанию Webmin содержит более 500 различных скриптов, которые можно использовать для настройки различных компонентов системы. Благодаря этим скриптам возможностей у Webmin будет больше, чем у VestaCP, где некоторые модули, например, файловый менеджер, придется покупать (50 долларов пожизненно или 3 доллара в месяц).

17.3.2. Установка Webmin

Первым делом установите файловый менеджер mc, чтобы было удобнее работать, в том числе изменять содержимое конфигурационных файлов. Откройте терминала или подключитесь к серверу по ssh и введите команду:

sudo apt install mc

Далее нам нужно подключить репозитарий с webmin. Для этого откройте файл /etc/apt/sources.list и добавьте в него строки:

deb http://download.webmin.com/download/repository sarge contrib
deb http://webmin.mirror.somersettechsolutions.co.uk/repository sarge contrib.

Добавьте GPG-ключ:

wget http://www.webmin.com/jcameron-key.asc
sudo apt-key add jcameron-key.asc

Осталось обновить списки пакетов и установить пакет webmin:

sudo apt-get update
sudo apt install webmin