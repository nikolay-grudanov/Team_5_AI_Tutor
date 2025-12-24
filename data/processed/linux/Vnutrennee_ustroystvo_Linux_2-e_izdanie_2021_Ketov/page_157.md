---
source_image: page_157.png
page_number: 157
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 21.69
tokens: 7446
characters: 2002
timestamp: 2025-12-24T04:36:15.724704
finish_reason: stop
---

Управление процессами и памятью

fitz@ubuntu:~$ echo deadline | sudo tee /sys/block/sr0/queue/scheduler
deadline

fitz@ubuntu:~$ cat /sys/block/sr0/queue/scheduler
noop [deadline] -> cfq

Листинг 4.31 показывает, что назначенный блочному устройству планировщик можно узнать только при помощи «прямого» чтения файловой системы sysfs, а выбрать иной планировщик при помощи «прямой» записи в ее файлы. Нужно отметить, что планировщик noop (по определению), как можно догадаться из названия, (почти) ничего с поступающими запросами не делает, но именно поэтому идеально подходит для недисковых устройств, например SSD-накопителей, задержки доступа к данным которых никак не определяются механической составляющей, присущей «обычным», дисковым накопителям.

Листинг 4.32. Параметры I/O планировщика CFQ

fitz@ubuntu:~$ ls /sys/block/sda/queue/iосched/
back_seek_max    group_idle_us    slice_async_us    target_latency
back_seek_penalty    low_latency    slice_idle    target_latency_us
fifo_expire_async    quantum    slice_idle_us
fifo_expire_sync    slice_async    slice_sync
group_idle    slice_async_rq    slice_sync_us

1 fitz@ubuntu:~$ cat /sys/block/sda/queue/iосched/slice_sync
100

2 fitz@ubuntu:~$ cat /sys/block/sda/queue/iосched/slice_async
40

3 fitz@ubuntu:~$ cat /sys/block/sda/queue/iосched/fifo_expire_*
250
125

4 fitz@ubuntu:~$ cat /sys/block/sda/queue/iосched/slice_idle
8

Широкое распространение сверхбыстрых твердотельных накопителей, например W:[NVMe], поставило перед разработчиками ядра Linux новые задачи, т. к. оказалось, что подсистема блочных устройств в силу внутреннего строения в принципе не способна обрабатывать большое количество запросов на чтение/запись в единицу времени W:[IOPS], что не позволяет использовать такие накопители на «полную катушку». При разработке ядер серии 4.x блочную систему перепроектировали и изменили принцип организации запросов, поступающих к блочному устройству на обработку. Вместо одной общей входящей очереди (single queue) к каждому уст-