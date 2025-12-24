---
source_image: page_128.png
page_number: 128
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 35.26
tokens: 7713
characters: 1865
timestamp: 2025-12-24T04:35:32.793597
finish_reason: stop
---

fitz@ubuntu:~$ ps f

PID TTY STAT TIME COMMAND
23025 pts/1 S 0:00 -bash
23228 pts/1 R 1:23 \_ dd if=/dev/dvd of=plan9.iso
23230 pts/1 R+ 0:00 \_ ps f

fitz@ubuntu:~$

fitz@ubuntu:~$ 586896+0 записей получено
586896+0 записей отправлено
300490752 байт (300 MB, 286 MiB) скопирован, 14,6916 c, 20,5 MB/c

[1]+ Завершён dd if=/dev/dvd of=plan9.iso

В листинге 4.12 показана конвейерная (см. разд. 5.3) конструкция интерпретатора, при помощи которой осуществляется поиск самого большого файла с суффиксом .html вниз по дереву каталогов, начиная с /usr/share/doc. Эта конструкция реализуется при помощи fork-and-exec четырьмя параллельно порожденными дочерними процессами интерпретатора, в каждом из которых запущена программа соответствующей части конвейера, при этом дочерние процессы связаны неименованным каналом pipe(2) — простейшим средством межпроцессного взаимодействия (см. разд. 4.9). Встроенная команда интерпретатора wait реализует одноименный системный вызов wait(2) и используется для ожидания окончания всех дочерних процессов конвейера, целиком запущенного в «фоновом» режиме.

Листинг 4.12. Параллельный запуск взаимодействующих программ

find /usr/share/doc -type f -name '*.html' | xargs -n1 wc -l | sort -k 1 -nr | head -1 &

[1] 12827
fitz@ubuntu:~$ ps fj

PPID PID PGID SID TTY TPGID STAT UID TIME COMMAND
11715 11716 11716 9184 pts/0 14699 S 1006 0:01 -bash
11716 12824 12824 9184 pts/0 14699 R 1006 0:00 \_ find ... -type f -name *.html
11716 12825 12824 9184 pts/0 14699 R 1006 0:00 \_ xargs -n1 wc -l
11716 12826 12824 9184 pts/0 14699 S 1006 0:00 \_ sort -k 1 -nr
11716 12827 12824 9184 pts/0 14699 S 1006 0:00 \_ head -1
11716 14699 14699 9184 pts/0 14699 R+ 1006 0:00 \_ ps fj

fitz@ubuntu:~$ wait
15283 /usr/share/doc/xterm/xterm.log.html

[1]+ Завершён find /usr/share/doc -type f -name '*.html' | xargs -n1 wc -l | sort -k 1 -nr | head -1