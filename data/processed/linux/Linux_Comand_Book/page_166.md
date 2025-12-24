---
source_image: page_166.png
page_number: 166
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 31.31
tokens: 6095
characters: 1166
timestamp: 2025-12-24T04:08:20.195361
finish_reason: stop
---

Команда ping сообщает, доступен ли удаленный хост. Она посылает маленькие пакеты (ICMP-пакеты, если быть точным) удаленному хосту и ждет ответов.

$ ping google.com
PING google.com (216.239.37.100) from 192.168.0.10 : 56(84) bytes of data.
64 bytes fromwww.google.com (216.239.37.100)
: icmp_seq=O ttl=49 time=32.390 msec
64 bytes fromwww.google.com (216.239.37.100)
: icmp_seq=l ttl=49 time=24.208 msec
AC
google.com ping statistics
2 packets transmitted, 2 packets received, 0% packet loss
round-trip min/avg/max/mdev = 24.208/28.299/32.390/4.091 ms

Полезные опции
-c N    Отправить пакеты максимум N раз
-± N    Ждать Жсекунд (по умолчанию 1 секунду) между отправками
-n      Выводить IP-адреса, а не имена хостов

traceroute [опции] хост[длина_пакета] traceroute
/bin   stdin stdout -file --opt -help —version
Команда traceroute выводит сетевой путь от вашего локального хоста до удаленного хоста и время, которое требуется пакетам для того, чтобы пройти этот путь.

$ traceroute yahoo.com
1 server.example.com (192.168.0.20)
1.397 ms 1.973 ms
2.817 ms
210.221.16.1 (10.221.16.1)
15.397 ms 15.973 ms
10.817 ms
3gbr2-plO.cblma.ip.att.net (12.123.40.190) 11.952ms