---
source_image: page_348.png
page_number: 348
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 20.06
tokens: 6391
characters: 1476
timestamp: 2025-12-24T04:03:37.804939
finish_reason: stop
---

stop program = "/etc/init.d/apache2 stop"
    # если загрузка cpu > 90% 5 циклов то перезапустить процесс.
    if cpu > 90% for 5 cycles then restart
    # если не удается получить файл server-status, перезапустить
    if failed host localhost port 80 with protocol http and request "/server-status" with timeout 25 seconds for 4 times within 5 cycles then restart
    depend apache_bin
    depend apache_rc

check file apache_bin with path /usr/sbin/apache2
group apache
include /etc/monit/templates/rootbin

check file apache_rc with path /etc/init.d/apache2
group apache
include /etc/monit/templates/rootbin

Конфигурация monit, понятна даже новичку. На конкретном сервере была проблема с большой загрузкой процессора, после пика загрузки сервер падал. Поэтому было добавлено две проверки: если загрузка процессора выше 90%, сервис перезапускался и если сервер уже упал (не удается получить файл), то сервис тоже перезапускался.

20.3. Борьба с сессиями Magento: защита от переполнения диска

Magento хранит в сессиях информацию о деятельности пользователя на сайте, в том числе информацию о корзине посетителя. Примечательно, но эта информация так и не удаляется, в конечном счете, в каталоге var/session собирается огромнее количество файлов (конечно, если в настройках Magento указано, что сессии хранятся в файловой системе, а не в базе данных). Хранение сессий в базе данных решает эту проблему, но создает новую — база данных будет изрядно подтормаживать со временем.