---
source_image: page_353.png
page_number: 353
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 26.90
tokens: 6338
characters: 1226
timestamp: 2025-12-24T04:03:54.222709
finish_reason: stop
---

до следующего циклического сдвига. Эта директива имеет силу только в комбинации с compress. Это может быть использовано в том случае, если некой программе нельзя указать закрыть ее файл журнала, и таким образом, можно некоторое время продолжать запись в предыдущий файл журнала.
• notifempty – не ротировать пустой файл.
• missingok – не записывать сообщение об ошибке, если журнал пуст.

Конечно, это далеко не все допустимые параметры конфигурации. О дополнительных вы можете узнать в справке (команда man logrotate) или по ссылке https://www.opennet.ru/man.shtml?topic=logrotate&category=8& russian=0.

Теперь представим, что у нас есть некий сервис daemond, хранящий свои файлы журналов в каталоге /var/log/daemond. Нужно настроить ротацию журналов этого сервиса.

Все достаточно просто: нужно в /etc/logrotate.d создать файл daemond (название может быть другим, важно, чтобы вы понимали, что находится в этом файле сразу по его названию) и заполнить конфигурацию ротации.

Создадим файл конфигурации ротации:

touch /etc/logrotate.d/daemond

Конфигурация может быть такой:

/var/log/daemond/*.log {
    daily
    missingok
    rotate 7
    compress
    notifempty
    create 0640 daemon-data daemon-data
    sharedscripts