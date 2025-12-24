---
source_image: page_181.png
page_number: 181
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 41.30
tokens: 7818
characters: 2026
timestamp: 2025-12-24T04:37:18.092305
finish_reason: stop
---

9270 pts/1   T   0:03  \_ strace -fe pipe,execve tar cJf /tmp/docs.tgz /usr
9273 pts/1    t   0:03  |   \_ tar cJf /tmp/docs.tgz /usr/share/doc
9274 pts/1    t   0:00  |   \_ /bin/sh -c xz
9275 pts/1    t   0:27  |   \_ xz
9321 pts/1    R+  0:00  \_ ps f

fitz@ubuntu:~$ lsof -p 9273
COMMAND PID USER FD TYPE DEVICE SIZE/OFF NODE NAME
tar   9273 fitz  cwd DIR 8,2      4096  417609 /home/fitz
tar   9273 fitz  rtd DIR 8,2      4096   2 /
tar   9273 fitz  txt REG 8,2     452048  397186 /usr/bin/tar
tar   9273 fitz  0u  CHR 136,1    0t0   4 /dev/pts/1
tar   9273 fitz  1u  CHR 136,1    0t0   4 /dev/pts/1
tar   9273 fitz  2u  CHR 136,1    0t0   4 /dev/pts/1
tar   9273 fitz  3r  DIR 8,2     69632  409070 /usr/share/doc
tar   9273 fitz  4w FIFO 0,13    0t0   75234 pipe

fitz@ubuntu:~$ lsof -p 9275
COMMAND PID USER FD TYPE DEVICE SIZE/OFF NODE NAME
xz    9275 fitz  cwd DIR 8,2      4096  417609 /home/fitz
xz    9275 fitz  rtd DIR 8,2      4096   2 /
xz    9275 fitz  txt REG 8,2     80224  397427 /usr/bin/xz
xz    9275 fitz  0r  FIFO 0,13    0t0   75234 pipe
xz    9275 fitz  1w  REG 8,2 19365888  394591 /tmp/docs.tgz
xz    9275 fitz  2u  CHR 136,1    0t0   4 /dev/pts/1
xz    9275 fitz  3r  FIFO 0,13    0t0   75937 pipe
xz    9275 fitz  4w  FIFO 0,13    0t0   75937 pipe

Нужно отметить, что в процессе архиватора PID = 9273 файловый дескриптор передающей части канала сохранил свой номер, а в дочернем процессе упаковщика PID = 9375 файловый дескриптор принимающей части канала был перенаправлен на STDIN, как того и ожидает упаковщик xz(1).

4.9.2. Именованные каналы

Именованные каналы повторяют поведение неименованных каналов, но предназначены для обмена информацией между неродственными процессами. Любые две запущенные программы могут организовать однонаправленный канал передачи путем открытия файла канала по заранее согласованному имени на запись «с одной стороны» и на чтение «с другой». Файл канала должен быть предварительно создан в дереве каталогов при помощи специального системного вызова mkfifo(3), а