---
source_image: page_440.png
page_number: 440
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 28.23
tokens: 7550
characters: 2033
timestamp: 2025-12-24T04:57:46.311417
finish_reason: stop
---

Обратите внимание на то, что в примере демон cups находился в неактивном состоянии. При условном перезапуске сообщения об ошибках не генерировались! Демон cups не был запущен, поскольку условные перезапуски влияют лишь на активные службы. Таким образом, всегда полезно проверять состояние службы после остановки, запуска, условного перезапуска и т. д.

Перезагрузка службы с помощью демона systemd

Перезагрузка службы отличается от ее перезапуска. При перезагрузке служба не останавливается, вновь загружаются только ее файлы конфигурации. В следующем примере показано, как перезагрузить демон cups:

# systemctl status sshd.service
sshd.service – OpenSSH server daemon
    Loaded: loaded (/usr/lib/systemd/system/sshd.service; enabled)
    Active: active (running) since Wed 2019-09-18 17:32:27 EDT; 3 days ago
    Main PID: 1675 (sshd)
    CGroup: /system.slice/sshd.service
        └─1675 /usr/sbin/sshd -D

# systemctl reload sshd.service
# systemctl status sshd.service
sshd.service – OpenSSH server daemon
    Loaded: loaded (/lib/systemd/system/sshd.service; enabled)
    Active: active (running) since Wed 2019-09-18 17:32:27 EDT; 3 days ago
    Process: 21770 ExecReload=/bin/kill -HUP $MAINPID (code=exited, status=0/SUCCESS)
    (code=exited, status=0/SUCCESSd)
    Main PID: 1675 (sshd)
    CGroup: /system.slice/sshd.service
        └─1675 /usr/sbin/sshd -D ...

Перезагрузка службы с помощью команды reload вместо перезапуска предотвращает прерывание любых ее отложенных действий. Перезагрузка — это лучший вариант для используемого сервера Linux.

Теперь, когда вы знаете, как останавливать и запускать службы, чтобы устранять неполадки и аварийные ситуации, вы должны научиться включать и отключать их.

Подключение постоянных служб

Параметры stop и start применяются для неотложных задач, а не для постоянных служб. Постоянная служба — это служба, которая запускается во время загрузки сервера или на определенном уровне выполнения. Службы, которые должны быть постоянными, — это обычно новые службы сервера Linux.