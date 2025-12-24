---
source_image: page_149.png
page_number: 149
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 34.54
tokens: 7765
characters: 1996
timestamp: 2025-12-24T04:36:10.803860
finish_reason: stop
---

12058 pts/0   Ss    0:00 bash
12065 pts/0   R+    0:00  \_ ps f

fitz@ubuntu:~$ taskset -p -c 3 12058
pid 12058's current affinity list: 0-3
pid 12058's new affinity list: 3

fitz@ubuntu:~$ chrt -b 0 time bzip2 --best -kf plan9.iso &
[1] 12410
fitz@ubuntu:~$ chrt -o 0 time bzip2 --best -kf plan9.iso &
[2] 12412
fitz@ubuntu:~$ chrt -i 0 time bzip2 --best -kf plan9.iso & .
[3] 12414
fitz@ubuntu:~$ ps fo pid,pcpu,class,pri,ni,psr,cmd
PID %CPU CLS PRI NI PSR CMD
12058 0.1 TS 19 0 3 -bash
12410 0.0 B 19 - 3 \_ time bzip2 --best -kf plan9.iso
12411 50.0 B 19 - 3 \_ bzip2 --best -kf plan9.iso
12412 0.0 TS 19 0 3 \_ time bzip2 --best -kf plan9.iso
12413 49.7 TS 19 0 3 \_ bzip2 --best -kf plan9.iso
12414 0.0 IDL 19 - 3 \_ time bzip2 --best -kf plan9.iso
12415 0.1 IDL 19 - 3 \_ bzip2 --best -kf plan9.iso
12471 0.0 TS 19 0 3 \_ ps fo pid,pcpu,class,pri,ni,psr,cmd

fitz@ubuntu:~$ wait
53.85user 0.26system 1:45.98elapsed 51%CPU (0avgtext+0avgdata 31248maxresident)k
0inputs+180560outputs (0major+1004minor)pagefaults 0swaps
53.96user 0.22system 1:46.04elapsed 51%CPU (0avgtext+0avgdata 31248maxresident)k
0inputs+180560outputs (0major+1004minor)pagefaults 0swaps
52.74user 0.27system 2:41.54elapsed 32%CPU (0avgtext+0avgdata 31248maxresident)k
0inputs+180560outputs (0major+1004minor)pagefaults 0swaps

[1] Завершён chrt -b 0 time bzip2 --best -kf plan9.iso
[2]- Завершён chrt -o 0 time bzip2 --best -kf plan9.iso
[3]+ Завершён chrt -i 0 time bzip2 --best -kf plan9.iso

В листинге 4.30 показана конкуренция процессов под управлением RR-планировщика, использующего статические приоритеты. Так как операция назначения политик планирования «реального времени» FIFO и RR является привилегированной, то сначала 1 командный интерпретатор переводится в RR-класс (-r) с наивысшим статическим приоритетом 99 при помощи команды chrt(1), выполняемой от лица суперпользователя root. При последующих запусках упаковщиков класс будет унаследован и не потребует повышенных привилегий. Два процесса упаковщиков