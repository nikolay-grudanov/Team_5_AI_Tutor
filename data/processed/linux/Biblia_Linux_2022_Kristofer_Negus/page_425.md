---
source_image: page_425.png
page_number: 425
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 31.53
tokens: 7643
characters: 2424
timestamp: 2025-12-24T04:57:24.125860
finish_reason: stop
---

Каталог /etc/rc.d/rc#.d существует для всех стандартных уровней запуска Linux. Каждый из каталогов содержит скрипты для запуска и остановки служб своего конкретного уровня выполнения:

# ls -d /etc/rc.d/rc?.d
/etc/rc.d/rc0.d  /etc/rc.d/rc2.d  /etc/rc.d/rc4.d  /etc/rc.d/rc6.d
/etc/rc.d/rc1.d  /etc/rc.d/rc3.d  /etc/rc.d/rc5.d

На самом деле файлы в каталогах /etc/rc.d/rc#.d являются не скриптами, а символическими ссылками на скрипты в каталоге /etc/rc.d/init.d. Таким образом, нет необходимости в копировании определенных скриптов.

# ls -l /etc/rc.d/rc5.d/K15httpd
lrwxrwxrwx 1 root root 15 Oct 10 08:15
/etc/rc.d/rc5.d/K15httpd -> ../init.d/httpd
# ls /etc/rc.d/init.d
anacron        functions    multipathd    rpcidmapd
atd            fuse         netconsole    rpcsvcgcgssd
auditd         gpm          netfs         saslauthd
autofs         haldaemon    netplugd      sendmail
avahi-daemon   halt         network       setroubleshoot
avahi-dnsconfd hidd         NetworkManager single
bluetooth      hplip        NetworkManagerDispatcher smartd
btseed         hsqldb        nfs           smolt
bttrack        httpd         nfslock       spamassassin
capi           ip6tables     nscd          squid
ConsoleKit     iptables      ntpd          sshd
cpuspeed       irda          pand          syslog
crond          irqbalance    pcscd         tux
cups           isdn          psacct        udev-post
cups-config-daemon killall    rdisc         vncserver
dc_client      kudzu         readahead_early winbind
dc_server      mcstrans      readahead_later wpa_supplicant
dhcdbd         mdmonitor     restorecond   xfs
dund           messagebus    rpcbind       yppbind
firstboot      microcode     rpcgssd       yum-updatesd

Обратите внимание на то, что каждая служба имеет один скрипт в файле /etc/rc.d/init.d. Не существует отдельных скриптов для остановки и запуска службы. Эти скрипты останавливают или запускают службу в зависимости от того, какой параметр передается им демоном init.

Каждый скрипт в файле /etc/rc.d/init.d делает все, что необходимо для запуска или остановки конкретной службы на сервере. Далее приведена часть скрипта httpd в системе Linux, использующей демон SysVinit. Пример содержит оператор для обработки переданного ему параметра ($1), к примеру start, stop, status т. д.:

# cat /etc/rc.d/init.d/httpd
#!/bin/bash
#
# httpd      Startup script for the Apache HTTP Server
#
# chkconfig: -  85 15