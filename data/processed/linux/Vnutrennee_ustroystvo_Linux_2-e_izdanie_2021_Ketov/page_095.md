---
source_image: page_095.png
page_number: 95
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 34.30
tokens: 7654
characters: 2097
timestamp: 2025-12-24T04:34:36.424274
finish_reason: stop
---

Листинг 3.39. Права доступа ссылок

finn@ubuntu:~$ ls -l README.finn
-rwxr--r-- 1 finn finn 2471 окт. 11 01:13 README.finn

finn@ubuntu:~$ ln README.finn read.me

finn@ubuntu:~$ ln -s README.finn readme.1st

finn@ubuntu:~$ ls -l README.finn read.me readme.1st
-rwxr--r-- 2 finn finn 2471 окт. 11 01:13 read.me
lrwxrwxrwx 1 finn finn 11 окт. 12 01:19 readme.1st -> README.finn
-rwxr--r-- 2 finn finn 2471 окт. 11 01:13 README.finn

finn@ubuntu:~$ chmod g+w read.me

finn@ubuntu:~$ ls -l README.finn read.me readme.1st
-rwxrw-r-- 2 finn finn 2471 окт. 11 01:13 read.me
lrwxrwxrwx 1 finn finn 11 окт. 12 01:19 readme.1st -> README.finn
-rwxrw-r-- 2 finn finn 2471 окт. 11 01:13 README.finn

finn@ubuntu:~$ chmod o-r readme.1st

finn@ubuntu:~$ ls -l README.finn read.me readme.1st
-rwxrw--- 2 finn finn 2471 окт. 11 01:13 read.me
lrwxrwxrwx 1 finn finn 11 окт. 12 01:19 readme.1st -> README.finn
-rwxrw--- 2 finn finn 2471 окт. 11 01:13 README.finn

Для специальных файлов устройств, именованных каналов и сокетов право x не определено, а права r и w стоит воспринимать как права ввода и вывода информации на устройство и как права передачи и приема информации через средство взаимодействия.

Дополнительные атрибуты

Помимо базовых прав доступа r, w и x, для решения отдельных задач разграничения доступа используют дополнительные атрибуты s, Set user/group ID (SUID Set User ID или SGID, Set Group ID) — атрибут неявного делегирования полномочий и t, sTicky — «липучка», атрибут ограниченного удаления.

Типичной задачей, требующей неявного делегирования полномочий, является проблема невозможности изменения пользователями свойств своих учетных записей, которые хранятся в двух файлах-таблицах — passwd(5) и shadow(5), доступных на запись ① (и чтение ②) только суперпользователю root. Однако (листинг 3.40) команды passwd(1), chsh(1) и chfn(1), будучи запущены обычным пользователем, прекрасно изменяют (!) пароль в таблице /etc/shadow и свойства пользовательской записи в таблице /etc/passwd за счет передачи полномочий ③ пользователя — владельца программы тому пользователю, который ее запускает.