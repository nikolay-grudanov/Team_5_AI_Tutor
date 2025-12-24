---
source_image: page_231.png
page_number: 231
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 31.26
tokens: 6597
characters: 1598
timestamp: 2025-12-24T04:01:24.933683
finish_reason: stop
---

14.2.5. Блокируем пакеты из-под приватных подсетей (спуфинг)

Правила будут такими:

iptables -t mangle -A PREROUTING -s 224.0.0.0/3 -j DROP
iptables -t mangle -A PREROUTING -s 169.254.0.0/16 -j DROP
iptables -t mangle -A PREROUTING -s 172.16.0.0/12 -j DROP
iptables -t mangle -A PREROUTING -s 192.0.2.0/24 -j DROP
iptables -t mangle -A PREROUTING -s 192.168.0.0/16 -j DROP
iptables -t mangle -A PREROUTING -s 10.0.0.0/8 -j DROP
iptables -t mangle -A PREROUTING -s 0.0.0.0/8 -j DROP
iptables -t mangle -A PREROUTING -s 240.0.0.0/5 -j DROP
iptables -t mangle -A PREROUTING -s 127.0.0.0/8 ! -i lo -j DROP

Эти правила блокируют поддельные пакеты, исходящие из частных (локальных) подсетей. На общедоступном сетевом интерфейсе обычно не должно быть пакетов с локальных подсетей.

Данные правила предполагают, что ваш интерфейс петли (loopback) использует адрес IP 127.0.0.0/8.

14.2.6. Дополнительные правила

Также не будут лишними следующими правила:

iptables -t mangle -A PREROUTING -p icmp -j DROP
iptables -A INPUT -p tcp -m connlimit --connlimit-above 80 -j REJECT --reject-with tcp-reset

Первое правило удаляет все ICMP-пакеты. Как правило, ICMP используется только для ping'a — чтобы проверить, «жив» ли узел или нет. Обычно это вам не нужно (есть и так много средств мониторинга, позволяющих убедиться, что с узлом все хорошо), а сторонним узлам и пользователям и по-давно не нужно ничего знать о вашем узле. Поэтому от ICMP можно смело отказаться.

Второе правило позволяет предотвратить атаки соединения. Он отклоняет соединения от хостов, которые уже установили более 80 соединений. Если