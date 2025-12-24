---
source_image: page_230.png
page_number: 230
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 25.85
tokens: 6539
characters: 1555
timestamp: 2025-12-24T04:01:19.473792
finish_reason: stop
---

Данное правило блокирует все пакеты, которые являются новыми (не при- надлежат уже установленному соединению) и не используют флаг SYN.

Блокируем пакеты с неправильным значением MSS:

iptables -t mangle -A PREROUTING -p tcp -m conntrack --ctstate NEW -m tcpmss ! --mss 536:65535 -j DROP

Такие пакеты выглядят подозрительно, поэтому лучше их заблокировать, чем пропустить атаку.

Блокируем пакеты с поддельными TCP-флагами:

iptables -t mangle -A PREROUTING -p tcp --tcp-flags FIN,SYN,RST,PSH,ACK,URG NONE -j DROP
iptables -t mangle -A PREROUTING -p tcp --tcp-flags FIN,SYN FIN,SYN -j DROP
iptables -t mangle -A PREROUTING -p tcp --tcp-flags SYN,RST SYN,RST -j DROP
iptables -t mangle -A PREROUTING -p tcp --tcp-flags FIN,RST FIN,RST -j DROP
iptables -t mangle -A PREROUTING -p tcp --tcp-flags FIN,ACK FIN -j DROP
iptables -t mangle -A PREROUTING -p tcp --tcp-flags ACK,URG URG -j DROP
iptables -t mangle -A PREROUTING -p tcp --tcp-flags ACK,FIN FIN -j DROP
iptables -t mangle -A PREROUTING -p tcp --tcp-flags ACK,PSH PSH -j DROP
iptables -t mangle -A PREROUTING -p tcp --tcp-flags ALL ALL -j DROP
iptables -t mangle -A PREROUTING -p tcp --tcp-flags ALL NONE -j DROP
iptables -t mangle -A PREROUTING -p tcp --tcp-flags ALL FIN,PSH,URG -j DROP
iptables -t mangle -A PREROUTING -p tcp --tcp-flags ALL SYN,FIN,PSH,URG -j DROP
iptables -t mangle -A PREROUTING -p tcp --tcp-flags ALL SYN,RST,ACK,FIN,URG -j DROP

Приведенный выше набор правил блокирует пакеты, использующих фиктивные флаги TCP, т.е. флаги TCP, которые нормальные пакеты не будут использовать.