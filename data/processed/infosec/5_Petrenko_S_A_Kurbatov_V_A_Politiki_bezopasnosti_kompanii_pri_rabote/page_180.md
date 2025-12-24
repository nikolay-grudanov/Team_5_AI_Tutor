---
source_image: page_180.png
page_number: 180
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 12.52
tokens: 11595
characters: 1498
timestamp: 2025-12-23T23:42:18.202617
finish_reason: stop
---

access-group Management-ACL in interface Management
access-group Internal-ACL in interface Internal

Настойка TACACS+. TACACS+ используется для централизованного управления аутентификацией и авторизацией доступа к межсетевым экранам. Определяем IP-адрес сервера TACACS+ и пароль для аутентификации:

...
aaa-server TACACS+ (Management) host 172.16.6.21 F$!19Ty timeout 5
...
Используемый метод аутентификации применяется для консольного доступа:

...
aaa authentication serial console TACACS+
...
Предупреждающий баннер:

...
banner login «This is a private computer system for authorized use only. All access is logged and monitored. Violators could be prosecuted».
...
«Ежедневное» сообщение, выводимое в первую очередь при попытке получения доступа к межсетевому экрану:

...
banner motd «This is a private computer system for authorized use only. All access is logged and monitored. Violators could be prosecuted».
...
Сообщение, выводимое при входе в непrivилегированный (EXEC) режим:

...
banner exec «Any unauthorized access will be vigorously prosecuted».
...

Настойка встроенной системы IDS. Cisco PIX имеет встроенную систему обнаружения вторжений. Хотя по количеству сигнатур система уступает устройствам серии Cisco IDS 4200, все же имеет смысл сконфигурировать ее для отсылки сообщений в случае атак:

...
ip audit info action alarm
ip audit attack action alarm
...
Защита системы аутентификации. Для защиты от атак на переполнение системы аутентификации используется следующая опция: