---
source_image: page_098.png
page_number: 98
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 31.62
tokens: 7567
characters: 1986
timestamp: 2025-12-24T04:34:43.884770
finish_reason: stop
---

щих» 1 для какой-то группы пользователей, каталогах, логичнее было бы назначать группой-владельцем создаваемых файлов эту общую группу 3.

Листинг 3.42. Дополнительный атрибут SGID для каталога

bubblegum@ubuntu:~$ cd /srv/kingdom
bubblegum@ubuntu:/srv$ id
uid=1005(bubblegum) gid=1005(bubblegum) группы=1005(bubblegum),1007(candy)
bubblegum@ubuntu:/srv/kingdom$ ls -ld .
drwxr-xr-x 2 bubblegum bubblegum 4096 окт. 21 22:02 .
bubblegum@ubuntu:/srv/kingdom$ touch bananaguard1
bubblegum@ubuntu:/srv/kingdom$ ls -l
итого 0
-rw-rw-r-- 1 bubblegum bubblegum 0 окт. 21 22:02 bananaguard1
bubblegum@ubuntu:/srv/kingdom$ chgrp candy .
bubblegum@ubuntu:/srv/kingdom$ chmod g+ws .
bubblegum@ubuntu:/srv/kingdom$ ls -ld .
drwxrwsr-x 2 bubblegum candy 4096 окт. 21 22:02 .
finn@ubuntu:/srv/kingdom$ id
uid=1001(finn) gid=1001(finn) группы=1001(finn),1007(candy)
finn@ubuntu:/srv/kingdom$ touch bananaguard2
finn@ubuntu:/srv/kingdom$ ls -l
итого 0
-rw-rw-r-- 1 bubblegum bubblegum 0 окт. 21 22:02 bananaguard1
3 -rw-rw-r-- 1 finn candy 0 окт. 21 22:02 bananaguard2

В примере из листинга 3.42 за счет SGID-атрибута каталога владельцем всех файлов, помещаемых в этот каталог, автоматически назначается группа-владелец самого каталога, а создатель (владелец) файла может теперь назначать нужные права доступа для всех членов этой группы к своему файлу — либо неявно при помощи реверсивной маски доступа, либо явно при помощи команды chmod(1).

Атрибут-«липучка» t (sTicky) служит для ограничения действия базового разрешения w записи в каталоге. Например, временный каталог /tmp предназначен для хранения временных файлов любых пользователей и поэтому доступен на запись всем пользователям. Однако право записи в каталог дает возможность не только создавать в нем новые файлы, но и удалять любые существующие файлы (любых пользователей), что совсем не кажется логичным. Именно атрибут t ограничивает возможность удалять чужие файлы, т. е. файлы, не принадлежащие пользователю, пытающемуся их удалить.