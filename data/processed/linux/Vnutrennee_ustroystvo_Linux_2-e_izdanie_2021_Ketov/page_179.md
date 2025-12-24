---
source_image: page_179.png
page_number: 179
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 25.07
tokens: 7454
characters: 1720
timestamp: 2025-12-24T04:36:57.420597
finish_reason: stop
---

Утилита schedtool(1) из одноименного пакета schedtool заменяет "стандартные" taskset/nice/renice/chrt.

^D

Cc:-

fitz@ubuntu:~$

При «одновременном» выводе информации на один терминал несколькими процессами результат точно так же непредсказуем, как и при вводе. В итоге будет получена смесь перемежающихся строчек разных процессов, однако по умолчанию вывод (output) разрешен как процессам группы «переднего» фона, так и процессам всех групп «заднего» фона. Настроочный флаг драйвера терминала tostop (terminal output stop) позволяет запретить вывод из заднего фона так же, как и ввод. При запрещенном выводе из заднего фона все попытки будут подавляться сигналом SIGTTOU (terminal stop on output signal), приостанавливающим процесс. В листинге 4.50 проиллюстрировано действие сигнала SIGTTOU при включении настроечного флага tostop посредством команды stty(1).

Листинг 4.50. Приостановка при выводе из заднего фона (SIGTTOU)

fitz@ubuntu:~$ find / -type f -size 0 &

fitz@ubuntu:~$ stty -a
speed 38400 baud; rows 24; columns 80; line = 0;
isig icanon iexten echo ... -echonl -noflsh -xcase -tostop -echoprt echoctl echoke

fitz@ubuntu:~$ stty tostop
fitz@ubuntu:~$ find / -type f -size 0 &
[1] 356
fitz@ubuntu:~$ jobs -l
[1]+ 356 Остановлено (вывод на терминал) find / -type f -size 0
fitz@ubuntu:~$ ps f
   PID TTY      STAT TIME COMMAND
 32535 pts/1   S    0:00 -bash
 356 pts/1     T    0:00 \_ find / -type f -size 0
 360 pts/1     R+   0:00 \_ ps f

4.9. Межпроцессное взаимодействие

Кроме сигналов, которые могут использоваться как простейшие средства межпроцессного взаимодействия (IPC, inter-process communication), для эффективного обмена информацией между процессами применяются каналы, сокеты, очереди со-