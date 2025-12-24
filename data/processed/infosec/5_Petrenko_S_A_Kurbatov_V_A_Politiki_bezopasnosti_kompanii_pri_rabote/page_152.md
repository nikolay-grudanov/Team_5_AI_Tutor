---
source_image: page_152.png
page_number: 152
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 27.81
tokens: 11627
characters: 1430
timestamp: 2025-12-23T23:41:14.369389
finish_reason: stop
---

Конфигурирование SNMP. Так как мониторинг сетевых устройств осуществляется из сети управления и является критичным аспектом обеспечения высокой доступности, решено использовать SNMP, несмотря на проблемы безопасности, связанные с ним. Для минимизации риска предприняты следующие шаги:
• запрещен SNMP-трафик в Интернет и из Интернета;
• ограничено количество используемых счетчиков.
Используемые команды:

snmp-server view NNM-Only internet included
snmp-server view NNM-Only ipRouteTable excluded
snmp-server view NNM-Only ipNetToMediaTable excluded
snmp-server view NNM-Only at excluded

Списки контроля доступа сконфигурированы для ограничения доступа только с HP OpenView NNM:

access-list 5 permit host 172.16.6.33

и SNMP используется только для чтения:

snmp-server community ThaaMasdf view NNM-Only RO 5

Маршрутизатор также сконфигурирован для отправки trap только к SNMP-серверу:

snmp-server host 172.16.6.33 Thaa!!asdf
snmp-server enable traps config
snmp-server enable traps envmon
snmp-server enable traps bgp
snmp-server trap-authentication
snmp-server trap-source Fa0/0

Конфигурирование протокола NTP Сконфигурирован список контроля доступа для ограничения получения времени через NTP только с сервера времени:

access-list 10 permit 172.16.6.41
access-list 10 deny any
ntp authentication-key 1 md5 Hn!hj
ntp authenticate
ntp trusted-key 1
ntp access-group peer 10
ntp update-calendar
ntp server 172.16.6.41 key 1