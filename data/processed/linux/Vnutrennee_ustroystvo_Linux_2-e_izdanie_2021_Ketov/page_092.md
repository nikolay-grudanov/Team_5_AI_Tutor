---
source_image: page_092.png
page_number: 92
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 24.68
tokens: 7379
characters: 1227
timestamp: 2025-12-24T04:34:20.792887
finish_reason: stop
---

ную, символизирующую НЕжелание) маску доступа при помощи встроенной команды интерпретатора umask (листинг 3.36).

**Листинг 3.36. Реверсивная маска доступа**

finn@ubuntu:~$ umask
0002

finn@ubuntu:~$ umask -S
u=rwx,g=rwx,o=rx

finn@ubuntu:~$ touch common.jnl
finn@ubuntu:~$ ls -l common.jnl
-rw-r--r-- 1 finn finn 0 ноя 18 01:37 common.jnl

finn@ubuntu:~$ umask g-w,o-rwx
finn@ubuntu:~$ umask
0027

finn@ubuntu:~$ umask -S
u=rwx,g=rx,o=

finn@ubuntu:~$ touch group.jnl
finn@ubuntu:~$ ls -l group.jnl
-rw-r--r-- 1 finn finn 0 ноя 18 01:37 group.jnl

finn@ubuntu:~$ umask g=
finn@ubuntu:~$ umask
0077

finn@ubuntu:~$ umask -S
u=rwx,g=,o=

finn@ubuntu:~$ touch private.jnl
finn@ubuntu:~$ ls -l private.jnl
-rw------- 1 finn finn 0 ноя 18 01:38 private.jnl

Изменять режима доступа разрешено непосредственному пользователю — владельцу файла, но не членами группы-владельцев, что иллюстрирует листинг 3.37 при помощи команды chmod(1).

**Листинг 3.37. Изменение режима доступа к файлу**

finn@ubuntu:~$ id finn
uid=1000(finn) gid=1000(finn) группы=1000(finn),4(adm),24(cdrom),...,131(sambashare)

finn@ubuntu:~$ ls -l README.*
-rw-r--r-- 1 finn adm 2471 окт. 11 01:12 README.finn
-rw-r--r-- 1 jake adm 776 окт. 11 01:12 README.jake