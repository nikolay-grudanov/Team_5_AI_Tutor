---
source_image: page_076.png
page_number: 76
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 30.31
tokens: 7526
characters: 1712
timestamp: 2025-12-24T04:34:01.854609
finish_reason: stop
---

файл, можно при помощи программ lsof(1) и fuser(1), что бывает полезно для идентификации программ, «занявших» файловую систему, подлежащую отмонтированию (см. ⋆ в листинге 3.21).

Листинг 3.18. Таблица файловых дескрипторов

① finn@ubuntu:~$ lsof -p $$¹
COMMAND   PID USER   FD TYPE DEVICE SIZE/OFF NODE NAME
...       ... ...
bash      17975 finn  1u  CHR  136,2    0t0   5 /dev/pts/2
...

② root@ubuntu:~# ls -la /dev/log
lrwxrwxrwx 1 root root 28 ноя 17 03:30 /dev/log -> /run/systemd/journal/dev-log
root@ubuntu:~# lsof /run/systemd/journal/dev-log
COMMAND   PID USER   FD TYPE DEVICE SIZE/OFF NODE NAME
systemd   1 root   35u  unix 0xffff964892232400 0t0 13321 /run/.../dev-log ...
systemd-j 285 root  6u  unix 0xffff964892232400 0t0 13321 /run/.../dev-log ...

root@ubuntu:~# fuser /run/systemd/journal/dev-log
/run/systemd/journal/dev-log:   1   285

root@ubuntu:~# ps p 285
PID TTY STAT TIME COMMAND
285 ? S< 0:04 /lib/systemd/systemd-journald

root@ubuntu:~# lsof /var/log/syslog
COMMAND   PID USER   FD TYPE DEVICE SIZE/OFF NODE NAME
rsyslogd 606 syslog  8w REG  8,2 1920291 131082 /var/log/syslog

root@ubuntu:~# ps up 606
USER     PID %CPU %MEM   VSZ RSS TTY STAT START TIME COMMAND
syslog   606 0.0 0.1 224360 4584 ? Ssl ноя17 0:00 /usr/sbin/rsyslogd -n ...

В первом ① примере из листинга 3.18 показано получение списка файловых дескрипторов (столбец FD) процесса командного интерпретатора bash пользователя finn, на котором файловый дескриптор ① номер 1 описывает открытый на чтение и запись u специальный символьный CHR файл устройства /dev/pts/2. Во втором ② примере показано получение информации о процессах, открывших файловый сокет

¹ О подстановках командного интерпретатора см. разд. 5.4.2.