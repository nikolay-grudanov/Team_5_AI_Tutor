---
source_image: page_355.png
page_number: 355
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 15.58
tokens: 7562
characters: 949
timestamp: 2025-12-24T04:28:42.035343
finish_reason: stop
---

else
    SYSLOGD_OPTIONS="-m 0"
    KLOGD_OPTIONS="-2"
fi

RETVAL=0

umask 077

start() {
    echo -n $"Starting system logger: "
    daemon syslogd $SYSLOGD_OPTIONS
    RETVAL=$?
    echo
    echo -n $"Starting kernel logger: "
    daemon klogd $KLOGD_OPTIONS
    echo
    [ $RETVAL -eq 0 ] && touch /var/lock/subsys/syslog
    return $RETVAL
}
stop() {
# Команды остановки сервиса
}
rhstatus() {
# Команды вывода состояния
}
restart() {
    stop
    start
}
...
...

Самое интересное спрятано в следующих строчках:

if [ -f /etc/sysconfig/syslog ] ; then
    . /etc/sysconfig/syslog
else
    SYSLOGD_OPTIONS="-m 0"
    KLOGD_OPTIONS="-2"
fi

Здесь происходит проверка: если файл /etc/sysconfig/syslog существует, то используются параметры загрузки из этого файла, иначе они явно задаются в строке

SYSLOGD_OPTIONS="-m 0"

Здесь в кавычках указываются параметры. Чтобы добавить ключ -r, измените строку следующим образом:

SYSLOGD_OPTIONS="-m 0 -r"