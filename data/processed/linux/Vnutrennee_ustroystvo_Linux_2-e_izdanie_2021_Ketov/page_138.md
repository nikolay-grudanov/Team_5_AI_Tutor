---
source_image: page_138.png
page_number: 138
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 33.81
tokens: 7675
characters: 2042
timestamp: 2025-12-24T04:35:53.991442
finish_reason: stop
---

Изменение идентификаторов EUID/EGID процесса происходит при срабатывании механизма неявной передачи полномочий, основанном на дополнительных атрибутах SUID/SGID файлов программ. При запуске таких программ посредством системного вызова exec(3) атрибуты EUID/EGID запускающего процесса устанавливаются равными идентификаторам UID/GID владельца запускаемой программы. В результате процесс, в который будет загружена такая программа, будет обладать правами владельца программы, а не правами пользователя, запустившего эту программу.

В листинге 4.21 приведен типичный пример использования механизма неявной передачи полномочий при выполнении команд passwd(1) и wall(1). При смене пароля пользователем при помощи программы /usr/bin/passwd ее процесс получает необходимое право записи ① в файл /etc/shadow (см. листинг 3.40) в результате передачи полномочий ① суперпользователя root (UID=0). При передаче широковещательного сообщения всем пользователям при помощи /usr/bin/wall необходимо иметь право записи ② в их файлы устройств /dev/tty*, которое появляется ② в результате передачи полномочий группы tty (GID = 5).

Листинг 4.21. Атрибуты файла SUID/SGID и атрибуты процесса RUID, EUID, RGID, EGID

fitz@ubuntu:~$ who
fitz pts/0 2019-11-22 00:52 (:0.0)
fitz pts/1 2019-11-22 00:53 (:0.0)
fitz pts/2 2019-11-22 01:06 (:0.0)

fitz@ubuntu:~$ ls -la /etc/shadow /dev/pts/*
crw--w---- 1 fitz tty 136, 2 ноя 19 12:00 /dev/pts/1
② crw--w---- 1 fitz tty 136, 3 ноя 19 13:53 /dev/pts/2
c---------- 1 root root 5, 2 ноя 17 03:30 /dev/pts/ptmx
① -rw-r----- 1 root shadow 1647 ноя 19 12:27 /etc/shadow

fitz@ubuntu:~$ ls -l /usr/bin/passwd /usr/bin/wall
-rwsr-xr-x 1 root root 67992 авг 29 16:00 /usr/bin/passwd
-rwxr-sr-x 1 root tty 35048 авг 21 16:19 /usr/bin/wall

fitz@ubuntu:~$ ls -ln /usr/bin/passwd /usr/bin/wall
-rwsr-xr-x 1 0 0 67992 авг 29 16:00 /usr/bin/passwd
-rwxr-sr-x 1 0 5 35048 авг 21 16:19 /usr/bin/wall

fitz@ubuntu:~$ ps ft pts/1,pts/2 o pid,ruid,rgid,euid,egid,tty,cmd
PID RUID RGID EUID EGID TT CMD
27883 1006 1008 1006 1008 pts/2 bash