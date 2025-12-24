---
source_image: page_427.png
page_number: 427
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 20.71
tokens: 7374
characters: 1683
timestamp: 2025-12-24T04:57:18.029018
finish_reason: stop
---

units). Хотя основная задача функции systemd заключается в запуске и остановке служб, она может управлять также другими типами объектов, называемых юнитами. Юнит — это группа, состоящая из имени, типа и файла конфигурации и реализующая определенную службу или действие. Существует 12 типов юнитов systemd:

● automount;
● device;
● mount;
● path;
● service;
● snapshot;
● socket;
● target;
● timer;
● wap;
● slice;
● cope.

Два основных юнита systemd, с которыми вы будете иметь дело в ходе работы со службами, — это сервисные и целевые юниты. Сервисные юниты используются для управления демонами на сервере Linux. Целевой юнит — это просто группа других юнитов.

В следующем примере показаны несколько сервисных и целевых юнитов systemd. Имена сервисных юнитов похожи на имена демонов, например cups и sshd. Обратите внимание на то, что каждое имя сервисного юнита заканчивается на .service. Целевые юниты имеют такие имена, как sysinit (sysinit используется для запуска служб при инициализации системы). Имена целевых юнитов заканчиваются на .target:

# systemctl list-units | grep .service
...
cups.service        loaded active running CUPS Printing Service
dbus.service        loaded active running D-Bus Message Bus
...
NetworkManager.service loaded active running Network Manager
prefdm.service      loaded active running Display Manager
remount-rootfs.service loaded active exited Remount Root FS
rsyslog.service     loaded active running System Logging
...
sshd.service        loaded active running OpenSSH server daemon
systemd-logind.service loaded active running Login Service
...
# systemctl list-units | grep .target
basic.target        loaded active active Basic System