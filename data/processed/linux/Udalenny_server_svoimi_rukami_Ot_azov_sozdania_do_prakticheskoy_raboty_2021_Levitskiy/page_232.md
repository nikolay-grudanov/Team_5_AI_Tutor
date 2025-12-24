---
source_image: page_232.png
page_number: 232
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 23.22
tokens: 6484
characters: 1539
timestamp: 2025-12-24T04:01:19.598580
finish_reason: stop
---

у вас возникнут какие-либо проблемы с легитимными узлами, вам нужно поднять лимит на количество установленных TCP-соединений.

Следующие правила ограничивают число новых соединений TCP, которые клиент может установить за секунду. Они полезны против атак на соединения, но не годятся против SYN-флуда, поскольку обычно используется бесконечное количество разных поддельных IP-адресов источника.

iptables -A INPUT -p tcp -m conntrack --ctstate NEW -m limit --limit 60/s --limit-burst 20 -j ACCEPT
iptables -A INPUT -p tcp -m conntrack --ctstate NEW -j DROP

Следующее правило блокирует фрагментированные пакеты:

iptables -t mangle -A PREROUTING -f -j DROP

А эти правила ограничивают входящие TCP RST пакеты, чтобы избежать TCP RST-наводнения:

iptables -A INPUT -p tcp --tcp-flags RST RST -m limit --limit 2/s --limit-burst 2 -j ACCEPT
iptables -A INPUT -p tcp --tcp-flags RST RST -j DROP

14.2.7. Полный список анти-DDoS правил

Собирая все вместе, приводим полный список правил, позволяющих существенно защитить ваш сервер от всякого рода DDoS-атак:

### 1: Избавляемся от неправильных пакетов ###
/sbin/iptables -t mangle -A PREROUTING -m conntrack --ctstate INVALID -j DROP

### 2: Удаляем новые TCP-пакеты без флага SYN ###
/sbin/iptables -t mangle -A PREROUTING -p tcp ! --syn -m conntrack --ctstate NEW -j DROP

### 3: Удаляем пакеты с подозрительным значением MSS ###
/sbin/iptables -t mangle -A PREROUTING -p tcp -m conntrack --ctstate NEW -m tcpmss ! --mss 536:65535 -j DROP

### 4: Блокируем пакеты с фиктивными TCP-флагами ###