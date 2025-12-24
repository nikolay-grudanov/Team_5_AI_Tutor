---
source_image: page_174.png
page_number: 174
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 21.42
tokens: 7427
characters: 1393
timestamp: 2025-12-24T04:36:45.922425
finish_reason: stop
---

Сигналы могут быть перехвачены, если процесс назначит собственный обработчик, а также проигнорированы, тогда при их доставке вообще никакой обработчик не вызывается. Исключение составляют некоторые «безусловные» сигналы, такие как № 9 (SIGKILL) — безусловное завершение или № 19 (SIGSTOP) — безусловная приостановка процесса. Игнорирование и перехват сигналов показаны в листинге 4.46 на примере командного интерпретатора bash(1). Ни попытки «интерактивного» завершения ① при помощи сигналов SIGINT и SIGQUIT, ни явная посылка ② сигналов SIGINT и SIGTERM не приводят к завершению командного интерпретатора. К желаемому результату приводит только явная отсылка ③ сигнала SIGKILL.

Листинг 4.46. Игнорирование и перехват сигналов

fitz@ubuntu:~$ ps f
PID TTY STAT TIME COMMAND
23025 pts/1 S 0:00 -bash
23771 pts/1 R+ 0:00 \_ ps f

fitz@ubuntu:~$ bash
fitz@ubuntu:~$ ps f
PID TTY STAT TIME COMMAND
23025 pts/1 S 0:00 -bash
23636 pts/1 S 0:00 \_ bash
23692 pts/1 R+ 0:00 \_ ps f

① fitz@ubuntu:~$ ^C
① fitz@ubuntu:~$ ^\

fitz@ubuntu:~$ ps f
PID TTY STAT TIME COMMAND
23025 pts/1 S 0:00 -bash
! 23636 pts/1 S 0:00 \_ bash
23692 pts/1 R+ 0:00 \_ ps f

② fitz@ubuntu:~$ kill -SIGINT 23636
fitz@ubuntu:~$ ps f
PID TTY STAT TIME COMMAND
23025 pts/1 S 0:00 -bash
! 23636 pts/1 S 0:00 \_ bash
23701 pts/1 R+ 0:00 \_ ps f

② fitz@ubuntu:~$ kill -SIGTERM 23636
fitz@ubuntu:~$ ps f
PID TTY STAT TIME COMMAND