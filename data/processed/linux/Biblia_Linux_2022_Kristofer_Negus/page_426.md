---
source_image: page_426.png
page_number: 426
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 20.42
tokens: 7352
characters: 1515
timestamp: 2025-12-24T04:57:13.204070
finish_reason: stop
---

# description:    Apache is a World Wide Web server.
#                It is used to serve \
#                HTML files and CGI.
# processname: httpd
# config: /etc/httpd/conf/httpd.conf
# config: /etc/sysconfig/httpd
# pidfile: /var/run/httpd.pid

# Source function library.
. /etc/rc.d/init.d/functions
...
# See how we were called.
case "$1" in
    start)
        start
        ;;
    stop)
        stop
        ;;
    status)
        status $httpd
        RETVAL=$?
        ;;
...
esac

exit $RETVAL

После отработки скриптов уровня выполнения из соответствующего каталога /etc/rc.d/rc#.d процесс запуска демона SysVinit завершается. Последнее, что делает процесс init на этом этапе, — выполняет какие-либо дополнительные указания из файла /etc/inittab (например, создать процессы mingetty для виртуальных консолей и запустить интерфейс рабочего стола, если вы находитесь на уровне запуска 5).

Система инициализации systemd

Демон инициализации systemd — это замена демонам SysVinit и Upstart. Этот современный демон инициализации был добавлен в дистрибутивы Fedora 15 и RHEL 7 и используется до сих пор. Он имеет обратную совместимость с SysVinit и Upstart. Время инициализации системы демоном systemd сокращается, поскольку он может запускать службы параллельно.

Основы работы демона systemd

С помощью демона SysVinit службы останавливаются и запускаются на основе уровней выполнения. Служба systemd занимается уровнями выполнения, но реализует их по-другому — с помощью так называемых юнитов целей (target