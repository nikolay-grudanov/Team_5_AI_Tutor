---
source_image: page_389.png
page_number: 389
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 12.63
tokens: 6283
characters: 1028
timestamp: 2025-12-24T04:04:19.967730
finish_reason: stop
---

Обновим список пакетов программ, чтобы в процессе установки не было ошибок:

$ sudo apt update

Установим пакет iptables-persistent для сохранения правил iptables:

$ sudo apt-get install iptables-persistent

Подготовим правила iptables:

$ sudo iptables -F
$ sudo iptables -A INPUT -i lo -j ACCEPT
$ sudo iptables -A INPUT -m state --state ESTABLISHED,RELATED -j ACCEPT
$ sudo iptables -A INPUT -p icmp -j ACCEPT
$ sudo iptables -A INPUT -p tcp --dport 22 -j ACCEPT
$ sudo iptables -A INPUT -p tcp --dport 80 -j ACCEPT
$ sudo iptables -A INPUT -p tcp --dport 443 -j ACCEPT
$ sudo iptables -A INPUT -p tcp --dport 7443 -j ACCEPT
$ sudo iptables -A INPUT -p udp --dport 16384:32768 -j ACCEPT
$ sudo iptables -P INPUT DROP

Данные правила необходимы для нормальной работы веб-конференции BBB. Сохраним правила:

$ sudo /etc/init.d/netfilter-persistent save

Установим вспомогательное программное обеспечение:

$ sudo apt-get install apt-transport-https apt-transport-tor ca-certificates curl gnupg-agent software-properties-common