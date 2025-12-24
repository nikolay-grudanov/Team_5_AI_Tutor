---
source_image: page_170.png
page_number: 170
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 29.93
tokens: 7581
characters: 1594
timestamp: 2025-12-24T04:36:46.160941
finish_reason: stop
---

«чистый» расход оперативной памяти системы 2. После принудительного завершения процесса при помощи команды kill(1) память естественным образом высвобождается. Однако, так как под процесс редактора был высвобожден страничный кэш 3, повторное его наполнение 4 будет происходить позже, при обращении процессов к своим отображенным файлам (и то, если потребуется).

Листинг 4.41. Потребление памяти процессами

fitz@ubuntu:~$ dd if=/dev/urandom of=big bs=4069 count=262144
262144+0 записей получено
262144+0 записей отправлено
1066663936 байт (1,1 GB, 1017 MiB) скопирован, 13,3567 s, 79,9 MB/s
fitz@ubuntu:~$ ls -lh big
-rw-rw-r-- 1 fitz fitz 1018M ноя 19 23:03 big
fitz@ubuntu:~$ free -m
total    used    free    shared    buffers    cache    available
Mem:     3935    987     509      39         71       2366     2656
Swap:    448     0       448
fitz@ubuntu:~$ vi big

fitz@ubuntu:~$ ps f
PID TTY STAT TIME COMMAND
20595 pts/1 S   0:00 -bash
21087 pts/1 R+  0:00 \_ ps f
20437 pts/0 S   0:00 -bash
21085 pts/0 Rl+ 0:08 \_ vi big

fitz@ubuntu:~$ ps up 21085
USER PID %CPU %MEM VSZ RSS TTY STAT START TIME COMMAND
fitz 21085 96.4 21.8 1816164 1807248 pts/0 Sl+ 21:14 0:18 vi big

fitz@ubuntu:~$ free -m
total    used    free    shared    buffers    cache    available
Mem:     3935    2752    133      38         55       993     913
Swap:    448     6       442

fitz@ubuntu:~$ top -b -n1 -p 21085
top - 23:11:05 up 2:49, 3 users, load average: 0,00, 0,09, 0,07
Tasks: 1 total, 0 running, 1 sleeping, 0 stopped, 0 zombie
%Cpu(s): 0,0 us, 0,0 sy, 0,0 ni,100,0 id, 0,0 wa, 0,0 hi, 0,0 si, 0,0 st