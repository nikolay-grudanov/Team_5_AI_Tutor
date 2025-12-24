---
source_image: page_179.png
page_number: 179
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 25.48
tokens: 7680
characters: 959
timestamp: 2025-12-24T04:23:50.934321
finish_reason: stop
---

Рис. 5.1. Графическая программа настройки сети

Окно программы, за исключением нескольких мелких усовершенствований, не менялось уже несколько лет.

5.1.2. ping

Одна из часто используемых администраторами команд — ping. Она посылает ICMP-пакеты в виде эхо-запросов на указанную систему для определения пропускной способности сети. О таких запросах мы уже говорили, когда рассматривали сетевой экран (см. разд. 4.10).

Например, выполните команду ping 195.18.1.41, и в ответ вы получите следующую информацию:

PING 195.18.1.41 (195.18.1.41) from 195.18.1.41 : 56(84) bytes of data.
64 bytes from 195.18.1.41: icmp_seq=1 ttl=64 time=0.102 ms
64 bytes from 195.18.1.41: icmp_seq=2 ttl=64 time=0.094 ms
64 bytes from 195.18.1.41: icmp_seq=3 ttl=64 time=0.094 ms
64 bytes from 195.18.1.41: icmp_seq=4 ttl=64 time=0.095 ms
--- 195.18.1.41 ping statistics ---
4 packets transmitted, 4 received, 0% loss, time 3013ms
rtt min/avg/max/mdev = 0.094/0.096/0.102/0.007 ms