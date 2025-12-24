---
source_image: page_357.png
page_number: 357
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 20.98
tokens: 7713
characters: 1632
timestamp: 2025-12-24T04:28:47.876167
finish_reason: stop
---

2. В следующий раз, при достижении максимального размера, содержимое файла /var/log/messages.1 переносится в /var/log/messages.2, а журнал /var/log/messages переносится в /var/log/messages.1.

Таким образом, история изменений сохраняется в отдельных файлах, и ее можно всегда просмотреть. При этом сам журнал никогда не превысит определенного размера, и с ним будет удобно работать.

За сохранение истории и перенос данных между файлами отвечает программа logrotate. Рассмотрим ее конфигурационный файл (/etc/logrotate.conf), который показан в листинге 12.5.

Листинг 12.5. Файл /etc/logrotate.conf конфигурации программы logrotate

# see "man logrotate" for details
# Выполните команду man logrotate для получения дополнительной информации

# rotate log files weekly
# Смена файлов происходит еженедельно
weekly

# keep 4 weeks worth of backlogs
# Будут использоваться 4 файла для сохранения истории
rotate 4

# create new (empty) log files after rotating old ones
# После сохранения журнала создается пустой новый файл
create

# uncomment this if you want your log files compressed
# Уберите комментарий со следующей строки,
# чтобы файлы журналов сжимались
#compress

# RPM packages drop log rotation information into this directory
# Пакеты RPM переносят информацию о переворотах журнала в эту директорию
include /etc/logrotate.d

# no packages own wtmp -- we'll rotate them here
# Для журнала /var/log/wtmp задаются собственные правила
/var/log/wtmp {
    monthly
    create 0664 root utmp
    rotate 1
}

# system-specific logs may be also be configured here.
# Специфичные системные журналы могут быть сконфигурированы здесь.