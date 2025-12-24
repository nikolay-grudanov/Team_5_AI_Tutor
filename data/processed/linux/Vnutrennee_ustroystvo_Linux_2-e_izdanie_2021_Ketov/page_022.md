---
source_image: page_022.png
page_number: 22
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 43.01
tokens: 7890
characters: 2187
timestamp: 2025-12-24T04:32:46.305880
finish_reason: stop
---

ся, что эти библиотечные функции находятся в библиотеке языка Си, что весьма ожидаемо в силу внутреннего устройства операционной системы (см. рис. 1.1).

Листинг 1.2. Трассировщик системных вызовов ltrace

bart@ubuntu:~$ ltrace -x *time*+fwrite date
clock_gettime@libc.so.6(0, 0x7ffc8601a300, 1, 0x56056f3b04c0) = 0
localtime_r@libc.so.6(0x7ffc8601a230, 0x7ffc8601a240, 4, 269) = 0x7ffc8601a240
strftime@libc.so.6( <unfinished ...>
    strftime_l@libc.so.6(0x7ffc86019db0, 1024, 0x7ffc86019dab, 0x7ffc8601a240) = 5
<... strftime resumed> "\320\241\320\261", 1024, "%a", 0x7ffc8601a240) = 5
fwrite@libc.so.6("\320\241\320\261", 4, 1, 0x7f3d7e8d56a0) = 1
strftime@libc.so.6( <unfinished ...>
    strftime_l@libc.so.6(0x7ffc86019db0, 1024, 0x7ffc86019dab, 0x7ffc8601a240) = 7
<... strftime resumed> "\320\275\320\276\321\217", 1024, "%b", 0x7ffc8601a240) = 7
fwrite@libc.so.6("\320\275\320\276\321\217", 6, 1, 0x7f3d7e8d56a0) = 1
fwrite@libc.so.6("16", 2, 1, 0x7f3d7e8d56a0) = 1
fwrite@libc.so.6("20", 2, 1, 0x7f3d7e8d56a0) = 1
fwrite@libc.so.6("5", 1, 1, 0x7f3d7e8d56a0) = 1
fwrite@libc.so.6("9", 1, 1, 0x7f3d7e8d56a0) = 1
fwrite@libc.so.6("MSK", 3, 1, 0x7f3d7e8d56a0) = 1
fwrite@libc.so.6("2019", 4, 1, 0x7f3d7e8d56a0) = 1
Сб ноя 16 20:05:09 MSK 2019
+++ exited (status 0) +++

1.5. Интерфейсы прикладного программирования

Системные и библиотечные вызовы Linux, формирующие интерфейс прикладного программирования (API, application programming interface), соответствуют определенным промышленным спецификациям, в частности (практически идентичным друг другу) стандартам W:[POSIX]¹, Portable Operating System Interface и SUS, W:[Single UNIX Specification], доставшимся «в наследство» от семейства операционных систем UNIX, членом которого Linux и является.

Стандарт POSIX условно делится на две части: POSIX.1, программный интерфейс (API) операционной системы, и POSIX.2, интерфейс командной строки (CLI) пользователя (см. главу 2) и командный интерпретатор (см. главу 5).

¹ Стандарт POSIX выпускается комитетом 1003 организации W:[IEEE], поэтому имеет формальное обозначение IEEE 1003, а части стандарта POSIX.1 и POSIX.2 формально обозначаются IEEE 1003.1 и IEEE 1003.2 соответственно.