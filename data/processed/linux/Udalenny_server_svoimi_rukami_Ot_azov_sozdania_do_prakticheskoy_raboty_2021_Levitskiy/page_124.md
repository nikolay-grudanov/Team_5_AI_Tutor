---
source_image: page_124.png
page_number: 124
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 14.41
tokens: 6307
characters: 858
timestamp: 2025-12-24T03:58:47.576350
finish_reason: stop
---

Листинг 6.2. Файл /etc/network/interfaces

# Локальный интерфейс lo
auto lo
iface lo inet loopback

# Внешняя сеть
auto eth0
iface eth0 inet static
address 88.99.88.99
netmask 255.255.255.0
network 88.99.88.99
dns-nameservers 8.8.8.8

# Внутренняя сеть
auto eth1
iface eth1 inet static
address 192.168.1.1
netmask 255.255.255.0
network 192.168.1.0
broadcast 192.168.1.255

Перезапустим сеть:

# service networking restart

Теперь создайте каталог /etc/firewall и поместите туда файл firewall.sh, который будет содержать команды, превращающий наш обычный компьютер в шлюз:

# touch /etc/firewall/firewall.sh
# chmod +x /etc/firewall/firewall.sh
# nano /etc/firewall/firewall.sh

Код файла firewall.sh приведен в листинге 6.3.

Листинг 6.3. Файл firewall.sh

#!/bin/bash

# Определяем некоторые переменные, чтобы облегчить редактирование конфигурации в будущем