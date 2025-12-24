---
source_image: page_438.png
page_number: 438
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 26.12
tokens: 7487
characters: 1884
timestamp: 2025-12-24T04:57:42.246600
finish_reason: stop
---

Starting cups:      [ OK ]
# service cups status
cupsd (pid 8236) is running...

Перезагрузка службы отличается от перезапуска службы. При перезагрузке сама служба не останавливается — снова загружаются только ее файлы конфигурации. В следующем примере показано, как перезагрузить демон cups:

# service cups status
cupsd (pid 8236) is running...
# service cups reload
Reloading cups:      [ OK ]
# service cups status
cupsd (pid 8236) is running...

Если служба SysVinit остановлена в процессе перезагрузки, появится статус FAILED. Это показано в следующем примере:

# service cups status
cupsd is stopped
# service cups reload
Reloading cups: [FAILED]
Stopping and starting systemd services

Для демона systemd команда systemctl позволяет останавливать, запускать, перезагружать и перезапускать службы. Параметры команды systemctl похожи.

Остановка службы с помощью демона systemd

В следующем примере состояние демона cups проверяется, а затем он останавливается с помощью команды systemctl stop cups.service:

# systemctl status cups.service
cups.service – CUPS Printing Service
    Loaded: loaded (/lib/systemd/system/cups.service; enabled)
    Active: active (running) since Mon, 20 Apr 2020 12:36:3...
    Main PID: 1315 (cupsd)
    CGroup: name=systemd:/system/cups.service
        1315 /usr/sbin/cupsd -f
# systemctl stop cups.service
# systemctl status cups.service
cups.service – CUPS Printing Service
    Loaded: loaded (/lib/systemd/system/cups.service; enabled)
    Active: inactive (dead) since Tue, 21 Apr 2020 04:43:4...
    Process: 1315 ExecStart=/usr/sbin/cupsd -f
    (code=exited, status=0/SUCCESS)
    CGroup: name=systemd:/system/cups.service

Обратите внимание на то, что при проверке статуса после остановки демона cups видно, что служба неактивна (dead), но все еще считается включенной. Это означает, что демон cups будет запускаться при загрузке сервера.