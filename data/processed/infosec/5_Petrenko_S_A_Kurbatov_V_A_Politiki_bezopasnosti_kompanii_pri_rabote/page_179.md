---
source_image: page_179.png
page_number: 179
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 47.35
tokens: 12328
characters: 2189
timestamp: 2025-12-23T23:42:52.897468
finish_reason: stop
---

255.255.255.252 eq 53
    access-list SecureData-ACL permit udp 172.16.5.0 255.255.255.0 host 172.16.6.33 eq 162
    access-list WebDMZ-ACL permit icmp 172.16.5.0 255.255.255.0 172.16.3.0 255.255.255.0 source-quench
    access-list SecureData-ACL deny ip any any

Списки контроля доступа для интерфейса Management:

    ...
    access-list Management-ACL permit udp host 172.16.6.33 172.16.0.0 255.255.0.0 eq 161
    access-list Management-ACL permit udp host 172.16.6.33 70.70.70.16 255.255.255.252 eq 161
    access-list Management-ACL permit tcp 172.16.6.0 255.255.255.0 172.16.1.8 255.255.248 eq 22
    access-list Management-ACL permit tcp 172.16.6.0 255.255.255.0 172.16.4.96 255.255.224 eq 22
    access-list Management-ACL permit tcp 172.16.6.0 255.255.255.0 object-group WindowsTS eq 3389
    access-list Management-ACL permit tcp host 172.16.6.13 172.16.1.4 255.255.255.252 object-group FWI-In
    access-list Management-ACL permit udp host 172.16.6.13 172.16.1.4 255.255.255.252 eq 259
    access-list Management-ACL deny ip any any

Списки контроля доступа для интерфейса Internal:

    ...
    access-list Internal-ACL permit tcp 172.16.32.0 255.255.224.0 172.16.4.104 255.255.255.252 eq 8080
    access-list Internal-ACL permit tcp host 172.16.17.46 172.16.4.108 255.255.255.252 eq 25
    access-list Internal-ACL permit udp 172.16.17.20 255.255.255.252 172.16.4.112 255.255.255.252 eq 53
    access-list Internal-ACL permit tcp 172.16.17.20 255.255.255.252 172.16.4.112 255.255.255.252 eq 53
    access-list Internal-ACL permit tcp 172.16.35.0 255.255.255.248 host 172.16.5.30 eq 2002
    access-list Internal-ACL permit tcp 172.16.36.0 255.255.255.248 172.16.5.32 255.255.255.252 eq 445
    access-list Internal-ACL permit udp 172.16.16.16 255.255.248.0 host 172.16.6.33 eq 162
    access-list Internal-ACL permit udp 172.16.17.16 255.255.255.252 host 172.16.6.41 eq 123
    access-list Internal-ACL deny ip any any

Включение списков контроля доступа:

    ...
    access-group AdminDMZ-ACL in interface AdminDMZ
    access-group WebDMZ-ACL in interface WebDMZ
    access-group ServiceDMZ-ACL in interface ServiceDMZ
    access-group SecureData-ACL in interface SecureData