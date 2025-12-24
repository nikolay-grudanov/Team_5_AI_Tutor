---
source_image: page_064.png
page_number: 64
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 31.82
tokens: 7628
characters: 2073
timestamp: 2025-12-24T04:33:44.937234
finish_reason: stop
---

В примере из листинга 3.1 в полном (-l, long) выводе команды ls(1) проиллюстрирован признак типа файла. Символом — обозначается обычный файл, символом b или c — специальные файлы блочного (block) или символьного (character) устройства, символом p — именованный канал (pipe), символом s — сокет (socket), а символом l — символическая ссылка (link).

Листинг 3.1. Признак типа файлов ls

finn@ubuntu:~$ ls -l /bin/ls /dev/sda /dev/tty /sbin/halt
-rwxr-xr-x 1 root root 142144 сен 5 13:38 /bin/ls
brw-rw---- 1 root disk 8, 0 ноя 17 03:31 /dev/sda
crw-rw-rw- 1 root tty 5, 0 ноя 17 12:18 /dev/tty
lrwxrwxrwx 1 root root 14 ноя 13 00:20 /sbin/halt -> /bin/systemctl

finn@ubuntu:~$ ls -l /run/initctl /run/udev/control
prw------- 1 root root 0 ноя 17 03:30 /run/initctl
srw------- 1 root root 0 ноя 17 03:30 /run/udev/control

3.2.1. Обычные файлы

Обычные файлы содержат пользовательскую информацию: текст, изображения, звук, видео и прочие данные в виде набора байтов (см. ② на рис. 3.2, листинг 3.2). За структуру содержания и имена обычных файлов ответственны прикладные программы, а операционная система не накладывает никаких ограничений.

Листинг 3.2. Содержание обычных файлов

finn@ubuntu:~$ file /usr/share/man/man1/file.1.gz
/usr/share/man/man1/file.1.gz: gzip compressed data, max compression, from Unix, original size modulo 2^32 21484

finn@ubuntu:~$ file /etc/passwd
/etc/passwd: ASCII text

finn@ubuntu:~$ file /bin/ls
/bin/ls: ELF 64-bit LSB pie executable, x86-64, version 1 (SYSV), dynamically linked, interpreter /lib64/ld-linux-x86-64.so.2,
BuildID[sha1]=2f15ad836be3339dec0e2e6a3c637e08e48aacbd, for GNU/Linux 3.2.0, stripped

finn@ubuntu:~$ file /usr/share/sounds/alsa/Noise.wav
/usr/share/sounds/alsa/Noise.wav: RIFF (little-endian) data, WAVE audio, Microsoft PCM, 16 bit, mono 48000 Hz

finn@ubuntu:~$ file /usr/share/backgrounds/Sky_Sparkles_by_Joe_Thompson.jpg
/usr/share/backgrounds/Sky_Sparkles_by_Joe_Thompson.jpg: JPEG image data, JFIF standard 1.01, aspect ratio, density 1x1, segment length 16, progressive, precision 8, 3840x2160, components 3