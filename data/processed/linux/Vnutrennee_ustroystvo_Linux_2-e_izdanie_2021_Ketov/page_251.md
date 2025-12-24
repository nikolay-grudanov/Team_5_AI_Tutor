---
source_image: page_251.png
page_number: 251
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 29.91
tokens: 7586
characters: 1930
timestamp: 2025-12-24T04:39:08.972627
finish_reason: stop
---

3: wlp2s0: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc mq state UP ... qlen 1000
    link/ether 08:11:96:29:19:70 brd ff:ff:ff:ff:ff:ff

lumpy@ubuntu:~$ ip addr show dev wlp2s0
3: wlp2s0: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc mq state UP group default qlen 1000
    link/ether 08:11:96:29:19:70 brd ff:ff:ff:ff:ff:ff
    inet 192.168.0.101/24 brd 192.168.0.255 scope global dynamic noprefixroute wlp2s0
        valid_lft 7121sec preferred_lft 7121sec
    inet6 fe80::5f2d:68c3:2c09:9a18/64 scope link noprefixroute
        valid_lft forever preferred_lft forever

За логическое взаимодействие (адресацию, маршрутизацию, обеспечение надежной доставки и пр.) отвечают сетевые протоколы, тоже в большинстве случаев реализуемые соответствующими модулями ядра. Нужно отметить, что в примере из листинга 6.4 показан список динамически загруженных модулей, среди которых присутствует «нестандартный» TCP vegas, но нет IP, TCP, UDP и прочих «стандартных» протоколов стека TCP/IP. На текущий момент времени сложно вообразить применение Linux без подключения к IP-сети, поэтому модули стандартных протоколов TCP/IP стека скомпонованы в ядро статически и являются частью «стартового» (см. разд. 4.1.1) модуля.

Листинг 6.4. Драйвера сетевых протоколов

lumpy@ubuntu:~$ lsmod
Module           Size Used by
iwldvm           229376   0
mac80211         786432   1 iwldvm
iwlwifi          290816   1 iwldvm
cfg80211         622592   3 iwldvm,iwlwifi,mac80211
e1000e           249856   0
ptp              20480    1 e1000e

lumpy@ubuntu:~$ modinfo tcp_vegas bneq mac80211 | grep ^description
description:     PTP clocks support
description:     Intel(R) Wireless WiFi Link AGN driver for Linux
description:     IEEE 802.11 subsystem

Доступ процессов к услугам ядерной части сетевой подсистемы реализует интерфейс сетевых сокетов socket(7), являющихся основным (и единственным) средством сетевого взаимодействия процессов в Linux.