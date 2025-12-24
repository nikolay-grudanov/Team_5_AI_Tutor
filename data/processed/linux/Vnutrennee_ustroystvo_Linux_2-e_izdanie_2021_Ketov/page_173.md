---
source_image: page_173.png
page_number: 173
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 25.08
tokens: 7498
characters: 1481
timestamp: 2025-12-24T04:36:46.948127
finish_reason: stop
---

Управление процессами и памятью

мощи Ctrl+C или Ctrl+\. В этом случае используется сигнал штатного завершения № 15 (SIGTERM), что проиллюстрировано в листинге 4.44.

Листинг 4.44. Штатное завершение процесса (SIGTERM)

fitz@ubuntu:~$ dd if=/dev/zero of=/dev/null &
[1] 23444
fitz@ubuntu:~$ kill -SIGTERM 23444
fitz@ubuntu:~$
[1]+ Завершено    dd if=/dev/zero of=/dev/null

Для приостановки процесса, т. е. временного исключения его из процедур распределения процессорного времени планировщиком, предназначен сигнал № 19 (SIGSTOP), а для возобновления процесса — сигнал № 18 (SIGCONT). В листинге 4.45 показано, что приостановленный (stopped) процесс не потребляет процессорного времени.

Листинг 4.45. Приостановка и возобновление процесса (SIGSTOP и SIGCONT)

fitz@ubuntu:~$ pbzip2 big &
[1] 1647
fitz@ubuntu:~$ top -b -n1 -p 1647

PID USER PR NI VIRT RES SHR S %CPU %MEM TIME+ COMMAND
1647 fitz 20 0 102m 33m 900 S 387,0 0,4 0:25.09 pbzip2

fitz@ubuntu:~$ pkill -STOP pbzip2
fitz@ubuntu:~$ ps f
PID TTY STAT TIME COMMAND
1640 pts/2 Ss 0:00 -bash
1647 pts/2 Tl 0:24 \_ pbzip2 big
1651 pts/2 R+ 0:00 \_ ps f
fitz@ubuntu:~$ jobs -l
[1]+ 1647 Остановлен pbzip2 big
fitz@ubuntu:~$ top -b -n1 -p 1647

PID USER PR NI VIRT RES SHR S %CPU %MEM TIME+ COMMAND
1647 fitz 20 0 102m 34m 900 T 0,0 0,4 0:42.90 pbzip2

fitz@ubuntu:~$ kill -CONT 1647
fitz@ubuntu:~$ top -b -n1 -p 1647

PID USER PR NI VIRT RES SHR S %CPU %MEM TIME+ COMMAND
1647 fitz 20 0 102m 34m 900 S 370,0 0,4 0:51.82 pbzip2