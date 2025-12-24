---
source_image: page_099.png
page_number: 99
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 36.36
tokens: 7608
characters: 1961
timestamp: 2025-12-24T04:34:51.149335
finish_reason: stop
---

Листинг 3.43. Дополнительный атрибут sticky для каталога

finn@ubuntu:/srv/kingdom$ id
uid=1001(finn) gid=1001(finn) группы=1001(finn),1007(candy)

finn@ubuntu:/srv/kingdom$ ls -la
итого 8
drwxrwsr-x 2 bubblegum candy 4096 окт. 23 20:57 .
drwxr-xr-x 3 root root 4096 окт. 21 21:57 ..
-rw-rw-r-- 1 bubblegum bubblegum 0 окт. 21 23:15 bananaguard1
-rw-rw-r-- 1 finn candy 0 окт. 21 23:24 bananaguard2

finn@ubuntu:/srv/kingdom$ rm bananaguard1
rm: удалить защищенный от записи пустой обычный файл «bananaguard1»? y

finn@ubuntu:/srv/kingdom$ ls -l
итого 0
-rw-rw-r-- 1 finn candy 0 окт. 21 23:24 bananaguard2

bubblegum@ubuntu:/srv/kingdom$ chmod +t .
bubblegum@ubuntu:/srv/kingdom$ touch bananaguard1
bubblegum@ubuntu:/srv/kingdom$ ls -la
итого 8
drwxrwsr-t 2 bubblegum candy 4096 окт. 23 21:19 .
drwxr-xr-x 3 root root 4096 окт. 21 21:57 ..
-rw-rw-r-- 1 bubblegum candy 0 окт. 23 21:19 bananaguard1
-rw-rw-r-- 1 finn candy 0 окт. 23 21:19 bananaguard2

finn@ubuntu:/srv/kingdom$ rm bananaguard1
rm: невозможно удалить «bananaguard1»: Операция не позволена

3.5.3. Списки контроля доступа POSIX

Режим доступа к файлу (access mode), определяющий базовые разрешения r, w и x только для трех субъектов доступа (владельца, группы-владельца и всех остальных), не является достаточно гибким и удобным инструментом разграничения доступа. Списки контроля доступа (W:[ACL], access control lists), согласно стандарту POSIX.1e, расширяют классический режим доступа к файлу дополнительными записями (рис. 3.4), определяющими права доступа для явно указанных пользователей и групп. Для просмотра и модификации записей в списках доступа используются утилиты getfacl(1) и setfacl(1), соответственно.

В примере из листинга 3.44 для всех «остальных» (не входящих в группу candy) пользователей отзываются все права на каталог /srv/kingdom/stash, но для отдельного пользователя jake (не являющегося членом группы candy) назначаются права чтения, модификации и прохода в него rwx.