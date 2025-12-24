---
source_image: page_435.png
page_number: 435
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 34.84
tokens: 7699
characters: 2282
timestamp: 2025-12-24T04:57:46.339680
finish_reason: stop
---

udev-post    0:off   1:off   2:off   3:on    4:on    5:on    6:off
vncserver    0:off   1:off   2:off   3:off   4:off   5:off   6:off
winbind       0:off   1:off   2:off   3:off   4:off   5:off   6:off
wpa_supplicant 0:off   1:off   2:off   3:off   4:off   5:off   6:off
xfs           0:off   1:off   2:on    3:on    4:on    5:on    6:off
ypbind        0:off   1:off   2:off   3:off   4:off   5:off   6:off
yum-updatesd  0:off   1:off   2:off   3:on    4:on    5:on    6:off

Некоторые службы никогда не запускаются, например vncserver. Другие службы, например демон cups, запускаются на уровнях выполнения со второго по пятый.

С помощью команды chkconfig нельзя определить, запущена ли служба в данный момент. Для этого необходимо воспользоваться командой service. Чтобы отделить только запущенные в данный момент службы, команда service передается по конвейеру в команду grep, а затем сортирует вывод следующим образом:

# service --status-all | grep running... | sort
anacron (pid 2162) is running...
atd (pid 2172) is running...
auditd (pid 1653) is running...
automount (pid 1952) is running...
console-kit-daemon (pid 2046) is running...
crond (pid 2118) is running...
cupsd (pid 1988) is running...
...
sshd (pid 2002) is running...
syslogd (pid 1681) is running...
xfs (pid 2151) is running...
yum-updatesd (pid 2205) is running...

Можно использовать обе команды, chkconfig и service, чтобы просмотреть параметры каждой службы. С помощью обеих команд вы сможете просмотреть настройки демона cups:

# chkconfig --list cups
cups      0:off   1:off   2:on    3:on    4:on    5:on    6:off
#
# service cups status
cupsd (pid 1988) is running...

Здесь видно, что демон cupsd настроен на запуск на каждом уровне выполнения, кроме 0, 1 и 6, а команда service показывает, что он в данный момент работает. Кроме того, для демона задается номер идентификатора процесса (PID).

Чтобы просмотреть все службы демона systemd для сервера Linux, используйте следующую команду:

# systemctl list-unit-files --type=service | grep -v disabled
UNIT FILE                                 STATE
abrt-ccpp.service                         enabled
abrt-oops.service                         enabled
abrt-vmcore.service                       enabled
abrttd.service                            enabled