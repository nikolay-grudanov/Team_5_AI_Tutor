---
source_image: page_119.png
page_number: 119
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 37.41
tokens: 7727
characters: 2305
timestamp: 2025-12-24T04:35:24.951759
finish_reason: stop
---

bzImage (big zipped image), который состоит из программы распаковки и собственно запакованного стартового модуля.

В листинге 4.5 проиллюстрирован процесс извлечения стартового модуля из архива /boot/vmlinuz-3.13.0-49-generic формата bzImage ①, который предварительно копируется ② в /tmp/vmlinuz. Для извлечения используется сценарий extract-vmlinux ③ из пакета заголовочных файлов ядра. Распакованный ③ стартовый модуль /tmp/vmlinuz ожидаемо оказывается статически скомпонованной (т. е. не использующей библиотеки ELF shared object) исполняемой ELF-программой.

Листинг 4.5. Ядро операционной системы

fitz@ubuntu:~$ uname -r
5.3.0-23-generic
fitz@ubuntu:~$ file /boot/vmlinuz-5.3.0-23-generic
/boot/vmlinuz-5.3.0-23-generic: regular file, no read permission
fitz@ubuntu:~$ ls -l /boot/vmlinuz-5.3.0-23-generic
-rw------- 1 root root 11399928 ноя 12 11:51 /boot/vmlinuz-5.3.0-23-generic
fitz@ubuntu:~$ sudo file /boot/vmlinuz-5.3.0-23-generic
① /boot/vmlinuz-5.3.0-23-generic: Linux kernel x86 boot executable bzImage, version 5.3.0-23-generic (buildd@lgw01-amd64-002) #25-Ubuntu SMP Tue Nov 12 09:22:33 UTC 2019, RO-rootFS, swap_dev 0xA, Normal VGA
② fitz@ubuntu:~$ sudo cat /boot/vmlinuz-5.3.0-23-generic > /tmp/vmlinuz
③ fitz@ubuntu:~$ /usr/src/linux-headers-5.3.0-23/scripts/extract-vmlinux /tmp/vmlinuz > /tmp/vmlinux
fitz@ubuntu:~$ file /tmp/vmlinux
/tmp/vmlinux: ELF 64-bit LSB executable ③, x86-64, version 1 (SYSV), statically linked, BuildID[sha1]=b23ff3f6790319ec538278e3269af619ba2ca642, stripped

Динамические модули загружаются в пространство ядра и пристыковываются к стартовому модулю позднее, уже при работе операционной системы при помощи системных утилит insmod(8) или modprobe(8). Для отстыковки и выгрузки ненужных модулей предназначена системная утилита rmmod(8), для просмотра списка ① (см. листинг 4.6) загруженных модулей — lsmod(8), а для идентификации свойств и параметров ② модулей — утилита modinfo(8). Загрузка и выгрузка модулей реализуется специальными системными вызовами init_module(2) и delete_module(2), доступ к списку загруженных модулей — при помощи файла /proc/modules псевдофайловой системы proc(5), а идентификация свойств и параметров модулей — чтением специальных секций ELF-файлов модулей.

Листинг 4.6. Модули ядра

① fitz@ubuntu:~$ lsmod
Module Size Used by