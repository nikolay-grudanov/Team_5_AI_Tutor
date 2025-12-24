---
source_image: page_353.png
page_number: 353
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 26.41
tokens: 7575
characters: 1938
timestamp: 2025-12-24T04:42:24.238920
finish_reason: stop
---

---
primary_language: ru
is_rotation_valid: True
rotation_correction: 0
is_table: False
is_diagram: False
---
--- 10.0.0.137 ping statistics ---
2 packets transmitted, 2 received, 0% packet loss, time 1007ms
rtt min/avg/max/mdev = 0.085/0.100/0.116/0.015 ms

/ # ping 10.0.0.1
PING 10.0.0.1 (10.0.0.1): 56 data bytes
64 bytes from 10.0.0.1: seq=0 ttl=64 time=0.165 ms
64 bytes from 10.0.0.1: seq=1 ttl=64 time=0.195 ms
^C
--- 10.0.0.1 ping statistics ---
2 packets transmitted, 2 packets received, 0% packet loss
round-trip min/avg/max = 0.165/0.180/0.195 ms

В листинге 9.8 в контейнере исполняется интерактивный командный интерпретатор, что позволяет запускать команды конфигурирования «изнутри». На практике же в контейнере сразу запускают определенную системную службу, а конфигурационные команды — в интерпретаторе хост-системы, перемещая их в нужное пространство имен нужного контейнера при помощи утилиты nsenter(1), которая использует для этой цели системный вызов setns(2).

Листинг 9.8. Выполнение программ в целевых пространствах имен

rick@ubuntu:~$ pgrep busybox
12089
rick@ubuntu:~$ ip link
5: c137net@if19: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 ... state UP ... qlen 1000
    link/ether e2:bd:81:ee:fe:bf brd ff:ff:ff:ff:ff:ff link-netns anotherdimension
rick@ubuntu:~$ sudo nsenter -t 12089 -n ip link
4: net@if20: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 ... state UP ... qlen 1000
    link/ether a6:71:65:45:fd:c2 brd ff:ff:ff:ff:ff:ff link-netnsid 0

9.3. Контейнеризация: glibc и docker

Изолированные окружения для выполнения программ, создаваемые при помощи механизмов изоляции процессов операционной системы, принято называть контейнерами. Сам принцип такого предоставления ресурсов ОС приложениям принято называть контейнеризацией и считать одним из видов виртуализации¹. Одна-

¹ См. W:[Virtualization] для отличия аппаратной виртуализации, паравиртуализации и виртуализации на уровне ОС (контейнеризации).