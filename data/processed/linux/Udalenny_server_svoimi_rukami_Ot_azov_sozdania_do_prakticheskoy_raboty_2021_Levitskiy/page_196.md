---
source_image: page_196.png
page_number: 196
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 32.35
tokens: 6472
characters: 1215
timestamp: 2025-12-24T04:00:39.369703
finish_reason: stop
---

Листинг 11.2. Пример файла dhcpd.conf для сложной сети

shared-network my_bignet {

# Доменное имя и имена DNS-серверов
option domain-name "company.com";
option domain-name-servers ns1.company.com ns2.company.com;
company.com
# Шлюз по умолчанию
option routers 192.168.0.1;

# Подсети 192.168.1.0 и 192.168.2.0
subnet 192.168.0.0 netmask 255.255.252.0 {
    range 192.168.0.101 192.168.0.200;
}
subnet 192.168.1.0 netmask 255.255.252.0 {
    range 192.168.1.101 192.168.1.200;
}

Если для подсетей 192.168.0.0 и 192.168.1.0 нужно указать различные параметры, например, разные шлюзы или разные имена DNS-серверов, то соответствующие параметры нужно указать в директиве subnet для определенной подсети.

11.5. Статические IP-адреса. Директива host

Иногда нужно привязать некоторые IP-адреса к МАС-адресам. Это полезно, если в вашей сети есть несколько компьютеров, IP-адреса которых не должны изменяться (как правило, это серверы сети и некоторые специальные компьютеры вроде компьютера администратора). Статические IP-адреса описываются с помощью директивы host:

host server {
    option host-name "server";
    option routers 192.168.1.1;
    hardware ethernet 00:FF:FB:69:DC:E5;
    fixed-address 192.168.1.99;
}