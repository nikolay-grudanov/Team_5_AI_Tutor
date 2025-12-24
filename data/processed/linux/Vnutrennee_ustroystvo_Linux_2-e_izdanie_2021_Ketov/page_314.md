---
source_image: page_314.png
page_number: 314
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 25.63
tokens: 7532
characters: 1900
timestamp: 2025-12-24T04:41:06.103816
finish_reason: stop
---

В большинстве случаев для дистанционного запуска используется ssh(1), что проиллюстрировано в листинге 7.25. Попытка ① «прямого» запуска xeyes(1) на узле centos от лица пользователя lich не увенчалась успехом потому, что в большинстве инсталляций аппаратный X-сервер на дисплее :0 не принимает сетевые соединения (см. листинг 7.25). Попытка ② запуска локального виртуального сервера Xnest(1) на дисплее :1 с перенаправлением ему вывода дистанционного xeyes(1) тоже оказалась неудачной, но уже по другим причинам (см. далее).

Листинг 7.25. Запуск дистанционного X клиента

① homer@ubuntu:~$ ssh -f lich@centos "DISPLAY=ubuntu.local:0 xeyes"
Error: Can't open display: ubuntu.local:0

② homer@ubuntu:~$ Xnest :1 &
homer@ubuntu:~$ ssh -f lich@centos "DISPLAY=ubuntu.local:1 xeyes"
- No protocol specified
Error: Can't open display: ubuntu.local:1

При сетевом взаимодействии X-клиентов и X-сервера для аутентификации клиентских подключений используется механизм, основанный на предъявлении общего (известного обеим сторонам) «секрета», называемого «волшебной печенькой» (см. W:[magic cookie]), использование которой проиллюстрировано в примере из листинга 7.26.

На стороне сервера «печеньки» всех клиентов, которым разрешено подключение, размещаются при помощи утилиты xauth(1) в «банке с печеньками» (jar) ①, откуда извлекаются сервером для проверки при подключении клиента. На стороне клиента «печеньки» при помощи той же утилиты xauth(1) размещаются ② в «банке» ~/.Xauthority, откуда извлекаются библиотекой Xlib для предъявления серверу при соединении с ним.

Листинг 7.26. Аутентификация дистанционного X-клиента

homer@ubuntu:~$ mcookie
8f36c904dc0c9934c506c21ea7860eb2
① homer@ubuntu:~$ xauth -f cookie-jar
xauth: file cookie-jar does not exist
Using authority file cookie-jar
xauth> add ubuntu:1 MIT-MAGIC-COOKIE-1 8f36c904dc0c9934c506c21ea7860eb2
xauth> exit
Writing authority file cookie-jar