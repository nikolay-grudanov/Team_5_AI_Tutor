---
source_image: page_229.png
page_number: 229
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 18.37
tokens: 6417
characters: 1313
timestamp: 2025-12-24T04:01:07.680044
finish_reason: stop
---

net.ipv4.tcp_rfc1337 = 1
net.ipv4.tcp_syncookies = 1
net.ipv4.tcp_synack_retries = 1
net.ipv4.tcp_syn_retries = 2
net.ipv4.tcp_max_syn_backlog = 16384
net.ipv4.tcp_timestamps = 1
net.ipv4.tcp_sack = 1
net.ipv4.tcp_fack = 1
net.ipv4.tcp_ecn = 2
net.ipv4.tcp_fin_timeout = 10
net.ipv4.tcp_keepalive_time = 600
net.ipv4.tcp_keepalive_intvl = 60
net.ipv4.tcp_keepalive_probes = 10
net.ipv4.tcp_no_metrics_save = 1
net.ipv4.ip_forward = 0
net.ipv4.conf.all.accept_redirects = 0
net.ipv4.conf.all.send_redirects = 0
net.ipv4.conf.all.accept_source_route = 0
net.ipv4.conf.all.rp_filter = 1

Все эти строки помогут повысить производительность вашего сервера во время DDoS-атаки — он дольше продержится и у вас будет дополнительное время на определение источника атаки и его блокировку. Чтобы данные изменения вступили в силу, выполните команду sudo sysctl -p.

14.2.4. Блокируем все подозрительное

Предотвратить DDoS-атаку могут и определенные правила брандмауэра. Мы будем использовать iptables, поскольку он более гибкий в настройке и предоставляет те возможности, которых нет в других продуктах.

Блокируем неправильные пакеты:

iptables -t mangle -A PREROUTING -m conntrack --ctstate INVALID -j DROP

Блокируем новые не-SYN пакеты:

iptables -t mangle -A PREROUTING -p tcp ! --syn -m conntrack --ctstate NEW -j DROP