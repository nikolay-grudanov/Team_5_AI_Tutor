---
source_image: page_751.png
page_number: 751
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 34.69
tokens: 7694
characters: 1808
timestamp: 2025-12-24T05:06:30.328516
finish_reason: stop
---

мер -p tcp. Перед добавлением нового правила следует удалить правило из предыдущего примера с помощью параметра -D. В противном случае оно будет использоваться брандмауэром netfilter/iptables для пакетов от 10.140.67.22 (Host-B):

# iptables -D INPUT 1
# iptables -A INPUT -s 10.140.67.22 -p tcp --dport 22 -j DROP
# iptables -vnL

Chain INPUT (policy ACCEPT)
Target     prot opt source      destination
DROP       tcp  --  10.140.67.22 anywhere tcp dpt:ssh

Chain FORWARD (policy ACCEPT)
target     prot opt source      destination

Chain OUTPUT (policy ACCEPT)
target     prot opt source      destination

Во-первых, новое правило iptables тестируется с сервера Host-C, чтобы гарантировать, что и попытки команды ping, и ssh-соединения не затрагиваются. Как видно в примере, это сработало:

$ ping -c 2 10.140.67.23
PING 10.140.67.23 (10.140.67.23) 56(84) bytes of data.
64 bytes from 10.140.67.23: icmp_req=1 ttl=64 time=1.04 ms
64 bytes from 10.140.67.23: icmp_req=2 ttl=64 time=0.740 ms

--- 10.140.67.23 ping statistics ---
2 packets transmitted, 2 received, 0% packet loss, time 1000ms
rtt min/avg/max/mdev = 0.740/0.892/1.045/0.155 ms

$ ssh root@10.140.67.23
root@10.140.67.23's password:

Затем новое правило iptables тестируется с сервера Host-B, чтобы убедиться, что ping работает и ssh-соединения заблокированы. Как видно в примере, это тоже сработало:

$ ping -c 2 10.140.67.23

PING 10.140.67.23 (10.140.67.23) 56(84) bytes of data.
64 bytes from 10.140.67.23: icmp_req=1 ttl=64 time=1.10 ms
64 bytes from 10.140.67.23: icmp_req=2 ttl=64 time=0.781 ms

--- 10.140.67.23 ping statistics ---

2 packets transmitted, 2 received, 0% packet loss, time 1001ms
rtt min/avg/max/mdev = 0.781/0.942/1.104/0.164 ms

$ ssh root@10.140.67.23

ssh: connect to host 10.140.67.23 port 22: Connection timed out