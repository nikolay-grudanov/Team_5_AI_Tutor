---
source_image: page_514.png
page_number: 514
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 30.65
tokens: 7616
characters: 2044
timestamp: 2025-12-24T04:59:51.149905
finish_reason: stop
---

1. Проверьте службу vsftpd. Прежде чем запустить службу vsftpd, посмотрите, не работает ли она. В системе Fedora или Red Hat Enterprise Linux 7 или 8 выполните следующее:

# systemctl status vsftpd.service
vsftpd.service – Vsftpd ftp daemon
    Loaded: loaded (/usr/lib/systemd/system/vsftpd.service; disabled)
    Active: inactive (dead)

В дистрибутиве Red Hat Enterprise Linux 6, чтобы увидеть ту же информацию, нужны две команды:

# service vsftpd status
vsftpd is stopped
# chkconfig --list vsftpd
vsftpd 0:off 1:off 2:off 3:off 4:off 5:off 6:off

В приведенных примерах команды service, chkconfig и systemctl отображают состояние службы — stopped. Видно также, что она совсем отключена (в Fedora и RHEL 7 или 8) и выключена на каждом уровне запуска (в RHEL 6). Значение off означает, что служба не будет включаться автоматически при запуске системы.

2. Чтобы запустить и включить службу vsftpd в дистрибутиве Fedora или RHEL 7 или 8 (и проверить состояние), введите следующее:

# systemctl start vsftpd.service
# systemctl enable vsftpd.service
ln -s '/lib/systemd/system/vsftpd.service'
    '/etc/systemd/system/multi-user.target.wants/vsftpd.service'
# systemctl status vsftpd.service
vsftpd.service – Vsftpd ftp daemon
    Loaded: loaded (/usr/lib/systemd/system/vsftpd.service;
        enabled vendor preset: disabled))
    Active: active (running) since Wed, 2019-09-18 00:09:54 EDT; 22s ago
    Main PID: 4229 (vsftpd)
    Tasks: 1 (limit: 12232)
    Memory: 536.0K
    CGroup: /system.slice/vsftpd.service
        └─4229 /usr/sbin/vsftpd /etc/vsftpd/vsftpd.conf

В дистрибутиве Red Hat Enterprise Linux 6 запустите и включите (on) службу vsftpd (затем проверьте состояние) следующим образом:

# service vsftpd start
Starting vsftpd for vsftpd: [ OK ]
# chkconfig vsftpd on ; chkconfig --list vsftpd
vsftpd    0:off   1:off   2:on   3:on   4:on   5:on   6:off

3. Теперь в любой системе проверьте, работает ли служба, используя команду netstat:

# netstat -tupln | grep vsftpd
tcp  0  0 0.0.0.0:21  0.0.0.0:*   LISTEN   4229/vsftpd