---
source_image: page_250.png
page_number: 250
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 29.79
tokens: 7578
characters: 1758
timestamp: 2025-12-24T04:39:08.818866
finish_reason: stop
---

Kernel driver in use: iwlwifi
Kernel modules: iwlwifi

lumpy@ubuntu:~$ lspci -ks 02:00.0
00:19.0 Ethernet controller: Intel Corporation 82579LM Gigabit Network Connection (Lewisville) (rev 04)
    Subsystem: Dell 82579LM Gigabit Network Connection (Lewisville)
    Kernel driver in use: e1000e
    Kernel modules: e1000e

lumpy@ubuntu:~$ modinfo iwlwifi e1000e | grep ^description
description:    Intel(R) Wireless WiFi driver for Linux
description:    Intel(R) PRO/1000 Network Driver

В отличие от несетевых устройств, большинство которых имеют специальный файл в каталоге /dev, сетевые устройства представляются в системе своими интерфейсами. Список доступных интерфейсов, их параметры и статистику можно получить при помощи «классической» UNIX-команды ifconfig(8) или специфичной для Linux команды ip(8) (листинги 6.2 и 6.3).

Листинг 6.2. Сетевые интерфейсы (UNIX ifconfig(8))

lumpy@ubuntu:~$ ifconfig -a
wlp2s0: flags=4163<UP,BROADCAST,RUNNING,MULTICAST> mtu 1500
    inet 192.168.0.101 netmask 255.255.255.0 broadcast 192.168.0.255
    inet6 fe80::5f2d:68c3:2c09:9a18 prefixlen 64 scopeid 0x20<link>
    ether 08:11:96:29:19:70 txqueuelen 1000 (Ethernet)

lo: flags=73<UP,LOOPBACK,RUNNING> mtu 65536
    inet 127.0.0.1 netmask 255.0.0.0
    inet6 ::1 prefixlen 128 scopeid 0x10<host>

eno1: flags=4099<UP,BROADCAST,MULTICAST> mtu 1500
    ether 5c:26:0a:85:a9:1a txqueuelen 1000 (Ethernet)

Листинг 6.3. Сетевые интерфейсы (Linux ip(8))

lumpy@ubuntu:~$ ip link show
1: lo: <LOOPBACK,UP,LOWER_UP> mtu 65536 qdisc noqueue state UNKNOWN ... qlen 1000
    link/loopback 00:00:00:00:00:00 brd 00:00:00:00:00:00
2: eno1: <NO-CARRIER,BROADCAST,MULTICAST,UP> mtu 1500 qdisc ... state DOWN ... qlen 1000
    link/ether 5c:26:0a:85:a9:1a brd ff:ff:ff:ff:ff:ff