---
source_image: page_159.png
page_number: 159
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 33.20
tokens: 7560
characters: 1862
timestamp: 2025-12-24T04:36:32.301616
finish_reason: stop
---

Листинг 4.34. I/O классы процессов планировщиков CFQ и BFQ

fitz@ubuntu:~$ ionice -p $$
none: prio 0
fitz@ubuntu:~$ ionice -c best-effort -n 5 -p $$
fitz@ubuntu:~$ ionice -p $$
best-effort: prio 5
fitz@ubuntu:~$ sudo ionice -c realtime -n 3 -p $$
fitz@ubuntu:~$ ionice -p $$
realtime: prio 3

В листинге 4.35 проведены два опыта, в которых сравнивается распределение пропускной способности при чтении с дискового накопителя /dev/sdc между двумя одинаковыми процессами. Если процессы имеют одинаковый класс и приоритет ①, то в результате и получают одинаковую долю пропускной способности диска ①, а если разные ① приоритеты, то пропорциональную ①. В принципе доля пропускной способности должна была распределиться как 40 мс/(40 мс + 180 мс) ≈ 0,18 и 180 мс/(40 мс + 180 мс) ≈ 0,82 согласно длительностям интервалов обработки, выделяемой очередям планировщиком (см. выше). Полученный результат отличается от прогнозируемого потому, что один процесс заканчивает копирование раньше другого на целых 4 с, что составляет примерно 30% общего времени копирования, поэтому второй заканчивает свое чтение, уже используя полную пропускную способность диска. Поэтому средние (!) скорости копирования в 1,5 и 2,2 Мбит/с и не соотносятся как 0,18 к 0,82.

Листинг 4.35. Распределение пропускной способности планировщиками CFQ и BFQ

fitz@ubuntu:~$ findmnt -T .
TARGET SOURCE FSTYPE OPTIONS
/ /dev/sda4 ext4 rw,relatime,errors=remount-ro
fitz@ubuntu:~$ cat /sys/block/sda/queue/scheduler
noop deadline [cfq]
fitz@ubuntu:~$ dd if=/dev/urandom of=big1 bs=16384 count=1024
1024+0 записей получено
1024+0 записей отправлено
16777216 bytes (17 MB, 16 MiB *) copied, 0,089367 s, 188 MB/s
fitz@ubuntu:~$ dd if=/dev/urandom of=big2 bs=16384 count=1024
...
fitz@ubuntu:~$ sync
① fitz@ubuntu:~$ dd if=big1 of=/dev/null iflag=direct &
fitz@ubuntu:~$ dd if=big2 of=/dev/null iflag=direct &