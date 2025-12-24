---
source_image: page_106.png
page_number: 106
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 24.89
tokens: 6395
characters: 981
timestamp: 2025-12-24T03:58:35.048616
finish_reason: stop
---

**Рис. 5.9. Вкладка Ethernet в Astra Linux**

**5.3. Команда ifconfig**

Команда ifconfig используется для настройки и отображения параметров сетевого интерфейса. Если ввести команду ifconfig без параметров, то мы получим список всех активных интерфейсов, например:

ens33
Link encap:Ethernet HWaddr 00:0C:29:C2:0D:D1
inet addr:192.168.52.154 Bcast:192.168.52.255 Mask:255.255.255.0
inet6 addr: fe80::20c:29ff:fec2:dd1/64 Scope:Link
UP BROADCAST RUNNING MULTICAST MTU:1500 Metric:1
RX packets:425 errors:0 dropped:0 overruns:0 frame:0
TX packets:406 errors:0 dropped:0 overruns:0 carrier:0
collisions:0 txqueuelen:1000
RX bytes:41540 (40.5 Kb) TX bytes:39618 (38.6 Kb)

lo
Link encap:Local Loopback
inet addr:127.0.0.1 Mask:255.0.0.0
inet6 addr: ::1/128 Scope:Host
UP LOOPBACK RUNNING MTU:65536 Metric:1
RX packets:96 errors:0 dropped:0 overruns:0 frame:0
TX packets:96 errors:0 dropped:0 overruns:0 carrier:0
collisions:0 txqueuelen:0
RX bytes:5760 (5.6 Kb) TX bytes:5760 (5.6 Kb)