---
source_image: page_352.png
page_number: 352
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 29.41
tokens: 7696
characters: 1931
timestamp: 2025-12-24T04:42:24.135215
finish_reason: stop
---

Вот текст, который выделен на изображении:

```
rick@ubuntu:~$ pgrep busybox
12089

rick@ubuntu:~$ sudo ip netns attach anotherdimension 12089

rick@ubuntu:~$ ip netns list
anotherdimension

↓ ①                ↓ ②
rick@ubuntu:~$ sudo ip link add c137net0 type veth peer name net0 ①

rick@ubuntu:~$ sudo ip link show
...
4: net0@c137net0: <BROADCAST,MULTICAST,M-DOWN> mtu 1500 qdisc noop state DOWN ... qlen 1000
    link/ether a6:71:65:45:fd:c2 brd ff:ff:ff:ff:ff:ff
5: c137net0@net0: <BROADCAST,MULTICAST,M-DOWN> mtu 1500 qdisc noop state DOWN ... qlen 1000
    link/ether e2:bd:81:ee:fe:bf brd ff:ff:ff:ff:ff:ff

rick@ubuntu:~$ sudo ip link set net0 netns anotherdimension ●

/ # ip link show
4: net0@if20: <BROADCAST,MULTICAST,M-DOWN> mtu 1500 qdisc noop qlen 1000
    link/ether a6:71:65:45:fd:c2 brd ff:ff:ff:ff:ff:ff
/ # ip addr add 10.0.0.137/24 dev net0 ●
/ # ip addr show dev net0
4: net0@if20: <BROADCAST,MULTICAST,M-DOWN> mtu 1500 qdisc noop qlen 1000
    link/ether a6:71:65:45:fd:c2 brd ff:ff:ff:ff:ff:ff
    inet 10.0.0.137/24 scope global net0
        valid_lft forever preferred_lft forever

rick@ubuntu:~$ ip link show dev c137net0
5: c137net0@if19: <BROADCAST,MULTICAST> mtu 1500 qdisc noop state DOWN ... qlen 1000
    link/ether e2:bd:81:ee:fe:bf brd ff:ff:ff:ff:ff:ff link-netns anotherdimension

rick@ubuntu:~$ sudo ip addr add 10.0.0.1/24 dev c137net0 ●
rick@ubuntu:~$ ip link set dev c137net0 up ●
rick@ubuntu:~$ ip addr show dev c137net0
20: c137net0@if19: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc noop state UP ...
    link/ether e2:bd:81:ee:fe:bf brd ff:ff:ff:ff:ff:ff link-netns anotherdimension
    inet 10.0.0.1/24 scope global c137net0
        valid_lft forever preferred_lft forever

rick@ubuntu:~$ ping 10.0.0.137
PING 10.0.0.137 (10.0.0.137) 56(84) bytes of data.
64 bytes from 10.0.0.137: icmp_seq=1 ttl=64 time=0.085 ms ●
64 bytes from 10.0.0.137: icmp_seq=2 ttl=64 time=0.116 ms

^C
```