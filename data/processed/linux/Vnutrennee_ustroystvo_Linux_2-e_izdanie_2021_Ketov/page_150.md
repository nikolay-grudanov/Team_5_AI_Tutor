---
source_image: page_150.png
page_number: 150
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 25.87
tokens: 7587
characters: 1572
timestamp: 2025-12-24T04:36:06.470421
finish_reason: stop
---

запускаются 2 командой chrt(1) с одинаковыми статическими приоритетами 1, привязанные одному процессору командой taskset(1), в результате чего получают равные доли процессорного времени, что вполне соответствует интуитивным ожиданиям от вытесняющего циклического планировщика RR. Нужно отметить, что шкала статических приоритетов 1→99 классов RR и FIFO, как и шкала «любезности» NICE +19 →-20 классов TS и B, отображаются на общую шкалу приоритетов PRI так, что верхняя часть шкалы PRI: 41→139 соответствует статическим приоритетам, а нижняя часть шкалы PRI: 0→39 соответствует «любезности».

Листинг 4.30. Классы процессов реального времени

fitz@ubuntu:~$ ps f
PID TTY STAT TIME COMMAND
- 15313 pts/0 S 0:00 -bash
15520 pts/0 R+ 0:00 \_ ps f

fitz@ubuntu:~$ sudo chrt -pr 99 15313
fitz@ubuntu:~$ ps fo pid,psr,cls,ni,pri,pcpu,comm
PID PSR CLS NI PRI %CPU COMMAND
15313 0 RR - 139 0.1 bash
15550 1 RR - 139 0.0 \_ ps

fitz@ubuntu:~$ chrt -r 1 taskset -c 2 bzip2 --best -kf plan9.iso &
[1] 15572
fitz@ubuntu:~$ chrt -r 1 taskset -c 2 bzip2 --best -kf plan9.iso &
[2] 15573
fitz@ubuntu:~$ ps fo pid,psr,cls,ni,pri,pcpu,comm
PID PSR CLS NI PRI %CPU COMMAND
15313 0 RR - 139 0.1 bash
15572 2 RR - 41 51.8 \_ bzip2
15573 2 RR - 41 48.8 \_ bzip2
15597 1 RR - 139 0.0 \_ ps

fitz@ubuntu:~$ chrt -r 2 taskset -c 2 bzip2 --best -kf plan9.iso &
[3] 15628
fitz@ubuntu:~$ ps fo pid,psr,cls,ni,pri,pcpu,comm
PID PSR CLS NI PRI %CPU COMMAND
15313 0 RR - 139 0.1 bash
15572 2 RR - 41 48.3 \_ bzip2
★ 15573 2 RR - 41 47.5 \_ bzip2
15628 2 RR - 42 93.3 \_ bzip2
15630 1 RR - 139 0.0 \_ ps