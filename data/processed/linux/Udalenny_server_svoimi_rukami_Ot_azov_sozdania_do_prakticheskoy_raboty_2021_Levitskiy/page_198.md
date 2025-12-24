---
source_image: page_198.png
page_number: 198
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 14.52
tokens: 6225
characters: 879
timestamp: 2025-12-24T04:00:26.218846
finish_reason: stop
---

11.6. Настройка DHCP-клиента в Ubuntu

В Ubuntu 16.04 вы можете настроить интерфейс в файле конфигурации /etc/network/interfaces.

$ sudo nano /etc/network/interfaces

Добавьте эти строчки:

auto eth0
iface eth0 inet dhcp

Сохраните файл и перезапустите сетевой сервис (или перезагрузите систему).

$ sudo systemctl restart networking

В Ubuntu 18.04 и более новых сетевое управление контролируется программой Netplan. Вам нужно отредактировать соответствующий файл, например, в каталоге /etc/netplan/

$ sudo vim /etc/netplan/01-netcfg.yaml

Затем включите dhcp4 под конкретным интерфейсом, например, под ethernet, ens0, и закомментируйте статические настройки, связанные с IP:

network:
    version: 2
    renderer: networkd
    ethernets:
        ens0:
            dhcp4: yes

Сохраните изменения и выполните следующую команду, чтобы применить изменения:

$ sudo netplan apply