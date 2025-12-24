---
source_image: page_469.png
page_number: 469
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 29.57
tokens: 7556
characters: 1988
timestamp: 2025-12-24T04:58:37.052086
finish_reason: stop
---

Запуск сервера CUPS

Для систем Linux, применяющих скрипт запуска в стиле System V (например, более ранние версии дистрибутивов Fedora и RHEL), запуск и выключение службы печати CUPS довольно просты. Используйте команду chkconfig, чтобы служба запускалась при каждой перезагрузке. Введите скрипт cups, чтобы служба CUPS запустилась автоматически. В дистрибутиве RHEL 6.x или более ранней версии введите от имени суперпользователя следующее:

# chkconfig cups on
# service cups start

Если служба CUPS уже запущена, возьмите параметр restart вместо start. Параметр restart — это хороший способ прочитать все параметры конфигурации, измененные в файле cupsd.conf (хотя, если служба CUPS уже запущена, команда service cups reload перечитывает файлы конфигурации без перезапуска).

В дистрибутивах Fedora 30 и RHEL 8 для запуска и остановки служб вместо service используется команда systemctl:

# systemctl status cups.service

* cups.service – CUPS Printing Service
Loaded: loaded (/usr/lib/systemd/system/cups.service; enabled)
Active: active (running) since Sat 2016-07-23 22:41:05 EDT; 18h ago
Main PID: 20483 (cupsd)
Status: "Scheduler is running..."
CGroup: /system.slice/cups.service
├─20483 /usr/sbin/cupsd -f

В примере видно, что служба CUPS запущена, так как статус показывает, что демон cupsd активен с идентификатором PID 20483. Запустить службу CUPS можно следующим образом (если она не запущена):

# systemctl start cups.service

Дополнительную информацию о командах systemctl и service для работы со службами см. в главе 15 «Запуск и остановка служб».

Настройка принтера CUPS вручную

Если в вашем дистрибутиве Linux нет графических средств настройки CUPS, можете редактировать файлы конфигурации напрямую. Так, добавленный в окне Print Settings (Настройки принтера) принтер определяется в файле /etc/cups/printers.conf. Вот как выглядит запись о принтере:

<DefaultPrinter printer>
Info HP LaserJet 2100M
Location HP LaserJet 2100M in hall closet
DeviceURI parallel:/dev/lp0