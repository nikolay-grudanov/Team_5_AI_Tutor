---
source_image: page_130.png
page_number: 130
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 30.71
tokens: 7623
characters: 2117
timestamp: 2025-12-24T04:35:36.203282
finish_reason: stop
---

4.3.2. Параллельные многонитевые программы

Для управления нитями в Linux используют стандартный POSIX-интерфейс pthreads(7), реализующийся библиотекой W:[NPTL], которая является частью библиотеки libc. Интерфейс предоставляет «нитевой» вызов создания нити pthread_create(3), который является условным аналогом «процессных» fork(2) и exec(3), вызов завершения и уничтожения нити pthread_exit(3), условно аналогичный exit(2), и вызов для получения статуса завершения нити pthread_join(3), условно аналогичный wait(2).

В качестве типичных примеров применения нитей можно привести сетевые сервисы, которые для параллельного обслуживания клиентских запросов используют нити вместо процессов. Например, WEB-сервер apache(8), как показано в листинге 4.14, использует два многонитевых процесса по 27 нитей в каждом, что позволяет экономить память (за счет работы всех нитей процесса с общей памятью) при обслуживании большого количества одновременных клиентских подключений.

Листинг 4.14. Параллельные многонитевые сервисы

fitz@ubuntu:~$ ps f -C apache2
PID TTY STAT TIME COMMAND
10129 ? Ss 0:00 /usr/sbin/apache2 -k start
10131 ? Sl 0:00 \_ /usr/sbin/apache2 -k start
10132 ? Sl 0:00 \_ /usr/sbin/apache2 -k start

fitz@ubuntu:~$ ps fo pid,nlwp,cmd -C apache2
PID NLWP CMD
10129 1 /usr/sbin/apache2 -k start
10131 27 \_ /usr/sbin/apache2 -k start
10132 27 \_ /usr/sbin/apache2 -k start

fitz@ubuntu:~$ ps -FLC rsyslogd
UID PID PPID LWP C NLWP STIME TTY TIME CMD
syslog 606 1 606 0 4 ноя18 ? 00:00:00 /usr/sbin/rsyslogd -n -iNONE
syslog 606 1 680 0 4 ноя18 ? 00:00:00 /usr/sbin/rsyslogd -n -iNONE
syslog 606 1 681 0 4 ноя18 ? 00:00:00 /usr/sbin/rsyslogd -n -iNONE
syslog 606 1 682 0 4 ноя18 ? 00:00:00 /usr/sbin/rsyslogd -n -iNONE

Аналогично, сервис централизованной журнализации событий rsyslogd(8) использует нити для параллельного сбора событийной информации из разных источников, ее обработки и журнализации. Одна нить считывает события ядра из /proc/kmsg, вторая принимает события других служб из файлового сокета /run/systemd/journal/syslog (/dev/log в ранних, до systemd системах), третья фильтрует поток принятых