---
source_image: page_143.png
page_number: 143
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 29.68
tokens: 7630
characters: 2176
timestamp: 2025-12-24T04:35:59.077212
finish_reason: stop
---

При отключении передачи полномочий 2 программа /bin/ping лишается возможности выполнять свои функции, а при назначении ей при помощи команды setcap(8) «файловой» привилегии CAP_NET_RAW 3 функциональность возвращается в полном объеме, т. к. приводит к установке «процессной» привилегии CAP_NET_RAW при запуске этой программы. Для просмотра привилегий, делегируемых при запуске программ, используется парная команда getcap(8).

Аналогично, при использовании анализаторов сетевого трафика tshark(1) (листинг 4.25) и/или wireshark(1), вызывающих для захвата сетевых пакетов утилиту dumpcap(1), требуется открывать как «необработанные» raw(7), так и пакетные packet(7) сетевые сокеты, что требует той же привилегии CAP_NET_RAW. Классический способ применения анализаторов пакетов состоит в использовании явной передачи всех полномочий суперпользователя (при помощи su(1) или sudo(1)) при их запуске, что опять не соответствует минимально необходимым и достаточным требованиям к разрешенным возможностям программ.

Листинг 4.25. Делегирование привилегий программе tshark(1)

fitz@ubuntu:~$ tshark
tshark: There are no interfaces on which a capture can be done
itz@ubuntu:~$ strace -fe execve tshark
execve("/usr/bin/tshark", ["tshark"], [/* 23 vars */]) = 0
Process 8951 attached
[pid 8951] execve("/usr/bin/dumpcap", ["/usr/bin/dumpcap", "-D", "-Z", "none"],...) = 0
Process 8951 detached
--- SIGCHLD (Child exited) @ 0 (0) ---
tshark: There are no interfaces on which a capture can be done
fitz@ubuntu:~$ ls -la /usr/bin/dumpcap
-rwxr-xr-x 1 root root 104688 Sep 5 19:43 /usr/bin/dumpcap
fitz@ubuntu:~$ getcap /usr/bin/dumpcap

fitz@ubuntu:~$ sudo setcap cap_net_raw+ep /usr/bin/dumpcap
fitz@ubuntu:~$ getcap /usr/bin/dumpcap
/usr/bin/dumpcap = cap_net_raw+ep
fitz@ubuntu:~$ tshark -i wlan0
Capturing on wlan0
0.307205 fe80::895d:9d7d:f0b3:a372 -> ff02::1:ff96:2df6 ICMPv6 86 Neighbor Solicitation
0.307460 SuperMic_74:0e:90 -> Spanning-tree-(for-bridges)_00 STP 60 Conf. Root =
32768/0/00:25:90:74:0e:90 Cost = 0 Port = 0x8001

Для эффективного использования анализаторов трафика непривилегированными пользователями достаточно делегировать их процессам захвата пакетов привилегию