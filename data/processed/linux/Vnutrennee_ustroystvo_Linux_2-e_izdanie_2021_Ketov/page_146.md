---
source_image: page_146.png
page_number: 146
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 26.20
tokens: 7569
characters: 1816
timestamp: 2025-12-24T04:35:59.047739
finish_reason: stop
---

При отсутствии конкуренции, когда количество готовых к выполнению задач равно количеству свободных процессоров, приоритет не будет играть никакой роли.

В примере из листинга 4.28 при помощи команды bzip(2) запущены два процесса сжатия ISO-образа с наилучшим качеством одновременно друг другу на «заднем фоне». В выводе свойств pcru (регсент cpu, процент потребляемого процессорного времени), pri (priority), ni (nice) и psr (processor number) их процессов при помощи ps(1) оказывается, что они потребляют практически одинаковые доли (проценты) процессорного времени, и это для одинаковых программ вполне соответствует интуитивным ожиданиям. После повышения любезности (понижения относительного приоритета) одного из них при помощи команды renice(1) до значения +10 отношение потребляемых долей процессорного времени не изменилось, что означает отсутствие конкуренции за процессор, подтверждаемое как столбцом PSR, показывающим номер процессора, выполняющего программу, так и командами nproc(1) и lscpu(1).

Листинг 4.28. Относительный приоритет NICE

fitz@ubuntu:~$ bzip2 --best -kf plan9.iso &
[1] 12944
fitz@ubuntu:~$ bzip2 --best -kf plan9.iso &
[2] 12945
fitz@ubuntu:~$ ps fo pid,pcpu,pri,ni,psr,cmd
PID %CPU PRI NI PSR CMD
12808 0.1 19 0 0 -bash
12944 94.5 19 0 2 \_ bzip2 --best -kf plan9.iso
12945 96.0 19 0 1 \_ bzip2 --best -kf plan9.iso
12946 0.0 19 0 3 \_ ps fo pid,pcpu,pri,ni,psr,cmd

fitz@ubuntu:~$ renice +10 12945
12945 (process ID) old priority 0, new priority 10
fitz@ubuntu:~$ ps fo pid,pcpu,pri,ni,psr,cmd
PID %CPU PRI NI PSR CMD
12808 0.1 19 0 0 -bash
12944 94.8 19 0 -2 \_ bzip2 --best -kf plan9.iso
12945 97.0 9 10 -0 \_ bzip2 --best -kf plan9.iso
12948 0.0 19 0 1 \_ ps fo pid,pcpu,pri,ni,psr,cmd
fitz@ubuntu:~$ nproc
4
fitz@ubuntu:~$ lscpu
Архитектура: x86_64
CPU op-mode(s): 32-bit, 64-bit