---
source_image: page_282.png
page_number: 282
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 22.73
tokens: 7524
characters: 1927
timestamp: 2025-12-24T04:40:03.865526
finish_reason: stop
---

Клиент smbclient(1) имеет встроенный механизм NBNS, поэтому без проблем подключается к узлу WINXP, а при монтировании cifs механизм NBNS недоступен ①, что требует подсказки ② в виде IP-адреса сервера.

Листинг 6.34. Монтирование ресурса SMB/CIFS

lumpy@ubuntu:~$ sudo mkdir -p /mnt/network/winxp/media
lumpy@ubuntu:~$ sudo mount -t cifs -o guest //WINXP/media /mnt/network/winxp/media
① mount error: could not resolve address for WINXP: Unknown error
lumpy@ubuntu:~$ nmblookup WINXP
querying WINXP on 192.168.100.255
192.168.100.3 WINXP<00>
② lumpy@ubuntu:~$ sudo mount -t cifs -o guest,ip=192.168.100.3 //WINXP/media /mnt/network/winxp/media
lumpy@ubuntu:~$ findmnt -t cifs
TARGET SOURCE FSTYPE OPTIONS
/mnt/network/winxp/media //WINXP/media cifs rw,relatime,vers=1.0,cache=strict,...
lumpy@ubuntu:~$ ls -l /mnt/network/winxp/media/DCIM/
итого 346228
-rw-r--r-- 1 root root 4494092 февр. 13 2011 Dd595.jpg
-rw-r--r-- 1 root root 4108278 февр. 13 2011 Dd681.jpg

6.5. Средства сетевой диагностики

Диагностика сетевого обмена существенно облегчает решение разнообразных задач, связанных с эксплуатацией или разработкой сетевых приложений. К сетевым диагностическим специальным средствам относят анализаторы пакетов и сетевые сканеры, которые применяются самостоятельно или вместе с трассировщиками системных и библиотечных вызовов.

6.5.1. Анализаторы пакетов tcpdump и tshark

Анализаторы пакетов предназначены для перехвата данных, поступающих из сети на сетевые интерфейсы или отправляющиеся в сеть с сетевых интерфейсов. Современные анализаторы пакетов, кроме собственно захвата пакетов, осуществляют их детальный протокольный разбор, а также позволяют отфильтровывать подлежащие анализу пакеты по ряду критериев.

В листинге 6.35 показан пример использования наиболее распространенного, «классического» анализатора пакетов tcpdump(1), анализирующего пакеты на интерфейсе (-i, interface) wlp2s0, адресованные порту port 53.