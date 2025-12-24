---
source_image: page_296.png
page_number: 296
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 34.51
tokens: 7629
characters: 1959
timestamp: 2025-12-24T04:40:42.451235
finish_reason: stop
---

**Листинг 7.6. Виртуальный X-сервер Xnest**

homer@ubuntu:~$ Xnest :0 &

_XSERVTransSocketUNIXCreateListener: ...SocketCreateListener() failed
_XSERVTransMakeAllCOTSServerListeners: server already running
(EE)
Fatal server error:

1 (EE) Cannot establish any listening sockets - Make sure an X server isn't already running(EE)

homer@ubuntu:~$ Xnest :1 -listen tcp &
[1] 10950
homer@ubuntu:~$ lsof -p 10950 -a -i
COMMAND PID USER FD TYPE DEVICE SIZE/OFF NODE NAME
2 Xnest 10950 homer 4u IPv6 146673 0t0 TCP *:x11-1 (LISTEN)
Xnest 10950 homer 5u IPv4 146674 0t0 TCP *:x11-1 (LISTEN)
homer@ubuntu:~$ lsof -p 10950 -a -U
COMMAND PID USER FD TYPE DEVICE SIZE/OFF NODE NAME
Xnest 10950 homer 6u unix 0x0000000000000000 0t0 146675 @/tmp/.X11-unix/X1 type=STREAM
3 Xnest 10950 homer 7u unix 0x0000000000000000 0t0 146676 /tmp/.X11-unix/X1 type=STREAM
Xnest 10950 homer 9u unix 0x0000000000000000 0t0 146679 type=STREAM

В примере из листинга 7.7 показана трассировка демонстрационного X-клиента xeyes(1), иллюстрирующая использование клиентом локального 1 и сетевого 2 сокетов в зависимости от значения переменной окружения DISPLAY.

**Листинг 7.7. Сетевые и локальные подключения клиента X-сервера**

homer@ubuntu:~$ DISPLAY=:1 strace -fe connect xeyes
1 connect(3, {sa_family=AF_UNIX, sun_path="@/tmp/.X11-unix/X1" }, 20) = 0
^C
homer@ubuntu:~$ DISPLAY=ubuntu.local:1 strace -fe connect xeyes
2 connect(3, {sa_family=AF_INET, sin_port=htons(6001), sin_addr=inet_addr("192.168.0.105")}, 16) = 0
^C

При работе в оконной системе переменную DISPLAY обычно устанавливают в начале сеанса, а затем при запуске X-клиентов их вывод будет попадать на нужный X-сервер, как это показано на примере1 сервера Xnest(1) и клиентов xterm(1), xcalc(1) и xeyes(1) в листинге 7.8 и на рис. 7.1.

1 Все иллюстрации дальше сделаны именно при помощи «виртуальных» X-серверов Xnest(1) или Xephyr(1) и могут быть без проблем воспроизведены пользователем, уже работающим в оконной системе.