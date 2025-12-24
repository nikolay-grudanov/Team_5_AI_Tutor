---
source_image: page_892.png
page_number: 892
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 19.11
tokens: 7360
characters: 1513
timestamp: 2025-12-24T05:10:04.532777
finish_reason: stop
---

8. Чтобы отобразить состояние демона cups на своем сервере Linux, используйте следующую команду:
а) для SysVinit:

    # service cups status
    cupsd (pid 8236) is running...

б) для systemd:

    # systemctl status cups.service
    cups.service - CUPS Printing Service
    Loaded: loaded (/lib/systemd/system/cups.service; enabled)
    Active: active (running) since Tue, 05 May 2020 04:43:5...
    Main PID: 17003 (cupsd)
    CGroup: name=systemd:/system/cups.service
    17003 /usr/sbin/cupsd -f

9. Чтобы перезапустить демон cups на своем Linux-сервере, выполните следующие действия:
а) для SysVinit:

    # service cups restart
    Stopping cups:      [ OK ]

б) для systemd:

    # systemctl restart cups.service

10. Чтобы перезагрузить демон cups на своем Linux-сервере, выполните следующие действия:
а) для SysVinit:

    # service cups reload
    Reloading cups: [ OK ]

б) а вот для systemd это не так просто. Нельзя перезагрузить демон cups на сервере systemd:

    # systemctl reload cups.service
    Failed to issue method call: Job type reload is not applicable for unit cups.service.

Глава 16. Настройка сервера печати

Для вопросов, связанных с принтерами, в большинстве случаев можно использовать графические средства или инструменты командной строки. В упражнениях важно убедиться, что вы получили те же результаты, какие показаны в ответах далее. Ответы включают в себя сочетание графических и командных способов решения упражнений. (Станьте суперпользователем, когда увидите приглашение #.)