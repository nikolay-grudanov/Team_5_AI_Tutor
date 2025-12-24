---
source_image: page_260.png
page_number: 260
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 23.84
tokens: 7523
characters: 1896
timestamp: 2025-12-24T04:39:19.303392
finish_reason: stop
---

к ним соответствующий модуль службы имен (см. 3, листинг 6.10) использует стандартный DNS-клиент (он же resolver(3), DNS-резолвер), в конфигурационном файле resolv.conf(5) которого при статических настройках указываются IP-адреса ближайших кэширующих DNS-серверов, например серверов провайдера услуг Интернета.

Однако в примере из листинга 6.12 показано, что в качестве кэширующего DNS-сервера указан адрес 127.0.0.53 некоторой локальной службы DNS. Такой подход позволяет динамически управлять настройками (не меняя каждый раз файл resolv.conf(5)) при реконфигурировании сетевых подключений, например при присоединении к другой Wi-Fi-сети. В этом случае именно менеджер сетевых подключений (см. разд. 6.2.2) сообщает новые DNS-параметры нового активированного подключения этой самой локальной службе DNS (которой на проверку оказывается systemd-resolved(1)).

Для диагностики DNS-модуля службы имен (равно как и любого другого ее модуля) используется команда getent(8), а для непосредственной диагностики DNS-серверов — команда host(1).

Листинг 6.12. DNS-клиент

lumpy@ubuntu:~$ cat /etc/resolv.conf
# This file is managed by man:systemd-resolved(8). Do not edit.
# See man:systemd-resolved.service(8) for details about the supported modes of
# operation for /etc/resolv.conf.

nameserver 127.0.0.53
options edns0

lumpy@ubuntu:~$ sudo ss -4autpn sport = 53
Netid State Recv-Q Send-Q Local Address:Port Peer Address:Port
udp UNCONN 0 0 127.0.0.53%lo:53 0.0.0.0:* users:(("systemd-resolve",pid=5932,...))
tcp LISTEN 0 128 127.0.0.53%lo:53 0.0.0.0:* users:(("systemd-resolve",pid=5932,...))

lumpy@ubuntu:~$ getent hosts bhv.ru
91.244.162.162 bhv.ru

lumpy@ubuntu:~$ host bhv.ru
bhv.ru has address 91.244.162.162
bhv.ru mail is handled by 50 relay2.peterlink.ru.
bhv.ru mail is handled by 30 relay1.peterlink.ru.

lumpy@ubuntu:~$ host 8.8.8.8
8.8.8.8.in-addr.arpa domain name pointer dns.google.