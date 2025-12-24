---
source_image: page_315.png
page_number: 315
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 24.07
tokens: 7506
characters: 1906
timestamp: 2025-12-24T04:41:06.570955
finish_reason: stop
---

homer@ubuntu:~$ Xnest :1 -auth cookie-jar - &
homer@ubuntu:~$ ssh lich@centos

Last login: Fri Jan 8 17:43:04 2016 from ubuntu
[lich@centos ~]$ xauth
xauth: file /home/lich/.Xauthority does not exist
Using authority file /home/lich/.Xauthority
xauth> add ubuntu.local:1 MIT-MAGIC-COOKIE-1 8f36c904dc0c9934c506c21ea7860eb2
xauth> exit
Writing authority file /home/lich/.Xauthority
[lich@centos ~]$ logout
Connection to centos closed.
homer@ubuntu:~$ ssh -f lich@centos "DISPLAY=ubuntu.local:1 xeyes"

Необходимость установки общего секрета, переменной окружения DISPLAY и запуска дополнительного виртуального X-сервера (или активации приема сетевых соединений аппаратным сервером) делают «ручной» запуск дистанционных X-клиентов неудобным «чуть более чем полностью». Вместе с этим передача «волшебных печеньек» (как и любых других сообщений X-протокола) от X-клиента к X-серверу по сети происходит незащищенным образом, что может быть легко использовано злоумышленником. Именно поэтому на практике используют туннелирующие возможности протокола SSH, позволяющие удобным автоматизированным способом решить все вышеперечисленные задачи и проблемы.

В примере из листинга 7.27 показано поведение SSH-сервера при туннелировании X-протокола. По запросу (-X) от SSH-клиента SSH-сервер начинает эмулировать поведение X-сервера, устанавливает переменную окружения DISPLAY, указывающую на «дисплей» :10 на «том же» узле localhost, и создает «волшебную печеньку» для этого дисплея.

При последующем запуске X-клиента xeyes(1) им будет установлено соединение с «SSH-эмулятором» X-сервера на localhost:10, а SSH-сервер перенаправит (туннелирует) это соединение X-протокола обратно SSH-клиенту внутри зашифрованного соединения SSH.

Листинг 7.27. SSH-туннелирование X-протокола (SSH-сервер)

homer@ubuntu:~$ ssh -X lich@centos
Last login: Fri Jan 8 17:48:34 2016 from ubuntu
[lich@centos ~]$ echo $DISPLAY
localhost:10.0