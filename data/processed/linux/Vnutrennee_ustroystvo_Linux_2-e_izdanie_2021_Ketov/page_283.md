---
source_image: page_283.png
page_number: 283
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 32.88
tokens: 7655
characters: 1954
timestamp: 2025-12-24T04:40:17.528827
finish_reason: stop
---

Листинг 6.35. Анализатор пакетов tcpdump

lumpy@ubuntu:~$ tcpdump -i wlp2s0 port 53
tcpdump: verbose output suppressed, use -v or -vv for full protocol decode
listening on wlp2s0, link-type EN10MB (Ethernet), capture size 65535 bytes

lumpy@ubuntu:~$ host 2x2tv.ru
2x2tv.ru ① has address 146.158.12.222 ②
2x2tv.ru mail is handled by 10 fm.tnt-tv.ru.

15:11:32.139394 IP ubuntu.local.40694 > 192.168.100.1.domain: 2656+ [1au] A? 2x2tv.ru. (37)
15:11:32.144674 IP 192.168.100.1.domain > ubuntu.local.40694: 2656 1/0/1 A 146.158.12.222 (53)
15:11:32.145260 IP ubuntu.local.22022 > 192.168.100.1.domain: 63760+ [1au] MX? 2x2tv.ru. (37)
15:11:32.147959 IP 192.168.100.1.domain > ubuntu.local.48132: 63760 1/0/1 MX fm.tnt-tv.ru. 10 (63)

^C
4 packets captured
4 packets received by filter
0 packets dropped by kernel

Анализу подвергается работа DNS-клиента host(1), отображающего имя домена 2x2tv.ru на IP-адрес и имена его почтовых адресов (MX-записи DNS). В результате анализа захваченных пакетов наблюдаются запросы и ответы DNS-протокола к локальному кэширующему серверу 192.168.100.1, который на запрос ① A? адреса IPv4, соответствующего имени 2x2tv.ru, отвечает ② адресом A 146.158.12.222.

Терминальный¹ анализатор пакетов tshark(1), позволяющий проводить детальный анализ прикладных протоколов, таких как SSH, HTTP, FTP, NFS и пр., проиллюстрирован в листинге 6.36. Здесь анализируется работа пользовательского агента curl(1), запрашивающего Web-ресурс по адресу http://ipinfo.io/city. В результате захвата пакетов на интерфейсе (-i, interface) wlp2s0, адресованных порту port 80, просматриваются (-R, read filter) пакеты, содержащие http-запросы, при этом детальному анализу (-v, view) подвергается только (-o, only) их http-содержимое.

В результате анализа, например, можно сделать вывод ★ о программном обеспечении Web-сервера, обслуживающего сайт http://ipinfi.io.

¹ Гораздо удобнее, конечно, использовать его графический вариант — wireshark(1).