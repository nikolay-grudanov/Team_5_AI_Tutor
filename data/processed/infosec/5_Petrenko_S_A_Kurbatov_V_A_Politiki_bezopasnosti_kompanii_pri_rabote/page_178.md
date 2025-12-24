---
source_image: page_178.png
page_number: 178
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 50.86
tokens: 12448
characters: 2179
timestamp: 2025-12-23T23:42:52.941301
finish_reason: stop
---

access-list WebDMZ-ACL deny ip any any

Списки контроля доступа для интерфейса ServiceDMZ:

access-list ServiceDMZ-ACL permit tcp 172.16.4.108 255.255.255.252 host 172.16.17.46 eq 25
access-list ServiceDMZ-ACL permit udp 172.16.4.104 255.255.255.252 host 172.16.6.25 eq 514
access-list ServiceDMZ-ACL permit udp host 172.16.4.117 host 172.16.6.25 eq 514
access-list ServiceDMZ-ACL permit tcp 172.16.61.0 255.255.255.0 host 172.16.17.54 eq 443
access-list ServiceDMZ-ACL permit tcp 172.16.62.0 255.255.255.248 host 172.16.17.54 eq 443
access-list ServiceDMZ-ACL permit tcp 172.16.61.0 255.255.255.0 172.16.17.32 255.255.248 eq 80
access-list ServiceDMZ-ACL permit tcp 172.16.62.0 255.255.255.248 172.16.17.32 255.255.248 eq 80
access-list ServiceDMZ-ACL permit tcp 172.16.61.0 255.255.255.0 172.16.17.32 255.255.248 eq 443
access-list ServiceDMZ-ACL permit tcp 172.16.62.0 255.255.255.248 172.16.17.32 255.255.248 eq 443
access-list ServiceDMZ-ACL permit tcp 172.16.62.0 255.255.255.248 host 172.16.6.45 eq 22
access-list ServiceDMZ-ACL permit tcp 172.16.62.0 255.255.255.248 host 172.16.6.13 eq 18190
access-list ServiceDMZ-ACL permit tcp 172.16.62.0 255.255.255.248 172.16.6.0 255.255.0 eq 3389
access-list ServiceDMZ-ACL permit tcp host 172.16.4.117 host 172.16.6.17 eq 389
access-list ServiceDMZ-ACL permit udp host 172.16.4.117 host 172.16.6.21 range 1645 1646
access-list ServiceDMZ-ACL permit tcp host 172.16.4.117 host 172.16.6.29 eq 5054
access-list ServiceDMZ-ACL permit udp 172.16.4.0 255.255.255.0 host 172.16.6.33 eq 162
access-list ServiceDMZ-ACL permit udp 172.16.4.0 255.255.255.0 host 172.16.6.41 eq 123
access-list ServiceDMZ-ACL deny ip any any

Списки контроля доступа для интерфейса SecureData:

access-list SecureData-ACL permit udp 172.16.5.48 255.255.255.252 object-group WebDMZServers eq 500
access-list Secure Data-ACL permit ah 172.16.5.48 255.255.255.252 object-group WebDMZServers
access-list Secure Data-ACL permit udp 172.16.5.48 255.255.255.252 host 172.16.6.41 eq 123
access-list SecureData-ACL permit udp 172.16.5.52 255.255.255.252 172.16.4.112 255.255.255.252 eq 53
access-list SecureData-ACL permit tcp 172.16.5.52 255.255.255.252 172.16.4.112