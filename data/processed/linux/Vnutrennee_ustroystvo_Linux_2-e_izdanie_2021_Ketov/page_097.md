---
source_image: page_097.png
page_number: 97
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 21.52
tokens: 7432
characters: 1701
timestamp: 2025-12-24T04:34:29.122091
finish_reason: stop
---

finn@ubuntu:~$ ls -l /dev/tty1 /dev/tty2
crw------ 1 finn tty 4, 1 окт. 20 00:03 /dev/tty1
crw------ 1 jake tty 4, 2 окт. 20 00:03 /dev/tty2
finn@ubuntu:~$ write jake
write: jake has messages disabled

Сеанс jake
jake@ubuntu:~$ mesg y

finn@ubuntu:~$ ls -l /dev/tty2
crw--w---- 1 jake tty 4, 2 окт. 20 00:07 /dev/tty2
finn@ubuntu:~$ write jake
write: write: you have write permission turned off.

Hi, buddy, wazzzup?
^D

Сеанс jake
jake@ubuntu:~$
Message from finn@ubuntu on tty1 at 00:10 ...
Hey buddy, wazzup?
EOF

finn@ubuntu:~$ ls -ll /usr/bin/write
-rwxr-sr-x 1 root tty 14328 мая 3 2018 /usr/bin/write

Аналогично (см. листинг 3.41) при использовании атрибута SGID, при передаче сообщений от пользователя к пользователю командой write(1) или wall(1), запускающему эти программы пользователю делегируются полномочия группы tty, имеющей доступ на запись к терминалам (специальным файлам устройств /dev/ttyN), владельцы которых разрешили такой доступ.

Именно за счет механизма SUID/SGID различные команды позволяют обычным, непривилегированным пользователям, выполнять сугубо суперпользовательские действия. Так, например, su(1) и sudo(1) позволяют выполнять команды одним пользователям от лица других пользователей, mount(8), umount(8) и fusermount(1) — монтировать и размонтировать файловые системы, ping(8) и traceroute(1) — выполнять диагностику сетевого взаимодействия, at(1) и crontab(1) — сохранять в «системных» каталогах отложенные и периодические задания, и т. д.

Однако для каталогов атрибут SGID имеет совсем другой смысл. По умолчанию владельцем файла становится тот пользователь (и его первичная группа), который запустил программу, создавшую файл. Но для файлов, создаваемых в «об-