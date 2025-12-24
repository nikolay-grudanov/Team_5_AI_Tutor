---
source_image: page_259.png
page_number: 259
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 18.58
tokens: 7379
characters: 1571
timestamp: 2025-12-24T04:39:07.156911
finish_reason: stop
---

Сетевая подсистема

3 /lib/x86_64-linux-gnu/libnss_dns.so.2
1 /lib/x86_64-linux-gnu/libnss_files.so.2
2 /lib/x86_64-linux-gnu/libnss_mdns4_minimal.so.2

Файловые таблицы имен /etc/hosts и /etc/services имеют тривиальный формат 1, 2, сопоставляющий имена узлов и сервисов — их IP-адресам и портам протоколов TCP и UDP, что проиллюстрировано в листинге 6.11. Утилита службы имен getent(1), позволяющая выбирать указанную сущность по ее типу и имени, используется в качестве диагностики 3 коммутатора службы имен и его модулей.

Листинг 6.11. Файловые таблицы имен

lumpy@ubuntu:~$ cat /etc/hosts
127.0.0.1 localhost
127.0.1.1 ubuntu

# The following lines are desirable for IPv6 capable hosts
::1 ip6-localhost ip6-loopback
fe00::0 ip6-localnet
ff00::0 ip6-mcastprefix
ff02::1 ip6-allnodes
ff02::2 ip6-allrouters

lumpy@ubuntu:~$ grep http /etc/services
# Updated from https://www.iana.org/assignments/service-names-port-numbers/service-names-port-numbers.xhtml .

http      80/tcp     www           # WorldWideWeb HTTP
https     443/tcp    # http protocol over TLS/SSL
http-alt  8080/tcp   webcache      # WWW caching service
http-alt  8080/udp

3 lumpy@ubuntu:~$ getent hosts ubuntu
127.0.1.1 ubuntu
lumpy@ubuntu:~$ getent services 53/udp
domain    53/tcp

Соответствия IP-адресов именам «серверных» узлов, например публичных Web-, почтовых и прочих серверов, обычно регистрируются их администраторами в «таблицах» на ответственных¹ (authoritative) серверах службы DNS. Для доступа

¹ Подробнее о том, как устроена система DNS, можно узнать здесь: https://tiny.cc/niwqqz.