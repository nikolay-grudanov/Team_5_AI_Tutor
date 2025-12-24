---
source_image: page_600.png
page_number: 600
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 28.01
tokens: 7542
characters: 2427
timestamp: 2025-12-24T05:02:07.572618
finish_reason: stop
---

Чтобы просмотреть службы, запускаемые файлом multi-user.target, перечислите содержимое каталога /etc/systemd/system/multi-user.target.wants, как в примере далее:

# ls /etc/systemd/system/multi-user.target.wants/
atd.service        ksm.service        rhsmcertd.service
auditd.service     ksmtuned.service   rpcbind.service
avahi-daemon.service libstoragemgmt.service rsyslog.service
chronyd.service    libvirtd.service   smartd.service
crond.service      mcelog.service     sshd.service
cups.path          mdmonitor.service  sssd.service
dnf-makecache.timer ModemManager.service tuned.service
firewalld.service  NetworkManager.service vdo.service
irqbalance.service nfs-client.target   vmtoolsd.service
kdump.service      remote-fs.target

Эти файлы являются символическими ссылками на файлы, которые определяют, что начинать для каждой из этих служб. В системе они могут включать удаленную оболочку (sshd), печать (cups), аудит (auditd), сеть (NetworkManager) и др. Ссылки добавляются в этот каталог либо при установке пакета для службы, либо при включении службы с помощью команды systemctl enable.

Имейте в виду, что в отличие от System V init система systemd может запускать или останавливать единичные файлы, которые представляют собой нечто большее, чем просто службы, и иным образом управлять ими. Она может управлять устройствами, автоматическим монтированием, путями, розетками и т. д. После того как systemd все запустила, вы можете войти в систему, чтобы предотвратить любые потенциальные проблемы.

После входа в систему команда systemctl позволяет увидеть каждый unit-файл, который systemd пытается запустить, например:

# systemctl
UNIT                                 LOAD   ACTIVE   SUB
DESCRIPTION
proc-sys-fs-binfmt_misc.automount    loaded active waiting
    Arbitrary Executable File Formats File System
sys-devices-pc...:00:1b.0-sound-card0.device loaded active plugged
    631xESB/632xESB High Definition Audio Control
sys-devices-pc...:00:1d.2-usb4-4\x2d2.device loaded active plugged
    DeskJet 5550
...
-.mount                              loaded active mounted Root Mount
boot.mount                           loaded active mounted /boot
...
autofs.service                       loaded active running
    Automounts filesystems on demand
cups.service                         loaded active running
    CUPS Scheduler
httpd.service                        loaded failed failed
    The Apache HTTP Server