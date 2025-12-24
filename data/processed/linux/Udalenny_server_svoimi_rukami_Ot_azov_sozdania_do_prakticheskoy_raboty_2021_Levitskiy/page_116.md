---
source_image: page_116.png
page_number: 116
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 18.37
tokens: 6339
characters: 1097
timestamp: 2025-12-24T03:58:36.715590
finish_reason: stop
---

# This file describes the network interfaces available on your system
# For more information, see netplan(5).
network:
    version: 2
    renderer: networkd
    ethernets:
        eno1:
            dhcp4: yes

Добывьте следующие строки:

    routes:
        - to: 192.168.44.0/24
          via: 192.168.0.1

Данная конфигурация означает, что маршрут к сети 192.168.44.0/24 (маска 255.255.255.0) будет проходить через маршрутизатор 192.168.0.1. Полная конфигурация будет выглядеть так:

# This file describes the network interfaces available on your system
# For more information, see netplan(5).
network:
    version: 2
    renderer: networkd
    ethernets:
        eno1:
            dhcp4: true
            routes:
                - to: 192.168.44.0/24
                  via: 192.168.0.1

Обратите внимание, что YAML-файл очень требователен к отступам и разметке. Убедитесь, что оператор «routes» находится на расстоянии двух пробелов от имени интерфейса (в нашем случае eno1), к которому вы применяете маршрут.

Сохраните изменения в файле и примените их посредством команды:

sudo netplan apply