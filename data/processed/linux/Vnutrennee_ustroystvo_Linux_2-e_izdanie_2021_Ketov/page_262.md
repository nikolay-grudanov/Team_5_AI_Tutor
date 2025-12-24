---
source_image: page_262.png
page_number: 262
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 19.34
tokens: 7373
characters: 1269
timestamp: 2025-12-24T04:39:18.917217
finish_reason: stop
---

port = [554]
txt = ["path=mpeg4/1/media.mp"]
= eth0 IPv4 NVR(SMB)        Microsoft Windows Network    local
hostname = [NVR.local]
address = [192.168.17.90]
port = [445]
txt = []
= eth0 IPv4 NVR(NFS)         Network File System         local
hostname = [NVR.local]
address = [192.168.17.90]
port = [2049]
txt = []

lumpy@ubuntu:~$ avahi-resolve --name NVR.local NPI4C6BF5.local axis-00408c81d401.local
NVR.local      192.168.17.90
NPI4C6BF5.local 192.168.17.68
axis-00408c81d401.local 192.168.17.142

lumpy@ubuntu:~$ getent hosts NVR.local NPI4C6BF5.local axis-00408c81d401.local
192.168.17.90   NVR.local
192.168.17.68   NPI4C6BF5.local
192.168.17.142  axis-00408c81d401.local

Для диагностики mDNS-модуля службы имен неизменно используется команда getent(8), а для непосредственной диагностики mDNS-сервера avahi-daemon(8) — специальная команда avahi-resolve(1).

6.4. Сетевые службы

6.4.1. Служба SSH

Служба W:[SSH] предназначена¹ для организации безопасного (secure) доступа к сеансу командного интерпретатора (shell) удаленных сетевых узлов. Изначально разрабатывалась как замена небезопасным R-утилитам W:[Rlogin], W:[Rsh] и протоколу сетевого алфавитно-цифрового терминала W:[telnet].

¹ О SSH протоколе с картинками можно узнать здесь: https://tiny.cc/ocxqgz.