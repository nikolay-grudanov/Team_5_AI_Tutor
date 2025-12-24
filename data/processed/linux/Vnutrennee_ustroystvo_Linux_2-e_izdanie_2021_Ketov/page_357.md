---
source_image: page_357.png
page_number: 357
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 30.53
tokens: 7659
characters: 2095
timestamp: 2025-12-24T04:42:32.195997
finish_reason: stop
---

1 4026532378 4026532373 4026532376 bash .
root@c-123:# apt update
root@c-123:# apt install iproute2
root@c-123:# ip link
1: lo: <LOOPBACK,UP,LOWER_UP> mtu 65536 qdisc noqueue state UNKNOWN ... qlen 1000
    link/loopback 00:00:00:00:00:00 brd 00:00:00:00:00:00
26: eth0@if27: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc noqueue state UP ...
    link/ether 02:42:ac:11:00:02 brd ff:ff:ff:ff:ff:ff link-netnsid 0
root@c-123:# Ctrl+P Ctrl+C
rick@ubuntu:~ $ docker ps
CONTAINER ID   IMAGE       COMMAND   CREATED   STATUS     PORTS   NAMES
d54bd8ab3100   ubuntu:16.04 "/bin/bash" 4 minutes ago Up 4 minutes c-123
rick@ubuntu:~ $ ps o pid,netns,mntns,pidns,comm p $$
    PID   NETNS   MNTNS   PIDNS   COMMAND
21357 4026531992 4026531840 4026531836 bash
rick@ubuntu:~ $ ip link
27: veth72908b6@if26: <BROADCAST,MULTICAST,UP,LOWER_UP> ... master docker0 state UP ...
    link/ether 2a:4a:c7:0b:9d:1f brd ff:ff:ff:ff:ff:ff link-netnsid 1
rick@ubuntu:~ $ docker attach c-123
root@c-132:#

Анализ Docker-контейнера в листинге 9.11 в очередной раз показывает, что в его основе лежат базовые механизмы изоляции на основе пространств имен (1) и (3), только сетевое пространство имен контейнера и хост-системы оказываются (2) (4) предварительно сконфигурированными. В них помещены парные интерфейсы veth72908b6 и eth0 виртуального Ethernet-коммутатора, обеспечивающие связь между виртуальной машиной и хост-системой по сценарию, похожему на изложенный ранее в листинге 9.6. Кроме того, Docker предоставляет удобный способ отключиться от интерактивной консоли контейнера (1), а затем подключиться к ней обратно (2).

9.4. Группы управления (cgroups)

Вместе с появлением в операционной системе новых сущностей — контейнеров, между которыми разделяются ее ресурсы, неизбежно возникает запрос на управление количественным распределением ресурсов центрального процессора, памяти и устройств ввода-вывода между ними. Контейнеры — по сути, это группы процессов, выполняющиеся в отдельных пространствах имен (и с отдельными корневыми каталогами). Именно для количественного распределения ресурсов между группами