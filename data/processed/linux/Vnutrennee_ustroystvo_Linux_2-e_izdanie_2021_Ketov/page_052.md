---
source_image: page_052.png
page_number: 52
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 25.68
tokens: 7391
characters: 1692
timestamp: 2025-12-24T04:33:22.168464
finish_reason: stop
---

dvk:x:1000:1000:Dmitry V. Ketov,,+7(812)703-02-02,,:/home/dvk:/bin/bash

finn@ubuntu:~$ cat /etc/group

dvk:x:1000:

lpadmin:x:119:dvk,finn

sambashare:x:131:dvk,finn

При использовании «коммутатора службы имен» (NSS, W:[Name Service Switch]) имеется возможность хранить базы данных учетных записей в любых хранилищах, включая сетевые службы каталогов NIS, NIS+, LDAP, активный каталог Microsoft Windows и даже реляционные сетевые базы данных SQL — при помощи соответствующих модулей NSS (листинг 2.25) и согласно настройкам коммутатора nsswitch.conf(5).

Листинг 2.25. Хранилища пользовательских учетных записей и модули NSS

finn@ubuntu:~$ cat /etc/nsswitch.conf

passwd:      files systemd
group:        files systemd
shadow:       files

finn@ubuntu:~$ find /lib/ -name 'libnss_*'
/lib/x86_64-linux-gnu/libnss_systemd.so.2
/lib/x86_64-linux-gnu/libnss_files.so
/lib/x86_64-linux-gnu/libnss_winbind.so.2

finn@ubuntu:~$ dpkg -S /lib/x86_64-linux-gnu/libnss_winbind.so.2
libnss-winbind:amd64: /lib/x86_64-linux-gnu/libnss_winbind.so.2

finn@ubuntu:~$ dpkg -s libnss-winbind
Package: libnss-winbind
This package provides nss_winbind, a plugin that integrates with a local winbindd server to provide user/group name lookups to the system; and nss_wins, which provides hostname lookups via both the NBNS and NetBIOS broadcast protocols.

2.8. Переменные окружения и конфигурационные dot-файлы

Для одноразовой параметризации выполнения команд служат их индивидуальные ключи, указываемые каждый раз при запуске команды, но иногда требуется установить некий параметр, который бы действовал в течение всего сеанса работы пользователя с системой, или общий параметр, который действовал бы для всех