---
source_image: page_277.png
page_number: 277
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 21.62
tokens: 7469
characters: 1763
timestamp: 2025-12-24T04:39:53.098071
finish_reason: stop
---

протокола NFS v3 (-t nfs -o vers=3). Для получения списка экспортируемых (-e, export) сервером файловых систем 1 вызывается команда showmount(8), которая также является специализированным NFS-клиентом.

Листинг 6.27. Монтирование NFS

1 lumpy@ubuntu:~$ showmount -e NVR.local
Export list for NVR.local:
/Qweb *
/Qusb *
/Qrecordings *
/Qmultimedia *
/Qdownload *
/Public *
/Network Recycle Bin 1 *

lumpy@ubuntu:~$ sudo mkdir -p /mnt/network/nvr/Qmm

2 lumpy@ubuntu:~$ sudo mount -t nfs -o vers=3 NVR.local:/Qmultimedia /mnt/network/nvr/Qmm
lumpy@ubuntu:~$ findmnt -t nfs
TARGET                SOURCE                STYPE OPTIONS
/mnt/network/nvr/Qmm  NVR.local:/Qmultimedia nfs rw,relatime,vers=3,...

lumpy@ubuntu:~$ ls /mnt/network/nvr/Qmm
3 -rw-r--r-- 1 toothy users   678696 авг.  20 2014 IMG_20140719_125651.jpg
-rw-r--r-- 1 toothy users   649685 авг.  20 2014 IMG_20140719_125713.jpg
-rw-r--r-- 1 toothy users   814607 авг.  20 2014 IMG_20140820_111355.jpg

lumpy@ubuntu:~$ id toothy
uid=1010(toothy) gid=1012(toothy) группы=1012(toothy)

Необходимо отметить, что права доступа и идентификаторы UID/GID владельцев файлов 3 передаются NFS-протоколом в неизменном виде, поэтому базы пользовательских учетных записей всех клиентов (и сервера) должны быть согласованы, например, при помощи их централизованного хранения в каталоге LDAP.

NFS-сервер

Функционирование NFS-сервера имеет свою специфику, связанную с использованием NFS-протоколом принципа RPC (remote procedure call, удаленного вызова процедур) в реализации W:[SUN RPC]. Серверы, использующие SUN RPC, не имеют «закрепленного»1 номера порта TCP/UDP, а используют произвольный, случай-

1 Как, например, порт 22 закреплен за службой SSH, порт 25 — за SMTP, а порт 80 — за HTTP протоколом службы WWW.