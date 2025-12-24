---
source_image: page_750.png
page_number: 750
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 34.73
tokens: 7683
characters: 2031
timestamp: 2025-12-24T05:06:29.945747
finish_reason: stop
---

В следующем примере политика DROP должна быть сначала изменена на ALLOW в iptables Host-A. После этого необходимо добавить специальное правило для блокировки сетевых пакетов только с IP-адреса Host-B 10.140.67.22:

# iptables -P INPUT ACCEPT
# iptables -A INPUT -s 10.140.67.22 -j DROP
# iptables -vnL
Chain INPUT (policy ACCEPT)
target     prot opt source                destination
DROP all -- 10.140.67.22 anywhere

Chain FORWARD (policy ACCEPT)
Target     prot opt source                destination

Chain OUTPUT (policy ACCEPT)
target     prot opt source                destination

Теперь сервер Host-C может успешно использовать ping и ssh на сервере Host-A, реализуя одну из поставленных целей:

$ ping -c 2 10.140.67.23
PING 10.140.67.23 (10.140.67.23) 56(84) bytes of data.
64 bytes from 10.140.67.23: icmp_req=1 ttl=64 time=11.7 ms
64 bytes from 10.140.67.23: icmp_req=2 ttl=64 time=0.000 ms

--- 10.140.67.23 ping statistics ---
2 packets transmitted, 2 received, 0% packet loss, time 1008ms
rtt min/avg/max/mdev = 0.000/5.824/11.648/5.824 ms
$ ssh root@10.140.67.23
root@10.140.67.23's password:

Однако Host-B не может использовать ping и ssh на сервере Host-A. Таким образом, применяемое правило не помогает в достижении общей цели:

$ ping -c 2 10.140.67.23

PING 10.140.67.23 (10.140.67.23) 56(84) bytes of data.

--- 10.140.67.23 ping statistics ---
2 packets transmitted, 0 received, 100% packet loss, time 1007ms

$ ssh root@10.140.67.23

ssh: connect to host 10.140.67.23 port 22: Connection timed out

Блокировка протокола и порта. А если вместо полной блокировки IP-адреса сервера Host-B заблокировать только соединения с ssh-портом (порт 22) с IP-адреса Host-B? Даст ли серверу Host-C полный доступ к серверу Host-A то, что заблокированы только ssh-соединения от сервера Host-B?

В следующем примере правила iptables для сервера Host-A модифицируются, чтобы попытаться заблокировать IP-адрес Host-B из порта 22. Обратите внимание на то, что параметр --dport должен сопровождать определенный протокол, напри-