---
source_image: page_288.png
page_number: 288
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 32.73
tokens: 7708
characters: 1871
timestamp: 2025-12-24T04:40:25.877926
finish_reason: stop
---

**Листинг 6.40. Сетевой сервер: системные вызовы socket(2), bind(2), listen(2), accept(2), send(2) и recv(2)**

lumpy@ubuntu:~$ cd /usr/share/doc
lumpy@ubuntu:/usr/share/doc$ strace -fe trace=network python -m SimpleHTTPServer

1 socket(AF_INET, SOCK_STREAM, IPPROTO_IP) = 3
setsockopt(3, SOL_SOCKET, SO_REUSEADDR, [1], 4) = 0
2 bind(3, {sa_family=AF_INET, sin_port=htons(8000), sin_addr=inet_addr("0.0.0.0")}, 16) = 0
3 listen(3, 5) = 0
Serving HTTP on 0.0.0.0 port 8000 ...
4 accept(3, {sa_family=AF_INET, sin_port=htons(55094), sin_addr=inet_addr("127.0.0.1")}, [16]) = 4
5 recvfrom(4, "GET / HTTP/1.1\r\nHost: localhost:"..., 8192, 0, NULL, NULL) = 78
127.0.0.1 - - [24/Nov/2019 12:14:54] "GET / HTTP/1.1" 200 -
6 sendto(4, "HTTP/1.0 200 OK\r\n", 17, 0, NULL, 0) = 17
sendto(4, "Server: SimpleHTTP/0.6 Python/2."..., 41, 0, NULL, 0) = 41
sendto(4, "Date: Sun, 24 Nov 2019 09:14:54 "..., 37, 0, NULL, 0) = 37
sendto(4, "Content-type: text/html; charset"... , 40, 0, NULL, 0) = 40
sendto(4, "Content-Length: 86602\r\n", 23, 0, NULL, 0) = 23
sendto(4, "\r\n", 2, 0, NULL, 0) = 2
sendto(4, "<!DOCTYPE html PUBLIC "-//W3C//D"..., 8192, 0, NULL, 0) = 8192
shutdowm(4, SHUT_WR) = 0

lumpy@ubuntu:~$ wget http://ubuntu:8000
--2019-11-24 12:18:05--  http://ubuntu:8000/
Распознаётся ubuntu (ubuntu)... 127.0.1.1
Подключение к ubuntu (ubuntu)|127.0.1.1|:8000... соединение установлено.
HTTP-запрос отправлен. Ожидание ответа... 200 OK
Длина: 86602 (85K) [text/html]
Сохранение в: «index.html»

100%[=============================>] 84,57K   --.-K/s   за 0,002s

2019-11-24 12:18:05 (54,6 MB/s) - «index.html» сохранён [86602/86602]

**6.6. В заключение**

Сетевая подсистема ОС Linux чрезвычайно развита на всех ее уровнях — от сетевых интерфейсов и протоколов и до прикладных сетевых служб. На сегодняшний день колоссальное количество сетевых устройств работают под управлением