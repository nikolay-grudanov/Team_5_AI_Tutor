---
source_image: page_393.png
page_number: 393
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 26.39
tokens: 7469
characters: 1359
timestamp: 2025-12-24T04:56:23.492328
finish_reason: stop
---

Рис. 14.4. Просмотр служб, доступных через межсетевой экран из веб-интерфейса Cockpit

Проверка сети из командной строки
Чтобы подробнее узнать о сетевых интерфейсах, попробуйте выполнить несколько команд. Существуют команды, которые могут отобразить информацию о сетевых интерфейсах, маршрутах, хостах и трафике в сети.

Просмотр сетевых интерфейсов. Чтобы просмотреть информацию о каждом сетевом интерфейсе в локальной системе Linux, введите следующее:

# ip addr show
1: lo: <LOOPBACK,UP,LOWER_UP> mtu 65536 qdisc noqueue
    state UNKNOWN group default qlen 1000
    link/loopback 00:00:00:00:00:00 brd 00:00:00:00:00:00
    inet 127.0.0.1/8 scope host lo
        valid_lft forever preferred_lft forever
    inet6 ::1/128 scope host
        valid_lft forever preferred_lft forever
2: enp4s0: <NO-CARRIER,BROADCAST,MULTICAST,UP> mtu 1500
    qdisc fq_codel state DOWN group default qlen 1000
    link/ether 30:85:a9:04:9b:f9 brd ff:ff:ff:ff:ff:ff
3: wlp2s0: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500
    qdisc mq state UP group default qlen 1000
    link/ether e0:06:e6:83:ac:c7 brd ff:ff:ff:ff:ff:ff
    inet 192.168.1.83/24 brd 192.168.1.255 scope global dynamic noprefixroute wlp2s0
        valid_lft 78738sec preferred_lft 78738sec
    inet6 2600:1700:722:a10::489/128 scope global dynamic noprefixroute
        valid_lft 5529sec preferred_lft 5229sec