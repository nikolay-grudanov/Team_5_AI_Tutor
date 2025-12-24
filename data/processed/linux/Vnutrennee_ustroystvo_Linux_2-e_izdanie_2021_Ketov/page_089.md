---
source_image: page_089.png
page_number: 89
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 28.59
tokens: 7465
characters: 1546
timestamp: 2025-12-24T04:34:24.071233
finish_reason: stop
---

**Листинг 3.31. Владельцы файлов**

finn@ubuntu:~$ ls -la /etc/profile .profile

-rw-r--r-- 1 root root 581 авг 27 21:31 /etc/profile
-rw-r--r-- 1 finn finn 807 ноя 13 00:25 .profile

finn@ubuntu:~$ stat .profile

Доступ: (0644/-rw-r--r--) ①Uid: (1000/finn) ②Gid: (1000/finn)

Назначаются владельцы файлов при их создании. По умолчанию пользователем-владельцем файла становится пользователь, создавший файл, а группой-владельцем файла становится его первичная группа (листинг 3.32).

**Листинг 3.32. Назначение владельцев файлов при создании**

finn@ubuntu:~$ id
uid=1000(finn) gid=1000(finn) группы=1000(finn),4(adm),24(cdrom),...,131(sambashare)
finn@ubuntu:~$ nano README
finn@ubuntu:~$ ls -la README
-rw-rw-r-- 1 finn finn 3 ноя 18 01:20 README

Изменить (листинг 3.33) пользователя-владельца ① файлов может только суперпользователь ① root при помощи команды chown(1), а группу-владельца — владелец файла ② при помощи команды chgrp(1), но только на ту ③ к которой он сам принадлежит.

**Листинг 3.33. Смена владельцев файлов**

finn@ubuntu:~$ ls -la README
-rw-rw-r-- 1 finn finn 3 ноя 18 01:20 README
finn@ubuntu:~$ chown jake README
① chown: изменение владельца 'README': Операция не позволена
finn@ubuntu:~$ id
uid=1000(finn) gid=1000(finn) группы=1000(finn),4(adm),24(cdrom),...,131(sambashare)
② finn@ubuntu:~$ chgrp adm README
finn@ubuntu:~$ ls -la README
-rw-rw-r-- 1 finn adm 3 ноя 18 01:20 README
finn@ubuntu:~$ chgrp daemon README
③ chgrp: изменение группы для 'README': Операция не позволена
① finn@ubuntu:~$ sudo chown jake README