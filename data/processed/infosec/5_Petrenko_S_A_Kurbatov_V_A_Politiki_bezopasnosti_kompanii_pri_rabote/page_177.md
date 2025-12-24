---
source_image: page_177.png
page_number: 177
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 31.29
tokens: 12134
characters: 1962
timestamp: 2025-12-23T23:42:29.431448
finish_reason: stop
---

object-group network WindowsTS group-object WebDMZServers
network-object 172.16.4.112 255.255.255.252
network-object 172.16.5.0 255.255.255.0
network-object 172.16.16.16 255.255.248.0
object-group service FW1-In tcp port-object eq 256
port-object eq 258
port-object eq 18191
port-object eq 18192
port-object eq 18211
object-group service FW1-Out tcp port-object eq 256
port-object eq 257
port-object eq 18210

Списки контроля доступа для интерфейса AdminDMZ:

...
access-list AdminDMZ-ACL permit udp object-group AdminDMZNet host 172.16.6.25 eq514
    access-list AdminDMZ-ACL permit top 172.16.1.4 255.255.255.252 host 172.16.6.13 object-group FW1-Out
    access-list AdminDMZ-ACL permit udp 172.16.1.4 255.255.255.252 host 172.16.6.13 eq 259
    access-list AdminDMZ-ACL permit udp object-group AdminDMZAll host 172.16.6.33 eq162
    access-list AdminDMZ-ACL permit udp object-group AdminDMZAll host 172.16.6.41 eq123
    access-list AdminDMZ-ACL permit top 70.70.70.16 255.255.255.252 host 172.16.6.21 eq 49
access-list AdminDMZ-ACL deny ip any any

Списки контроля доступа для интерфейса WebDMZ:

...
access-list WebDMZ-ACL permit top 172.16.3.64 255.255.255.248 host 172.16.5.30 eq 2002
    access-list WebDMZ-ACL permit top 172.16.3.64 255.255.255.248172.16.5.32 255.255.255.252 eq 445
    access-list WebDMZ-ACL permit udp object-group WebDMZServers 172.16.5.52 255.255.255.252 eq 53
    access-list WebDMZ-ACL permit tcp object-group WebDMZServers 172.16.5.52 255.255.255.252 eq 53
    access-list WebDMZ-ACL permit udp object-group WebDMZServers 172.16.5.48 255.255.255.252 eq 500
    access-list WebDMZ-ACL permit ah object-group WebDMZServers 172.16.5.48 255.255.255.252
    access-list WebDMZ-ACL permit udp object-group WebDMZServers host 172.16.6.33 eq162
    access-list WebDMZ-ACL permit top 172.16.3.16 255.255.255.240 host 172.16.6.9 eq443
    access-list WebDMZ-ACL permit icmp object-group WebDMZServers 172.16.5.0 255.255.255.0 source-quench