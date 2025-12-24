---
source_image: page_185.png
page_number: 185
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 24.99
tokens: 7445
characters: 1421
timestamp: 2025-12-24T04:37:10.909383
finish_reason: stop
---

22261 ? Ss 0:00 SCREEN
22262 pts/2 Ss+ 0:00 \_ /bin/bash
22263 pts/2 S+ 0:10 \_ /usr/bin/python3 /usr/bin/youtube-dl ...
28020 pts/4 Ss+ 0:00 \_ /bin/bash
fitz@ubuntu:~$ logout

Первичный сеанс
fitz@somewhere:~$ ssh ubuntu
No mail.
Last login: Sat Nov 23 01:01:04 2019 from 10.0.2.2
fitz@ubuntu:~$ screen -ls
There is a screen on:
    22261.pts-14.ubuntu    (23.11.2019 01:01:06)   (Detached)
1 Socket in /run/screen/S-fitz.
fitz@ubuntu:~$ ls -l /run/screen/S-fitz
итого 0
srwx------ 1 fitz fitz 0 ноя 20 00:40 22261.pts-14.ubuntu
fitz@ubuntu:~$ screen -r

Продолжаем вторичный сеанс #2
fitz@ubuntu:~$ tty
/dev/pts/4
fitz@ubuntu:~$ ^D

Продолжаем вторичный сеанс #1
[download] 100% of 219.30MiB in 06:28
[dashsegments] Total fragments: 246
[download] Destination: Основы Linux - командная строка-kbEKbmpZKzo.f251.webm
[download] 100% of 26.45MiB in 00:19
[ffmpeg] Merging formats into "Основы Linux - командная строка-kbEKbmpZKzo.webm"
Deleting original file Основы Linux - командная строка-kbEKbmpZKzo.f248.webm (pass -k to keep)
Deleting original file Основы Linux - командная строка-kbEKbmpZKzo.f251.webm (pass -k to keep)
fitz@ubuntu:~$ tty
/dev/pts/2
fitz@ubuntu:~$ ^D
[screen is terminating]

4.9.5. Разделяемая память, семафоры и очереди сообщений

Разделяемая память

Каналы и сокеты являются удобными средствами обмена информацией между процессами, но их использование при интенсивном обмене или обмене объемными