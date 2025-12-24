---
source_image: page_254.png
page_number: 254
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 29.40
tokens: 7604
characters: 1688
timestamp: 2025-12-24T04:39:13.687018
finish_reason: stop
---

RX errors 0 dropped 0 overruns 0 frame 0
TX packets 94 bytes 14932 (14.9 KB)
TX errors 0 dropped 0 overruns 0 carrier 0 collisions 0

lumpy@ubuntu:~$ ping -c 1 10.0.0.10
PING 10.0.0.10 (10.0.0.10) 56(84) bytes of data.
64 bytes from 10.0.0.10: icmp_seq=1 ttl=64 time=0.032 ms

--- 10.0.0.10 ping statistics ---
1 packets transmitted, 1 received, 0% packet loss, time 0ms
rtt min/avg/max/mdev = 0.032/0.032/0.032/0.000 ms

lumpy@ubuntu:~$ sudo ip address add 172.16.16.172/16 dev eno1
lumpy@ubuntu:~$ ip address show dev eno1
3: eno1: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc fq_codel state UP group default qlen 1000
    link/ether 08:00:27:c0:67:8f brd ff:ff:ff:ff:ff:ff
    inet 10.0.0.10/8 brd 10.255.255.255 scope global eno1
        valid_lft forever preferred_lft forever
    inet 172.16.16.172/16 scope global eno1
        valid_lft forever preferred_lft forever

lumpy@ubuntu:~$ ping -c 1 172.16.16.172
PING 172.16.16.172 (172.16.16.172) 56(84) bytes of data.
64 bytes from 172.16.16.172: icmp_seq=1 ttl=64 time=1.27 ms

--- 172.16.16.172 ping statistics ---
1 packets transmitted, 1 received, 0% packet loss, time 0ms
rtt min/avg/max/mdev = 1.270/1.270/1.270/0.000 ms

Просмотр таблиц маршрутизации и ручное конфигурирование IP-маршрутов выполняется посредством команды route(8) или ip(8), а простейшая диагностика — при помощи команды traceroute(1). В примере из листинга 6.8 показана процедура ручного добавления маршрута «по умолчанию» 1 через интернет-шлюз 10.0.0.1 2 с последующей диагностикой 3 доступности узлов за ним 4.

Листинг 6.8. Ручное конфигурирование таблицы маршрутизации

lumpy@ubuntu:~$ sudo ip route add 0.0.0.0/0 via 10.0.0.1
lumpy@ubuntu:~$ route -n