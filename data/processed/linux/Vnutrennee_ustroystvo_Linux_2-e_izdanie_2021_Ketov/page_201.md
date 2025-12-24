---
source_image: page_201.png
page_number: 201
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 42.46
tokens: 7725
characters: 1755
timestamp: 2025-12-24T04:37:53.242921
finish_reason: stop
---

Листинг 5.13. Конвейерная обработка: просмотр группового членства пользователей системы

bender@ubuntu:~$ getent passwd | cut -f 1 -d : | xargs groups
finn : finn candy
jake : jake
bubblegum : bubblegum candy
fitz : fitz sudo
skillet : skillet
bender : bender

С помощью конвейеров и универсального спискового «применителя» команд xargs(1) можно организовать (листинг 5.14) параллельный запуск (-P) упаковки целого списка отобранных командой find(1) файлов, использовав параллельный упаковщик pbzip2(1), в несколько упаковочных нитей (-p) на каждый файл. В результате получим запускаемые парами процессы по две активные нити на каждый, что эффективно загружает четырехъядерный процессор в течение упаковки всего списка файлов.

Листинг 5.14. Конвейерная обработка: параллельная упаковка ISO-образов

bender@ubuntu:~$ find . -name '*.iso' | xargs -P 2 pbzip2 -p2 &
bender@ubuntu:~$ ps f
PID TTY STAT TIME COMMAND
4723 pts/1 S 0:00 -bash
4903 pts/1 S 0:00 \_ xargs -P 2 -n1 pbzip2 -p2
4904 pts/1 Sl 0:08 \_ pbzip2 -p2 ./dvd.iso
4905 pts/1 Sl 0:08 \_ pbzip2 -p2 ./plan9.iso
4856 pts/1 R+ 0:00 \_ ps f
bender@ubuntu:~$ ps -fL
UID PID PPID LWP C NLWP STIME TTY TIME CMD
bender 4723 4722 4723 0 1 01:18 pts/1 00:00:00 -bash
bender 4903 4723 4903 0 1 01:21 pts/1 00:00:00 xargs -P 2 -n1 pbzip2
bender 4904 4903 4910 99 6 01:21 pts/1 00:00:01 pbzip2 -p2 ./dvd.iso
bender 4904 4903 4913 99 6 01:21 pts/1 00:00:01 pbzip2 -p2 ./dvd.iso
bender 4904 4903 4914 0 6 01:21 pts/1 00:00:00 pbzip2 -p2 ./dvd.iso
bender 4905 4903 4911 99 6 01:21 pts/1 00:00:01 pbzip2 -p2 ./plan9.is
bender 4905 4903 4912 99 6 01:21 pts/1 00:00:01 pbzip2 -p2 ./plan9.is
bender 4905 4903 4915 0 6 01:21 pts/1 00:00:00 pbzip2 -p2 ./plan9.is
bender 4916 4723 4916 0 1 01:21 pts/1 00:00:00 ps -fL