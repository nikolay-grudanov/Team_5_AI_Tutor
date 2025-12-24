---
source_image: page_292.png
page_number: 292
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 42.63
tokens: 7732
characters: 1822
timestamp: 2025-12-24T04:40:45.260315
finish_reason: stop
---

Именно X-сервер принимает подключения от X-клиентов и согласно их запросам создает окна, изменяет их размер, отображает или скрывает окна на дисплеях, сообщает положение курсора, рисует текст, линии, точки, прямоугольники, дуги, полигоны и пр. В обратную сторону X-сервер отправляет X-клиентам информацию о событиях (events) нажатия клавиш, кнопок мыши и планшетов, оповещает о движении курсора и т. д.

Листинг 7.1. Аппаратный X-сервер

homer@ubuntu:~$ pgrep -l Xorg
6892 Xorg

homer@ubuntu:~$ ps o pid,tty,cmd p 6892
PID TT CMD
6892 tty3 /usr/lib/xorg/Xorg vt3 -displayfd 3 -auth /run/user/1000/gdm/Xauthority ...

(1) homer@ubuntu:~$ lsof -p 6892 -a /dev
COMMAND PID USER FD TYPE DEVICE SIZE/OFF NODE NAME
Xorg 6892 homer mem CHR 226,0 439 /dev/dri/card0
Xorg 6892 homer 0u CHR 4,3 0t0 24 /dev/tty3
Xorg 6892 homer 11u CHR 4,3 0t0 24 /dev/tty3 @
Xorg 6892 homer 12u CHR 226,0 0t0 439 /dev/dri/card0
Xorg 6892 homer 16u CHR 226,0 0t0 439 /dev/dri/card0
Xorg 6892 homer 24u CHR 13,64 0t0 149 /dev/input/event0
Xorg 6892 homer 32u CHR 13,68 0t0 336 /dev/input/event4

(2) homer@ubuntu:~$ lsof -p 6892 -a -U
COMMAND PID USER FD TYPE DEVICE SIZE/OFF NODE NAME
Xorg 6892 homer 1u unix 0x0000000000000000 0t0 118649 type=STREAM
Xorg 6892 homer 2u unix 0x0000000000000000 0t0 119748 type=STREAM
Xorg 6892 homer 3u unix 0x0000000000000000 0t0 119927 @/tmp/.X11-unix/X0 type=STREAM
Xorg 6892 homer 6u unix 0x0000000000000000 0t0 118653 @/tmp/.X11-unix/X0 type=STREAM
Xorg 6892 homer 7u unix 0x0000000000000000 0t0 118654 /tmp/.X11-unix/X0 type=STREAM
Xorg 6892 homer 47u unix 0x0000000000000000 0t0 124222 @/tmp/.X11-unix/X0 type=STREAM

(3) homer@ubuntu:~$ lsof -p 6892 -a -i
!-

Листинг 7.1 иллюстрирует сервер Xorg(1), использующий специальные файлы устройств видеоускорителя /dev/dri/card0 и устройств пользовательского ввода