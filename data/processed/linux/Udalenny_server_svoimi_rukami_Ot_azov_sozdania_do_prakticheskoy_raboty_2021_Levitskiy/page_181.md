---
source_image: page_181.png
page_number: 181
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 23.18
tokens: 6374
characters: 1279
timestamp: 2025-12-24T04:00:12.002359
finish_reason: stop
---

auto-trust-anchor-file: "/var/lib/unbound/root.key"

Теперь проверим конфигурацию сервера:

# unbound-checkconf

Если ошибок нет, вы получите сообщение:

unbound-checkconf: no errors in /etc/unbound/unbound.conf

Осталось только перезапустить Unbound:

# service unbound restart

Осталось только настроить DHCP-сервер, чтобы он сообщал всем локальным узлам ваш новый IP-адрес DNS-сервера. В нашем случае - это 192.168.1.1.

10.3. Настройка кэширующего сервера на базе bind

Ради контраста сейчас мы попытаемся настроить кэширующий сервер на базе пакета bind (в некоторых дистрибутивах - bind9). Первым делом установим сам bind:

# apt-get install bind9

Примечание. BIND9 - это уникальный сервер. Его пакет называется bind9, каталог с конфигурационными файлами - /etc/bind, а название конфигурационного файла - named.conf. Процесс (исполнимый файл) называется named. К такому многообразию имен придется привыкнуть. Главное понимать, что это одно и то же.

Раньше основной конфигурационный файл /etc/bind/named.conf был довольно большим, если не огромным. Сейчас в нем только три строчки (лист. 10.2).

Листинг 10.2. Файл /etc/bind/named.conf по умолчанию

include "/etc/bind/named.conf.options";
include "/etc/bind/named.conf.local";
include "/etc/bind/named.conf.default-zones";