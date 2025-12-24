---
source_image: page_195.png
page_number: 195
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 25.72
tokens: 6414
characters: 1245
timestamp: 2025-12-24T04:00:31.904370
finish_reason: stop
---

Листинг 11.1. Пример файла dhcpd.conf для простой сети

ddns-update-style interim;

# Расположение базы данных с арендой IP-адресов
lease-file-name "/var/lib/dhcpd/dhcpd.leases";

# Данный сервер является официальным DHCP-сервером для локальной сети
authoritative;

# Доменное имя и имена DNS-серверов
option domain-name "company.com";
option domain-name-servers ns1.company.com ns2.company.com

# Время аренды
default-lease-time 86400;   # 24 часа
max-lease-time 172800;     # 48 часов

subnet 192.168.0.0 netmask 255.255.255.0 {
    option routers 192.168.0.1;
    option subnet-mask 255.255.255.0;
    range 192.168.0.101 192.168.0.200;
}

Мы удалили из dhcpd.conf все лишнее и наш файл получился довольно компактным (сравните его с файлом по умолчанию, где в качестве примера приводятся чуть ли не все мыслимые и немыслимые параметры).

11.4. DHCP-сервер в больших сетях

Далее мы рассмотрим пример более сложной сети с несколькими подсетями — ради чего, собственно, и есть смысл настраивать DHCP-сервер вручную, а не использовать встроенный в маршрутизатор DHCP. Общая сеть должна быть описана в директиве shared-network, а все подсети должны быть описаны директивами subnet внутри директивы shared-network. Пример приведен в листинге 11.2.