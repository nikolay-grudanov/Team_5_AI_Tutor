---
source_image: page_147.png
page_number: 147
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 30.15
tokens: 7666
characters: 1984
timestamp: 2025-12-24T04:36:06.020156
finish_reason: stop
---

Управление процессами и памятью

Порядок байт: Little Endian
Address sizes: 36 bits physical, 48 bits virtual
CPU(s): 4
On-line CPU(s) list: 0-3

1 fitz@ubuntu:~$ taskset -p -c 3 12808
pid 12808's current affinity list: 0-3
pid 12808's new affinity list: 3

2 fitz@ubuntu:~$ nice -n 5 time bzip2 --best -kf plan9.iso &
[1] 29331

3 fitz@ubuntu:~$ nice -n 15 time bzip2 --best -kf plan9.iso &
[2] 29333

fitz@ubuntu:~$ ps fo pid,pcpu,pri,ni,psr,cmd
PID %CPU PRI NI PSR CMD
28573 0.0 19 0 3 -bash
29331 0.0 9 5 3 \_ time bzip2 --best -kf plan9.iso
29332 91.4 9 5 3 \_ bzip2 --best -kf plan9.iso
29333 0.0 4 15 3 \_ time bzip2 --best -kf plan9.iso
29334 9.7 4 15 3 \_ bzip2 --best -kf plan9.iso
29336 0.0 19 0 3 \_ ps fo pid,pcpu,pri,ni,psr,cmd

fitz@ubuntu:~$ wait
51.10user 0.22system 0:56.86elapsed 90%CPU (0avgtext+0avgdata 31248maxresident)k
0inputs+180560outputs (0major+1004minor)pagefaults 0swaps
[1]- Завершён nice -n 5 time bzip2 --best -kf plan9.iso
53.79user 0.20system 1:43.08elapsed 52%CPU (0avgtext+0avgdata 31520maxresident)k
0inputs+180560outputs (0major+1515minor)pagefaults 0swaps
[2]+ Завершён nice -n 15 time bzip2 --best -kf plan9.iso

Проиллюстрировать действие относительного приоритета NICE на многопроцессорной системе можно, создав искусственную конкуренцию двух процессов за один процессор. Для этого при помощи команды taskset(1) устанавливается привязка (affinity) 1 командного интерпретатора (PID = 12808) к процессору 3 (привязка, как и прочие свойства и атрибуты процесса, наследуется потомками). Затем при помощи команды nice(1) запускаются 3 две программы упаковки с относительными приоритетами 5 и 15 в режиме измерения потребления времени при помощи команды time(1). В результате доли процессорного времени распределяются неравномерно, причем их разница зависит от разницы в относительных приоритетах (и от свойств конкурирующих процессов, но в примере они одинаковые). Дождавшись завершения процессов заднего фона, при помощи встроенной команды wait