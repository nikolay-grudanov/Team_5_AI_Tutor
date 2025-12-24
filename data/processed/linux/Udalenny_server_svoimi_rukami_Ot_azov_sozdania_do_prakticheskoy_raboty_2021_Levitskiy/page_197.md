---
source_image: page_197.png
page_number: 197
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 23.95
tokens: 6396
characters: 1142
timestamp: 2025-12-24T04:00:31.772008
finish_reason: stop
---

В данном случае если к сети подключится компьютер с MAC-адресом 00:FF:FB:69:DC:E5, ему будет назначен IP-адрес 192.168.1.99, имя узла server и шлюз по умолчанию 192.168.1.1.

Директиву host нужно поместить в одну из директив subnet, к которой при- надлежит выделяемый IP-адрес, например:

subnet 192.168.1.0 netmask 255.255.255.0 {
    option routers 192.168.1.1;
    option subnet-mask 255.255.255.0;
    range 192.168.1.101 192.168.1.200;
}

host server {
    option host-name "server";
    option routers 192.168.1.1;
    hardware ethernet 00:FF:FB:69:DC:E5;
    fixed-address 192.168.1.99;
}

Управлять DHCP-сервером можно с помощью команды service. Следующие команды позволяют запустить, перезапустить или остановить сервер:

$ sudo systemctl start isc-dhcp-server
$ sudo systemctl enable isc-dhcp-server
$ sudo systemctl enable isc-dhcp-server

или (в старых дистрибутивах):

# service dhcpd start
# service dhcpd restart
# service dhcpd stop

Обратите внимание, как называется сервис DHCP-сервиса. В современных версиях Ubuntu он называется isc-dhcp-server. В старых версиях Ubuntu и других дистрибутивов нужный сервис назывался dhcpd.