---
source_image: page_347.png
page_number: 347
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 17.06
tokens: 6309
characters: 1029
timestamp: 2025-12-24T04:03:34.787732
finish_reason: stop
---

HTTPD="apache2"
$PGREP ${HTTPD}
if [ $? -ne 0 ]; then
$RESTART
date >> /var/log/srvmon.log
echo "Apache restarted" >> /var/log/srvmon.log
fi

RESTARTM="/etc/init.d/mysql restart"
MYSQLD="mysqld"
$PGREP ${MYSQLD}
if [ $? -ne 0 ]; then
$RESTART
$RESTARTM
date >> /var/log/srvmon.log
echo "Services restarted" > /var/log/srvmon.log
fi

Он не только перезапускает «упавшие» сервисы, но и ведет небольшой лог — записывает время, когда сервисы были перезапущены.

20.2.4. Monit: если нет таланта программиста

Все приведенное ранее можно сделать и с помощью сервиса monit. Его задача — мониторинг работоспособности сервера. Если что-то не так, то monit может перезапустить ту или иную службу.

В Интернете есть множество статей, посвященных monit, к тому же у него очень хорошая документация. Поэтому переписывать ее не станем. Вместо этого приведем реальный конфигурационный файл мониторинга Apache:

check process apache with pidfile /var/run/apache2.pid
    group www
    group apache
    start program = "/etc/init.d/apache2 start"