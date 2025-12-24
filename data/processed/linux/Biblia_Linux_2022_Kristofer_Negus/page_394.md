---
source_image: page_394.png
page_number: 394
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 40.11
tokens: 7962
characters: 2638
timestamp: 2025-12-24T04:56:37.603962
finish_reason: stop
---

inet6 fe80::25ff:8129:751b:23e3/64 scope link noprefixroute
    valid_lft forever preferred_lft forever
4: virbr0: <NO-CARRIER,BROADCAST,MULTICAST,UP> mtu 1500
    qdisc noqueue state DOWN group default qlen 1000
    link/ether 52:54:00:0c:69:0a brd ff:ff:ff:ff:ff:ff
    inet 192.168.122.1/24 brd 192.168.122.255 scope global virbr0
    valid_lft forever preferred_lft forever

Команда ip addr show выводит информацию о сетевых интерфейсах, в данном случае с ноутбука под управлением системы Fedora 30.

Запись lo в первой строке вывода показывает кольцевой интерфейс, который используется для подключения сетевых команд, выполняемых в локальной системе, к самой локальной системе. IP-адрес для локального хоста — это 127.0.0.1/8 (/8 — обозначение бесклассовой адресации CIDR, указывающее, что 127.0 — это номер сети, а 0.1 — номер хоста). Добавьте параметр -s (ip-s addr show), чтобы увидеть статистику пакетных передач и ошибок, связанных с каждым интерфейсом.

В этом случае проводной интерфейс Ethernet (enp4s0) отключен (нет кабеля), но беспроводной интерфейс включен (wlp2s0). МАС-адрес в беспроводном интерфейсе (wlp2s0) — это e0:06:e6:83:ac:c7 и интернет-адрес (IPv4) — это 192.168.1.8. IPv6-адрес также включен.

Более старые версии Linux применяются для назначения общих имен сетевых интерфейсов, таких как eth0 и wlan0. Теперь интерфейсы называются по их расположению на шине компьютера. Например, первый порт на сетевой карте, размещенной на третьей шине PCI для системы Fedora, называется p3p1. Первым встроенным портом Ethernet будет m1. Бывает, что беспроводные интерфейсы используют имя беспроводной сети в качестве имени устройства.

Другая популярная команда для просмотра информации о сетевом интерфейсе — ifconfig. По умолчанию она отображает ту же информацию, что и команда ip addr, а еще, тоже по умолчанию, — количество пакетов, принятых (RX) и переданных (TX), а также количество данных, любые ошибки или потери пакетов:

# ifconfig wlp2s0
wlp2s0: flags=4163<UP,BROADCAST,RUNNING,MULTICAST> mtu 1500
    inet 192.168.1.83 netmask 255.255.255.0
    broadcast 192.168.1.255
    inet6 2600:1700:722:a10:b55a:fca6:790d:6aa6
        prefixlen 64 scopeid 0x0<global>
    inet6 fe80::25ff:8129:751b:23e3
        prefixlen 64 scopeid 0x20<link>
    inet6 2600:1700:722:a10::489
        prefixlen 128 scopeid 0x0<global>
    ether e0:06:e6:83:ac:c7 txqueuelen 1000 (Ethernet)
    RX packets 208402 bytes 250962570 (239.3 MiB)
    RX errors 0 dropped 4 overruns 0 frame 0
    TX packets 113589 bytes 13240384 (12.6 MiB)
    TX errors 0 dropped 0 overruns 0 carrier 0 collisions 0
    Checking connectivity to remote systems