---
source_image: page_150.png
page_number: 150
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 27.91
tokens: 11669
characters: 1717
timestamp: 2025-12-23T23:41:06.271883
finish_reason: stop
---

aaa authorization commands 15 default group tacacs+ local
aaa accounting exec default start-stop group tacacs+
aaa accounting commands 15 default start-stop group tacacs+

Используемый метод аутентификации применяется для консольного доступа:

...
line console 0
login authentication default exec-timeout 5 0
logging synchronous

Предупреждающий баннер:

...
banner login «This is a private computer system for authorized use only.
All access is logged and monitored. Violators could be prosecuted».

«Ежедневное» сообщение, выводимое в первую очередь при попытке получения доступа к маршрутизатору:

...
banner motd «This is a private computer system for authorized use only.
All access is logged and monitored. Violators could be prosecuted».

Сообщение, выводимое при входе в непrivилегированный (EXEC) режим:

...
banner exec «Any unauthorized access will be vigorously prosecuted».

Маршрутизация «от источника». Отключение маршрутизации «от источника».
Маршрутизация от источника дает пакетам возможность переносить информацию о «верном» или более удобном маршруте и позволяет пренебречь правилами, которые предписаны в таблице маршрутизации для данного пакета, то есть модифицирует маршрут пакета. Это позволяет злоумышленнику управлять трафиком по своему желанию.
Необходимо отключить маршрутизацию «от источника»:

...
no ip source-route

4.3.2. Сервисы маршрутизатора
Необходимо отключить все неиспользуемые и опасные сервисы на маршрутизаторе и сконфигурировать нужные сервисы для обеспечения безопасности. Некоторые из них уже отключены по умолчанию в версии IOS 12.3, поэтому здесь они приводятся для дополнительной проверки.
«Малые» сервисы. Отключение редко используемых UDP-и TCP-сервисов диагностики: