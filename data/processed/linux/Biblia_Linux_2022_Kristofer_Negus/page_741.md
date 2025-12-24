---
source_image: page_741.png
page_number: 741
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 17.74
tokens: 7294
characters: 1232
timestamp: 2025-12-24T05:05:55.167497
finish_reason: stop
---

Служба firewalld

Служба firewalld уже может быть установлена в вашей системе Linux. Чтобы проверить это, введите следующее:

# systemctl status firewalld
• firewalld.service – firewalld – dynamic firewall daemon
    Loaded: loaded (/usr/lib/systemd/system/firewalld.service; ena>
    Active: active (running) since Sat 2019-10-19 11:43:13 EDT; 5m>
    Docs: man:firewalld(1)
Main PID: 776 (firewalld)
    Tasks: 2 (limit: 2294)
Memory: 39.6M
CGroup: /system.slice/firewalld.service
    └─776 /usr/bin/python3 /usr/sbin/firewalld --nofork -->

Если это не так, вы можете установить службу firewalld и связанный с ней графический интерфейс пользователя, а затем запустить ее следующим образом:

# yum install firewalld firewall-config
# systemctl start firewalld.service
# systemctl enable firewalld.service

Для управления службой firewalld запустите окно Firewall Configuration (Настройка межсетевого экрана). Для этого введите следующую команду:

# firewall-config &

На рис. 25.1 показан пример окна Firewall Configuration (Настройка межсетевого экрана).

![Окно Firewall Configuration (Настройка межсетевого экрана)](https://example.com/firewall_config.png)

Рис. 25.1. Окно Firewall Configuration (Настройка межсетевого экрана)