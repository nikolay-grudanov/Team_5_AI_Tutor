---
source_image: page_116.png
page_number: 116
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 39.09
tokens: 7750
characters: 2242
timestamp: 2025-12-24T04:35:22.585742
finish_reason: stop
---

последовательно. Однако если выделить «независимые» поднаборы инструкций (независимые ветви), то их можно выполнять несколькими исполнителями одновременно — параллельно. Поэтому различают последовательные и параллельные алгоритмы и соответствующие им последовательные и параллельные программы. Некоторые программы реализуют алгоритмы общего назначения, например алгоритмы сжатия или шифрования информации, алгоритмы сетевых протоколов и т. д. Такие программы, востребованные не столько конечными пользователями, сколько другими программами, называют библиотеками.

Согласно hier(7), откомпилированные до машинного языка программы размещаются в каталогах /bin, /sbin, /usr/bin, /usr/sbin, /usr/local/bin, /usr/local/sbin, а библиотеки — в каталогах /lib, /usr/lib, /usr/local/lib. Программы имеют специальный бинарный «запускаемый» формат W:[ELF] executable и зависят от библиотек, что проиллюстрировано в листинге 4.1 при помощи команды ldd(1) (loader dependencies). Каждая зависимость отображается именем библиотеки ① (SONAME, shared object name), найденным в системе файлом библиотеки ② и адресом¹ в памяти процесса ③ (32- или 48-битным, в зависимости от платформы), куда библиотека будет загружена.

Листинг 4.1. Программы и библиотеки

fitz@ubuntu:~$ which ls
/usr/bin/ls
fitz@ubuntu:~$ file /usr/bin/ls
/usr/bin/ls: ELF 64-bit LSB pie executable, x86-64, version 1 (SYSV), dynamically linked, interpreter /lib64/ld-linux-x86-64.so.2,
BuildID[sha1]=2f15ad836be3339dec0e2e6a3c637e08e48aacbd, for GNU/Linux 3.2.0, stripped
fitz@ubuntu:~$ ldd /usr/bin/ls
linux-vdso.so.1 (0x00007ffc529d000)
libsdlinux.so.1 => /lib/x86_64-linux-gnu/libsdlinux.so.1 (0x00007fb02f58d000)
① libc.so.6 => ② /lib/x86_64-linux-gnu/libc.so.6 (0x00007fb02f39c000) ③
libpcre2-8.so.0 => /lib/x86_64-linux-gnu/libpcre2-8.so.0 (0x00007fb02f317000)
libdl.so.2 => /lib/x86_64-linux-gnu/libdl.so.2 (0x00007fb02f311000)
/lib64/ld-linux-x86-64.so.2 (0x00007fb02f5f1000)
libpthread.so.0 => /lib/x86_64-linux-gnu/libpthread.so.0 (0x00007fb02f2ee000)

fitz@ubuntu:~$ file /lib/x86_64-linux-gnu/libc.so.6
④ /lib/x86_64-linux-gnu/libc.so.6: symbolic link to libc-2.30.so

¹ Для противодействия эксплуатации уязвимости в программах адрес выбирается случайным образом, см. W:[ASLR].