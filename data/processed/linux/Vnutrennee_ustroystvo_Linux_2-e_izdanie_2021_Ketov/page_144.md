---
source_image: page_144.png
page_number: 144
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 22.07
tokens: 7410
characters: 1564
timestamp: 2025-12-24T04:35:51.574384
finish_reason: stop
---

CAP_NET_RAW при помощи «файловых» привилегий CAP_NET_RAW для программы захвата /usr/bin/dumpcap, что и проиллюстрировано¹ в листинге 4.25.

4.5.3. Другие атрибуты

Переменные окружения (листинг 4.26) и текущий рабочий каталог (листинг 4.27) на поверку тоже оказываются атрибутами процесса, которые можно получить при помощи команд ps(1) и pwdx(1) соответственно.

Листинг 4.26. Переменные окружения процесса

fitz@ubuntu:~$ ps fe
PID TTY STAT TIME COMMAND
21872 pts/2 S 0:00 -bash USER=fitz LOGNAME=fitz HOME=/home/fitz PATH=/usr/...
22904 pts/2 R+ 0:00 \_ ps fe LANGUAGE=ru:ko:en LC_ADDRESS=ru_RU.UTF-8 ...

Листинг 4.27. Текущий рабочий каталог процесса

fitz@ubuntu:~$ ps fx
PID TTY STAT TIME COMMAND
22984 pts/0 S 0:00 -bash
23086 pts/0 S+ 0:00 \_ man ps
23097 pts/0 S+ 0:00 \_ pager
21872 pts/2 S 0:00 -bash
23103 pts/2 R+ 0:00 \_ ps fx

fitz@ubuntu:~$ pwdx 23097 22984
23097: /home/fitz
22984: /home/fitz

4.6. Классы и приоритеты процессов

4.6.1. Распределение процессора между процессами

Переключение центрального процессора между задачами (процессами и нитями) выполняет специальная компонента подсистемы управления процессами, называемая планировщиком (scheduler). Именно планировщик определенным образом

¹ Необходимо заметить, что все это уже достаточно давно умеет проделывать инсталлятор при установке пакета wireshark-common (от которого зависят пакеты tshark и wireshark), если утвердительно ответить на вопрос инсталлятора 'Should non-superusers be able to capture packets?'. Однако для более простого tcpdump(8) такой услуги не предоставлено ☺.