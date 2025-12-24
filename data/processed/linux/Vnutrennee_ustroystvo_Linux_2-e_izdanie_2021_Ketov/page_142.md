---
source_image: page_142.png
page_number: 142
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 28.37
tokens: 7557
characters: 1769
timestamp: 2025-12-24T04:35:55.522289
finish_reason: stop
---

является с точки зрения ядра привилегированной операцией. В старых системах1 программа /bin/ping наделялась атрибутом SUID и находилась во владении суперпользователя root, чьи права и передавались при ее запуске. С точки зрения защищенности системы это не соответствует здравому смыслу, подсказывающему наделять программы минимально необходимыми возможностями, достаточными для их функционирования. Для создания «необработанных» raw(7) и пакетных socket(7) сокетов достаточно только привилегии CAP_NET_RAW, а весь суперпользовательский набор привилегий более чем избыточен.

Листинг 4.24. Делегирование привилегий программы ping(1)

fitz@ubuntu-1804:~$ ls -l /bin/ping
① -rwsr-xr-x 1 root root 64424 Jun 28 11:05 /bin/ping

fitz@ubuntu-1804:~$ ping ubuntu-1804
PING ubuntu-1804 (127.0.1.1) 56(84) bytes of data.
64 bytes from ubuntu-1804 (127.0.1.1): icmp_req=1 ttl=64 time=0.074 ms
^C
--- ubuntu ping statistics ---
1 packets transmitted, 1 received, 0% packet loss, time 0ms
rtt min/avg/max/mdev = 0.074/0.074/0.074/0.000 ms

② fitz@ubuntu-1804:~$ sudo chmod u-s /bin/ping
fitz@ubuntu-1804:~$ ls -l /bin/ping
-rwrxr-xr-x 1 root root 64424 Jun 28 11:05 /bin/ping
fitz@ubuntu-1804:~$ ping ubuntu-1804
ping: icmp open socket: Operation not permitted

③ fitz@ubuntu-1804:~$ sudo setcap cap_net_raw+ep /bin/ping
fitz@ubuntu-1804:~$ getcap /bin/ping
/bin/ping = cap_net_raw+ep
fitz@ubuntu-1804:~$ ping ubuntu-1804
PING ubuntu (127.0.1.1) 56(84) bytes of data.
64 bytes from ubuntu (127.0.1.1): icmp_req=1 ttl=64 time=0.142 ms
^C
--- ubuntu ping statistics ---
1 packets transmitted, 1 received, 0% packet loss, time 0ms
rtt min/avg/max/mdev = 0.142/0.142/0.142/0.000 ms

1 Актуально для Ubuntu ● до версии 18.10 включительно. Начиная с 19.04 все уже «правильно из коробки».