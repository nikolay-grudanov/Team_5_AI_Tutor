---
source_image: page_447.png
page_number: 447
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 27.74
tokens: 7441
characters: 1526
timestamp: 2025-12-24T04:58:00.065037
finish_reason: stop
---

echo
    [ $RETVAL = 0 ] && touch /var/lock/subsys/cups
return $RETVAL
}
stop () {
    # stop daemon
    echo -n $"Stopping $prog: "
    killproc $DAEMON
    RETVAL=$?
    echo        [ $RETVAL = 0 ] && rm -f /var/lock/subsys/cups
}
restart() {
    stop
    start
}
case $1 in
...
Скрипт службы cups начинается с создания функций для каждого из параметров start, stop и restart. Если у вас возникли проблемы с написанием скриптов оболочки, обратитесь к главе 7 «Простейшие скрипты оболочки».

Строка, которую обязательно нужно проверить и, возможно, изменить в новом скрипте, — это закомментированная строка chkconfig, например:

# chkconfig: 2345 25 10

При добавлении скрипта службы на более позднем этапе команда chkconfig считывает эту строку, чтобы установить уровни выполнения для служб start (2, 3, 4 и 5), порядок выполнения, когда скрипт настроен на службы start (25), и порядок завершения, когда он установлен на службы stop (10). Проверьте порядок загрузки на уровне выполнения по умолчанию, прежде чем добавлять собственный скрипт, как показано в примере:

# ls /etc/rc5.d
...
/etc/rc5.d/S22messagebus
/etc/rc5.d/S23NetworkManager
/etc/rc5.d/S24nfslock
/etc/rc5.d/S24openct
/etc/rc5.d/S24rpcgssd
/etc/rc5.d/S25blk-availability
/etc/rc5.d/S25cups
/etc/rc5.d/S25netfs
/etc/rc5.d/S26acpid
/etc/rc5.d/S26haldaemon
/etc/rc5.d/S26hypervkvpd
/etc/rc5.d/S26udev-post
...

В этом случае строка chkconfig в скрипте S25My_New_Service приведет к добавлению скрипта после S25cups и перед S25netfs в порядке загрузки. По желанию