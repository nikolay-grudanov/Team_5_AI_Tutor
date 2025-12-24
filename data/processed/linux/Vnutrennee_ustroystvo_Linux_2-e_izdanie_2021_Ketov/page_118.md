---
source_image: page_118.png
page_number: 118
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 35.73
tokens: 7697
characters: 2239
timestamp: 2025-12-24T04:35:19.692756
finish_reason: stop
---

fitz@ubuntu:~$ file /lib/x86_64-linux-gnu/libpcre2-8.so.0.7.1
/lib/x86_64-linux-gnu/libpcre2-8.so.0.7.1: ELF 64-bit LSB shared object, x86-64, version 1 (SYSV), dynamically linked, BuildID[sha1]=815e1acbce22015f05d62c17fe982c1b573125b1, stripped

fitz@ubuntu:~$ ldd /lib/x86_64-linux-gnu/libpcre2-8.so.0.7.1
    linux-vdso.so.1 (0x00007ffe22093000)
    libpthread.so.0 => /lib/x86_64-linux-gnu/libpthread.so.0 (0x00007f8ec2bdd000)
    libc.so.6 => /lib/x86_64-linux-gnu/libc.so.6 (0x00007f8ec29ec000)
    /lib64/ld-linux-x86-64.so.2 (0x00007f8ec2c99000)

Библиотеки имеют тот же бинарный формат W:[ELF], что и «запускаемые» программы, но не «запускаемый» executable, а «совместно используемый» shared object. Библиотеки, являясь пусть и незапускаемыми, но программами, естественным образом тоже зависят от других библиотек, что показано в листинге 4.3. Практически «запускаемость» ELF-файлов (листинг 4.4) зависит не от их типа, а от прав доступа и осмысленности точки входа — адреса первой инструкции, которой передается управление при попытке запуска. Например, библиотеку libc-2.30.so можно запустить, в результате чего будет выведена статусная информация.

Листинг 4.4. Запускаемые библиотеки

fitz@ubuntu:~$ ls -l /lib/x86_64-linux-gnu/libc-2.30.so
-rw-r--r-- 1 root root 2025032 сен 16 17:56 /lib/x86_64-linux-gnu/libc-2.30.so

fitz@ubuntu:~$ /lib/i386-linux-gnu/libc-2.15.so
GNU C Library (Ubuntu GLIBC 2.30-0ubuntu2) stable release version 2.30.
Copyright (C) 2019 Free Software Foundation, Inc.
This is free software; see the source for copying conditions.
There is NO warranty; not even for MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
Compiled by GNU CC version 9.2.1 20190909.
libc ABIs: UNIQUE IFUNC ABSOLUTE
For bug reporting instructions, please see:
<https://bugs.launchpad.net/ubuntu/+source/glibc/+bugs>.

4.1.1. Ядро Linux

Не стоит забывать, что самой главной программой операционной системы является ее ядро, которое в Linux состоит из статического стартового модуля (листинг 4.5) в формате ELF executable и динамически пристыковываемых программных модулей формата ELF relocatable (листинг 4.6). Для выполнения процедуры начальной загрузки стартовый модуль упакован в «самораспаковывающийся» gzip-архив формата