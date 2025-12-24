---
source_image: page_253.png
page_number: 253
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 55.28
tokens: 8306
characters: 3079
timestamp: 2025-12-24T04:39:34.574441
finish_reason: stop
---

**Листинг 6.6. Сетевые сокеты (Linux ss(8))**

lumpy@ubuntu:~$ sudo ss -4atupn

<table>
  <tr>
    <th>Netid</th>
    <th>State</th>
    <th>Recv-Q</th>
    <th>Send-Q</th>
    <th>Local Address:Port</th>
    <th>Peer Address:Port</th>
    <th></th>
  </tr>
  <tr>
    <td>udp</td>
    <td>UNCONN</td>
    <td>0</td>
    <td>0</td>
    <td>127.0.0.53%lo:53</td>
    <td>0.0.0.0:*</td>
    <td>users:(("systemd-resolve",pid=638,fd=12))</td>
  </tr>
  <tr>
    <td>udp</td>
    <td>UNCONN</td>
    <td>0</td>
    <td>0</td>
    <td>192.168.0.101%wlp2s0:68</td>
    <td>0.0.0.0:*</td>
    <td>users:(("NetworkManager",pid=684,fd=19))</td>
  </tr>
  <tr>
    <td>tcp</td>
    <td>LISTEN</td>
    <td>0</td>
    <td>128</td>
    <td>0.0.0.0:22</td>
    <td>0.0.0.0:*</td>
    <td>users:(("sshd",pid=864,fd=3))</td>
  </tr>
  <tr>
    <td>tcp</td>
    <td>LISTEN</td>
    <td>0</td>
    <td>S</td>
    <td>0.0.0.1:631</td>
    <td>0.0.0.0:*</td>
    <td>users:(("cupsd",pid=697,fd=7))</td>
  </tr>
  <tr>
    <td>tcp</td>
    <td>LISTEN</td>
    <td>0</td>
    <td>128</td>
    <td>127.0.0.1:5432</td>
    <td>0.0.0.0:*</td>
    <td>users:(("postgres",pid=1039,fd=3))</td>
  </tr>
  <tr>
    <td>tcp</td>
    <td>LISTEN</td>
    <td>0</td>
    <td>100</td>
    <td>0.0.0.0:25</td>
    <td>0.0.0.0:*</td>
    <td>users:(("master",pid=1250,fd=13))</td>
  </tr>
  <tr>
    <td>tcp</td>
    <td>LISTEN</td>
    <td>0</td>
    <td>128</td>
    <td>127.0.0.53%lo:53</td>
    <td>0.0.0.0:*</td>
    <td>users:(("systemd-resolve",pid=638,fd=13))</td>
  </tr>
  <tr>
    <td>tcp</td>
    <td>ESTAB</td>
    <td>0</td>
    <td>0</td>
    <td>192.168.0.101:22</td>
    <td>192.168.0.103:57622</td>
    <td>users:(("sshd",pid=6234,fd=4),("sshd",pid=6152,fd=4))</td>
  </tr>
</table>

Из примеров листингов 6.5 и 6.6 видны 5 «слушающих» (LISTEN) сокетов TCP и 2 «несоединенных» (UNCONN) сокета UDP, открытых разными службами операционной системы. Например, 22-й порт TCP открыл сервер sshd, PID = 864 службы удаленного доступа W:[SSH], а 5432-й порт TCP — сервер postgres, PID = 1039 службы реляционной СУБД W:[SQL].

**6.2. Конфигурирование сетевых интерфейсов и протоколов**

**6.2.1. Ручное конфигурирование**

Для функционирования разных стеков протоколов сетевым интерфейсам должны быть предварительно назначены корректные сетевые адреса и сконфигурированы прочие параметры, что может быть выполнено вручную администратором или автоматически специальными службами этих стеков.

Ручное назначение сетевых адресов стека TCP/IP выполняется при помощи команды ifconfig(8) или ip(8), а простейшая диагностика — при помощи команды ping(1), как проиллюстрировано в листинге 6.7.

**Листинг 6.7. Ручное конфигурирование сетевых интерфейсов**

lumpy@ubuntu:~$ sudo ifconfig eno1 10.0.0.10 up
lumpy@ubuntu:~$ sudo ifconfig eno1
eno1: flags=4163<UP,BROADCAST,RUNNING,MULTICAST> mtu 1500
    inet 10.0.0.10 netmask 255.0.0.0 broadcast 10.255.255.255
    inet6 fe80::66f6:6415:7455:6a0f prefixlen 64 scopeid 0x20<link>
    ether 08:00:27:c0:67:8f txqueuelen 1000 (Ethernet)
    RX packets 0 bytes 0 (0.0 B)