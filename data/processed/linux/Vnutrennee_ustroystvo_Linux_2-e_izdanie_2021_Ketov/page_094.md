---
source_image: page_094.png
page_number: 94
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 22.49
tokens: 7435
characters: 1690
timestamp: 2025-12-24T04:34:24.506892
finish_reason: stop
---

finn@ubuntu:~$ ls -lad folder/
d---rwxr-x 2 finn finn 4096 окт. 12 00:40 folder/

finn@ubuntu:~$ ls -li folder/magic
ls: невозможно получить доступ к folder/magic: Отказано в доступе

finn@ubuntu:~$ chmod u+rw folder/
finn@ubuntu:~$ ls -lad folder/
drw-rwrxr-x 2 finn finn 4096 окт. 12 00:40 folder/

finn@ubuntu:~$ cp /etc/localtime folder/
cp: не удалось выполнить stat для «folder/localtime»: Отказано в доступе

finn@ubuntu:~$ rm folder/magic
rm: невозможно удалить «folder/magic»: Отказано в доступе

finn@ubuntu:~$ ls -l folder/
ls: невозможно получить доступ к folder/magic: Отказано в доступе
итого 0

! -??????? ? ? ? ? ? ? ? magic
finn@ubuntu:~$ chmod u=rwx folder/
finn@ubuntu:~$ ls -ld folder/
drwxrwxr-x 2 finn finn 4096 окт. 12 00:40 folder/
finn@ubuntu:~$ cd folder/
finn@ubuntu:~/folder$ ls -l
итого 4
-rw-r--r-- 1 finn finn 111 окт. 12 00:40 magic
finn@ubuntu:~/folder$ chmod a= magic
finn@ubuntu:~/folder$ ls -l magic
---------- 1 finn finn 111 окт. 12 00:40 magic
finn@ubuntu:~/folder$ rm magic
rm: удалить защищенный от записи обычный файл «magic»? y
finn@ubuntu:~/folder$ ls -l
! итого 0

Для жестких ссылок права доступа не существуют вовсе — они просто являются теми же правами, что и права целевого файла, в силу того что права доступа хранятся в метаданных. Для символьских ссылок семантика прав сохранена такой же, как и у жестких ссылок, с тем лишь различием, что права символьских ссылок существуют отдельно от целевых файлов, но никогда не проверяются (см. symlink(7)). Для изменения прав доступа самих символьских ссылок даже не существует специальной команды — при использовании chmod(1) со ссылкой всегда будут изменяться права целевого файла (листинг 3.39).