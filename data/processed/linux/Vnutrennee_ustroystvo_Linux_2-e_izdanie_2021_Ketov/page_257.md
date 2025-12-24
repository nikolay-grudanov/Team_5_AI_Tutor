---
source_image: page_257.png
page_number: 257
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 34.46
tokens: 7788
characters: 2001
timestamp: 2025-12-24T04:39:22.408156
finish_reason: stop
---

lumpy@ubuntu:~$ nmcli conn

<table>
  <tr>
    <th>NAME</th>
    <th>UUID</th>
    <th>TYPE</th>
    <th>DEVICE</th>
  </tr>
  <tr>
    <td>464+</td>
    <td>57cd20ce-098e-3b31-acd6-f50fd2e4db41</td>
    <td>wifi</td>
    <td>wlp2s0</td>
  </tr>
</table>

lumpy@ubuntu:~$ sudo nmcli conn add type ethernet ifname eno1

Соединение «ethernet-eno1» (eadac6e2-eb71-43ee-9b34-86c2910a382c) добавлено.

lumpy@ubuntu:~$ nmcli conn

<table>
  <tr>
    <th>NAME</th>
    <th>UUID</th>
    <th>TYPE</th>
    <th>DEVICE</th>
  </tr>
  <tr>
    <td>464+</td>
    <td>57cd20ce-098e-3b31-acd6-f50fd2e4db41</td>
    <td>wifi</td>
    <td>wlp2s0</td>
  </tr>
  <tr>
    <td>ethernet-eno1</td>
    <td>eadac6e2-eb71-43ee-9b34-86c2910a382c</td>
    <td>ethernet</td>
    <td>eno1</td>
  </tr>
</table>

lumpy@ubuntu:~$ sudo nmcli conn up ethernet-eno1

Соединение успешно активировано (адрес действующего D-Bus: /org/freedesktop/NetworkManager/ActiveConnection/6)

lumpy@ubuntu:~$ nmcli dev show eno1

GENERAL.DEVICE: eno1
GENERAL.TYPE: ethernet
GENERAL.HWADDR: 08:00:27:C0:67:8F
IP4.ADDRESS[1]: 10.0.2.4/24
IP4.GATEWAY: 10.0.2.1
IP4.ROUTE[1]: dst = 0.0.0.0/0, nh = 10.0.2.1, mt = 101
IP4.ROUTE[2]: dst = 10.0.2.0/24, nh = 0.0.0.0, mt = 10
IP4.DNS[1]: 10.0.2.1

lumpy@ubuntu:~$ ip a show dev eno1

(1) 3: eno1: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc fq_codel state UP ... qlen 1000
link/ether 08:00:27:c0:67:8f brd ff:ff:ff:ff:ff:ff
inet 10.0.2.4/24 brd 10.0.2.255 scope global dynamic noprefixroute eno1
    valid_lft 954sec preferred_lft 954sec
inet6 fe80::9eca:df0a:5401:d34f/64 scope link noprefixroute
    valid_lft forever preferred_lft forever

lumpy@ubuntu:~$ ip route show

(2) default via 10.0.2.1 dev enp0s8 proto dhcp metric 101
10.0.2.0/24 dev enp0s8 proto kernel scope link src 10.0.2.4 metric 101
169.254.0.0/16 dev enp0s3 scope link metric 1000

В листинге 6.9 проиллюстрирован результат работы менеджера подключений при подключении сетевого интерфейса eno1. Полученные при помощи DHCP-клиента