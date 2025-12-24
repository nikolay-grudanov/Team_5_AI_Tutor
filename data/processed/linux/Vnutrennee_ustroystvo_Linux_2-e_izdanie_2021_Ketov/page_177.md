---
source_image: page_177.png
page_number: 177
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 25.74
tokens: 7504
characters: 1296
timestamp: 2025-12-24T04:36:54.064029
finish_reason: stop
---

fitz@ubuntu:~$ man dd

[2]+ Остановлен man dd

fitz@ubuntu:~$ jobs -l
[1]- 3181 Запущен      dd if=/dev/zero of=/dev/null &
[2]+ 3193 Остановлено   man dd

fitz@ubuntu:~$ ps jf
PPID PID PGID SID TTY TPGID STAT UID TIME COMMAND
3094 3099 3099 3099 pts/0 3310 Ss 1000 0:00 bash
3099 3181 3181 3099 pts/0 3310 R 1000 4:48 \_ dd if=/dev/zero of=
3099 3193 3193 3099 pts/0 3310 T 1000 0:00 \_ man dd
3193 3203 3193 3099 pts/0 3310 T 1000 0:00 | \_ pager -s
3099 3310 3310 3099 pts/0 3310 R+ 1000 0:00 \_ ps jf

fitz@ubuntu:~$ fg %1
dd if=/dev/zero of=/dev/null

^Z
[1]+ Остановлен      dd if=/dev/zero of=/dev/null

fitz@ubuntu:~$ ps f
PID TTY STAT TIME COMMAND
3099 pts/0 Ss 0:00 bash
3181 pts/0 T 26:44 \_ dd if=/dev/zero of=/dev/null
3193 pts/0 T 0:00 \_ man dd
3203 pts/0 T 0:00 | \_ pager -s
3937 pts/0 R+ 0:00 \_ ps f

fitz@ubuntu:~$ bg 1
[1]+ dd if=/dev/zero of=/dev/null &

fitz@ubuntu:~$ fg %2
man dd

fitz@ubuntu:~$ jobs
[1]+ Запущен      dd if=/dev/zero of=/dev/null &
fitz@ubuntu:~$ fg
dd if=/dev/zero of=/dev/null
^C11771330744+0 записей получено
11771330743+0 записей отправлено
скопировано 6026921340416 байт (6,0 TB), 8400,83 с, 717 MB/c

Кроме переключения группы «переднего» фона, механизм управления заданиями координирует «совместный» доступ процессов к управляющему терминалу. При