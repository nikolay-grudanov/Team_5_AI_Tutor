---
source_image: page_423.png
page_number: 423
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 19.68
tokens: 7403
characters: 1860
timestamp: 2025-12-24T04:57:08.895098
finish_reason: stop
---

Уровни выполнения используются не только в качестве уровня по умолчанию в файле /etc/inittab. Их можно вызвать и с помощью самого демона init. Поэтому, если нужно немедленно остановить свой сервер, введите команду init в командной строке:

# init 0
...
System going down for system halt NOW!

Команда init принимает любые уровни выполнения из табл. 15.1, что позволяет быстро переключать сервер из одной категории уровней в другую. Например, если нужно устранить неполадки, которые требуют отключения графического интерфейса, введите команду init 3 в командной строке:

# init 3
INIT: Sending processes the TERM signal
starting irqbalance: [ OK ]
Starting setroubleshootd:
Starting fuse: Fuse filesystem already available.
...
Starting console mouse services: [ OK ]

Чтобы увидеть текущий уровень выполнения своего Linux-сервера, просто введите команду runlevel. Первый элемент вывода — это предыдущий уровень выполнения сервера, который в примере далее равен 5. Второй элемент вывода отображает текущий уровень выполнения сервера, который в примере равен 3:

$ runlevel
5 3

Кроме команды init, можно применять команду telinit, которая работает точно так же. В следующем примере команда telinit используется для перезагрузки сервера, переводя его на уровень выполнение 6:

# telinit 6
INIT: Sending processes the TERM signal
Shutting down smartd: [ OK ]
Shutting down Avahi daemon: [ OK ]
Stopping dhcdbd: [ OK ]
Stopping HAL daemon: [ OK ]
...
Starting killall:
Sending all processes the TERM signal... [ OK ]
Sending all processes the KILL signal... [ OK ]
...
Unmounting filesystems [ OK ]
Please stand by while rebooting the system
...

На только что запущенном сервере Linux текущий номер уровня выполнения должен совпадать с номером уровня по умолчанию в файле /etc/inittab. Однако обратите внимание на то, что предыдущий уровень выполнения в следующем