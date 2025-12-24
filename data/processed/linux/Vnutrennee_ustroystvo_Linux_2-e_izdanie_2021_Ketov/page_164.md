---
source_image: page_164.png
page_number: 164
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 9.82
tokens: 7093
characters: 521
timestamp: 2025-12-24T04:36:16.181136
finish_reason: stop
---

Рис. 4.5. Отображение файла в память

Листинг 4.37. Карта памяти процесса

fitz@ubuntu:~$ ps f
   PID TTY      STAT TIME COMMAND
26958 pts/0   Ss    0:00 bash
28540 pts/0   R+    0:00 \_ ps f
fitz@ubuntu:~$ which bash
/usr/bin/bash

fitz@ubuntu:~$ readelf -l /usr/bin/bash
Заголовки программы:
Тип        Смещ.        Вирт.адр        Физ.адр
          Рэм.файл     Рэм.пм           Флаги Выравн
(1) LOAD   0x000000000002d000 0x000000000002d000 0x000000000002d000
          0x00000000000ad78d 0x00000000000ad78d R E 0x1000