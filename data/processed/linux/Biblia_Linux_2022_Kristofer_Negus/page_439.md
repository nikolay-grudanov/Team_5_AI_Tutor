---
source_image: page_439.png
page_number: 439
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 28.75
tokens: 7575
characters: 2115
timestamp: 2025-12-24T04:57:46.770217
finish_reason: stop
---

Запуск службы с помощью демона systemd

Запустить демон cups так же просто, как и остановить его. В следующем примере это показано:

# systemctl start cups.service
# systemctl status cups.service
cups.service – CUPS Printing Service
    Loaded: loaded (/lib/systemd/system/cups.service; enabled)
    Active: active (running) since Tue, 21 Apr 2020 04:43:5...
    Main PID: 17003 (cupsd)
    CGroup: name=systemd:/system/cups.service
        └ 17003 /usr/sbin/cupsd -f

После запуска демона cups использование команды systemctl с параметром status говорит о том, что служба активна (запущена), кроме того, показан ее номер идентификатора процесса (PID) — 17003.

Перезапуск службы с помощью демона systemd

Перезапуск службы означает, что служба останавливается, а затем запускается снова. Если в данный момент она не запущена, перезапуск просто запустит ее:

# systemctl restart cups.service
# systemctl status cups.service
cups.service – CUPS Printing Service
    Loaded: loaded (/lib/systemd/system/cups.service; enabled)
    Active: active (running) since Tue, 21 Apr 2020 04:45:2...
    Main PID: 17015 (cupsd)
    CGroup: name=systemd:/system/cups.service
        └ 17015 /usr/sbin/cupsd -f

Вы также можете выполнить условный перезапуск службы с помощью команды systemctl. Условный перезапуск перезапускает службу только в том случае, если она в данный момент запущена. Любая служба в неактивном состоянии не запускается:

# systemctl status cups.service
cups.service – CUPS Printing Service
    Loaded: loaded (/lib/systemd/system/cups.service; enabled)
    Active: inactive (dead) since Tue, 21 Apr 2020 06:03:32...
    Process: 17108 ExecStart=/usr/sbin/cupsd -f
    (code=exited, status=0/SUCCESS)
    CGroup: name=systemd:/system/cups.service
# systemctl condrestart cups.service
# systemctl status cups.service
cups.service – CUPS Printing Service
    Loaded: loaded (/lib/systemd/system/cups.service; enabled)
    Active: inactive (dead) since Tue, 21 Apr 2020 06:03:32...
    Process: 17108 ExecStart=/usr/sbin/cupsd -f
    (code=exited, status=0/SUCCESS)
    CGroup: name=systemd:/system/cups.service