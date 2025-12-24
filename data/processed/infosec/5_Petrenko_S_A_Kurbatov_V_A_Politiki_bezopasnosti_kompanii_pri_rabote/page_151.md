---
source_image: page_151.png
page_number: 151
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 14.71
tokens: 11503
characters: 1260
timestamp: 2025-12-23T23:40:57.670339
finish_reason: stop
---

no service tcp-small-servers
no service tcp-small-servers

Чтобы уменьшить для злоумышленника возможности получения дополнительной информации о маршрутизации, надо отключить сервисы finger и identd. Также требуется отключить HTTP-, DNS-, DHCP-, bootp-сервисы:

no ip finger
no service finger
no ip identd
no ip http server
no ip bootp service
no ip domain-lookup
no service pad
no service dhcp
no call rsvp-sync

Определяется максимальное количество получателей для SMTP-соединений для встроенной в IOS функции поддержки факсов. Установка максимального количества, равного 0, означает отключение сервиса:

mta receive maximum-recipients 0

Отключение протокола CDP (Cisco Discovery Protocol), который позволяет обмениваться информацией канального уровня с другими устройствами от компании Cisco:

no cdp running

Отключение функций proxy arp на маршрутизаторе. Proxy arp позволяет распространяться ARP-запросам по смежным сетям, что дает злоумышленнику дополнительную возможность узнать о структуре сети:

no ip proxy-arp

Для того чтобы в сообщениях, отправляемых по syslog, присутствовала временная метка, необходимо выполнить команды:

service timestamps debug datetime msec localtime showtimezone
service timestamps log datetime msec localtime showtimezone