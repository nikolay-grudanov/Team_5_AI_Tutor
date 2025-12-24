---
source_image: page_261.png
page_number: 261
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 29.96
tokens: 7709
characters: 2260
timestamp: 2025-12-24T04:39:27.681848
finish_reason: stop
---

Сетевые устройства (принтеры, камеры, видеорегистраторы и пр.) и «клиентские» узлы локальных сетей, динамически получающие случайные IP-адреса при помощи DHCP, на ответственных серверах DNS почти никогда не регистрируются, а использование их имен в локальной сети (в «домене» .local) становится возможным благодаря службе W:[mDNS].

Серверы mDNS запускаются на каждом «клиентском» узле и регистрируют у себя соответствия собственных IP-адресов своему имени, а затем используют многоадресную (multicast) рассылку стандартных запросов DNS для получения информации друг у друга. Сервером mDNS, как показано в примере из листинга 6.13, является avahi-daemon(8), реализующий еще и службу W:[DNS-SD] (DNS service discovery), которая позволяет узлам локальной сети обнаруживать (discovery) услуги (service), предоставляемые другими узлами. При помощи avahi-browse(1) проиллюстрирован список всех (-a, all) имен и типов услуг, объявленных узлами сети и сохраненных в локальном кэше (-c, cache), а также результаты (-r, resolve) запросов на получение информации об услугах.

Листинг 6.13. mDNS/DNS-SD-клиент

lumpy@ubuntu:~$ sudo ss -4autpn sport = :mdns
sudo ss -4autpn sport = :mdns
Netid State Recv-Q Send-Q Local Address:Port Peer Address:Port
udp UNCONN 0 0 0.0.0.0:5353 0.0.0.0:* users:(("avahi-daemon",pid=678,...))

lumpy@ubuntu:~$ avahi-browse -arcl
+ eth0 IPv4 HP LaserJet 700 M712 [4C6BF5] UNIX Printer local
+ eth0 IPv4 AXIS 211M - 00408C81D401 RTSP Realtime Streaming Server local
+ eth0 IPv4 NVR(SMB) Microsoft Windows Network local
+ eth0 IPv4 NVR(NFS) Network File System local
= eth0 IPv4 HP LaserJet 700 M712 [4C6BF5] UNIX Printer local
hostname = [NPI4C6BF5.local]
address = [192.168.17.68]
port = [515]
txt = ["Scan=F" "UUID=56ff35dd-1065-4e5e-9385-3c26b8946b79" "Color=F" "Duplex=T" "Binary=T" "Transparent=T" "note=" "adminurl=http://NPI4C6BF5.local." "priority=40" "usb_MDL=HP LaserJet 700 M712" "usb_MFC=Hewlett-Packard" "product=(HP LaserJet 700 M712)" "ty=HP LaserJet 700 M712" "URF=V1.1,CP99,RS600,MT1-2-3-5-12,W8,PQ4,IS20-21-22-23,DM1,OB1" "pdl=application/postscript" "rp=BINPS" "qtotal=4" "txtvers=1"]
= eth0 IPv4 AXIS 211M - 00408C81D401 RTSP Realtime Streaming Server local
hostname = [axis-00408c81d401.local]
address = [192.168.17.142]