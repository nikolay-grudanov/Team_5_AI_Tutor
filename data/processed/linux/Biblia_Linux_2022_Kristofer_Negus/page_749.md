---
source_image: page_749.png
page_number: 749
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 32.15
tokens: 7603
characters: 2003
timestamp: 2025-12-24T05:06:22.696700
finish_reason: stop
---

Во-первых, что произойдет, если политика INPUT будет изменена с ACCEPT на DROP? Достигнет ли она цели? Посмотрите, что будет, если попытаться это сделать. Помните, что если для входящего пакета не указано никаких правил, то соблюдается политика chain's policy. Это изменение внесено в брандмауэр Host-A в следующем примере:

# iptables -P INPUT DROP
# iptables -vnL

Chain INPUT (policy DROP)
target    prot opt source                destination

Chain FORWARD (policy ACCEPT)
target    prot opt source                destination

Chain OUTPUT (policy ACCEPT)
target    prot opt source                destination

СОВЕТ
Для политик нельзя установить цель REJECT. При такой попытке выдается сообщение iptables: Bad policy name. Вместо этого используйте в качестве политики DROP.

Host-B пытается пропинговать Host-A, а затем установить ssh-соединение, как показано в следующем примере. Здесь обе попытки провалились. Поскольку команда ping заблокирована, это не соответствует цели блокировать только удаленные подключения входа с помощью ssh от Host-B:

$ ping -c 2 10.140.67.23
PING 10.140.67.23 (10.140.67.23) 56(84) bytes of data.

--- 10.140.67.23 ping statistics ---
2 packets transmitted, 0 received, 100% packet loss, time 1007ms
$ ssh root@10.140.67.23

ssh: connect to host 10.140.67.23 port 22: Connection timed out

Попытки сервера Host-C пинговать Host-A и установить ssh-соединение терпят неудачу. Таким образом подтверждается, что настройка брандмауэра, где политика INPUT равна DROP, не поможет в достижении цели:

$ ping -c 2 10.140.67.23
PING 10.140.67.23 (10.140.67.23) 56(84) bytes of data.

--- 10.140.67.23 ping statistics ---
2 packets transmitted, 0 received, 100% packet loss, time 1008ms
$ ssh root@10.140.67.23

ssh: connect to host 10.140.67.23 port 22: Connection timed out

Блокировка источника IP-адресов. А что, если вместо этого будет заблокирован только IP-адрес сервера Host-B? Это позволило бы Host-C достичь сервера Host-A. Поможет ли эта настройка добиться желаемого?