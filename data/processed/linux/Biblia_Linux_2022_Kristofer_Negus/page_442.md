---
source_image: page_442.png
page_number: 442
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 27.68
tokens: 7528
characters: 2205
timestamp: 2025-12-24T04:57:51.858417
finish_reason: stop
---

Отключить службу так же просто, как и включить ее с помощью демона SysVinit. Для этого нужно изменить значение on в команде chkconfig на off. В следующем примере показано использование команды chkconfig для отключения службы cups на уровне выполнения 5:

# chkconfig --level 5 cups off
# chkconfig --list cups
cups        0:off  1:off  2:on   3:on   4:on   5:off   6:off
# ls /etc/rc.d/rc5.d/S*cups
ls: cannot access /etc/rc.d/rc5.d/S*cups: No such file or directory

Как и ожидалось, теперь нет символической ссылки, начинающейся с буквы S, для службы cups в каталоге /etc/rc.d/rc5.d. Для демона systemd снова используется команда systemctl. С ее помощью вы можете отключать и включать службы на сервере Linux.

Включение службы с помощью демона systemd

Параметр enable в команде systemctl настраивает запуск служб при загрузке системы (делает службы постоянными). Далее показано, как именно это сделать:

# systemctl status cups.service
cups.service – CUPS Printing Service
    Loaded: loaded (/lib/systemd/system/cups.service; disabled)
    Active: inactive (dead) since Tue, 21 Apr 2020 06:42:38 ...
    Main PID: 17172 (code=exited, status=0/SUCCESS)
    CGroup: name=systemd:/system/cups.service
# systemctl enable cups.service
Created symlink /etc/systemd/system/printer.target.wants/cups.service → /usr/lib/systemd/system/cups.service.
Created symlink /etc/systemd/system/sockets.target.wants/cups.socket → /usr/lib/systemd/system/cups.socket.
Created symlink /etc/systemd/system/multi-user.target.wants/cups.path → /usr/lib/systemd/system/cups.path.
# systemctl status cups.service
cups.service – CUPS Printing Service
    Loaded: loaded (/lib/systemd/system/cups.service; enabled)
    Active: inactive (dead) since Tue, 21 Apr 2020 06:42:38...
    Main PID: 17172 (code=exited, status=0/SUCCESS)
    CGroup: name=systemd:/system/cups.service

Обратите внимание на то, что статус службы cups.service изменился после использования параметра enable в команде systemctl. Кроме того, отметьте для себя, что параметр enable просто создает несколько символьских ссылок. Может возникнуть искушение создать эти ссылки самостоятельно. Однако предпочтительнее применять для этого именно команду systemctl.