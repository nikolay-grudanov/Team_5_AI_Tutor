---
source_image: page_182.png
page_number: 182
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 17.28
tokens: 11539
characters: 1075
timestamp: 2025-12-23T23:42:34.942779
finish_reason: stop
---

использования защищенного протокола для управления сконфигурирован SSH. Для этого сначала создается пара ключей:

ca generate rsa key 1024
ca save all

Далее отключается Telnet:

ssh 172.16.6.0 255.255.255.0 Management
ssh timeout 15
no telnet

Журналирование событий межсетевого экрана. Журналирование событий межсетевого экрана является критически важным для надежного функционирования сети. Межсетевые экраны сконфигурированы для отправки сообщений на сервер Cisco SIMS:

logging buffered warnings
logging host Management 172.16.6.25
logging trap informational
logging timestamp
logging on

Конфигурирование SNMP. Межсетевой экран конфигурируется для отправки trap только к SNMP-серверу:

snmp-server community TopoE6?%HU
snmp-server host 172.16.6.33 Management trap
snmp-server enable traps
logging on

4.3.6. Настройка корпоративной системы защиты от вирусов
Все серверы и рабочие станции внутренней сети компании защищены с помощью Symantec Antivirus Corporate Edition v.8.1. Политики управляются централизованно с использованием Symantec System Center (см. рис. 4.11).