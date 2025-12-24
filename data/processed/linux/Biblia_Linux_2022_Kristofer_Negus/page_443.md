---
source_image: page_443.png
page_number: 443
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 29.74
tokens: 7568
characters: 2394
timestamp: 2025-12-24T04:57:54.310302
finish_reason: stop
---

Отключение службы с помощью демона systemd

Вы можете использовать параметр disable в команде systemctl, чтобы предотвратить запуск службы при загрузке. Однако это действие не сразу останавливает службу. Для этого нужен параметр stop, который описан в пункте «Остановка службы с помощью демона systemd». В следующем примере показано, как отключить включенную в данный момент службу:

# systemctl disable cups.service
rm '/etc/systemd/system/printer.target.wants/cups.service'
rm '/etc/systemd/system/sockets.target.wants/cups.socket'
rm '/etc/systemd/system/multi-user.target.wants/cups.path'
# systemctl status cups.service
cups.service – CUPS Printing Service
    Loaded: loaded (/lib/systemd/system/cups.service; disabled )
    Active: active (running) since Tue, 21 Apr 2020 06:06:41...
    Main PID: 17172 (cupsd)
    CGroup: name=systemd:/system/cups.service
        17172 /usr/sbin/cupsd -f

Параметр disable просто удаляет несколько файлов с помощью команды systemctl. Обратите также внимание на то, что в предыдущем примере, хоть служба cups и отключена, демон cups все еще активен (работает) и должен быть остановлен вручную. Некоторые службы нельзя отключить с помощью демона systemd. Таковы статические службы. Рассмотрим пример со службой dbus.service:

# systemctl status dbus.service
dbus.service – D-Bus System Message Bus
    Loaded: loaded (/lib/systemd/system/dbus.service; static)
    Active: active (running) since Mon, 20 Apr 2020 12:35:...
    Main PID: 707 (dbus-daemon)
...
# systemctl disable dbus.service
# systemctl status dbus.service
dbus.service – D-Bus System Message Bus
    Loaded: loaded (/lib/systemd/system/dbus.service; static)
    Active: active (running) since Mon, 20 Apr 2020 12:35:...
    Main PID: 707 (dbus-daemon)
...

Когда команда systemctl disable задействуется для службы dbus.service, ничего не происходит. Помните: значение static означает, что служба включена по умолчанию и не может быть отключена даже суперпользователем. Иногда отключения службы недостаточно, чтобы точно понять, что она не работает. Например, вам нужно, чтобы служба network.service заменила службу NetworkManager.service для запуска сетевых интерфейсов.

Отключение службы NetworkManager не позволит ей запуститься самостоятельно. Но если какая-то другая служба перечислит NetworkManager в качестве зависимости, то при запуске она попытается запустить и NetworkManager.