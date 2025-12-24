---
source_image: page_429.png
page_number: 429
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 22.06
tokens: 7391
characters: 1660
timestamp: 2025-12-24T04:57:21.215771
finish_reason: stop
---

sockets.target      static
sound.target        static
swap.target         static
sysinit.target      static
syslog.target       static
time-sync.target    static
umount.target       static
43 unit files listed.

Обратите внимание на то, что в обоих примерах файлов конфигурации юнитов сами юниты отображаются со значением статуса static, enabled или disabled. Статус enabled означает, что юнит в данный момент включен. Статус disabled означает, что юнит в данный момент отключен. Тут все просто. А со статусом static может возникнуть недопонимание. Он говорит о том, что юнит «статически включен», то есть включен по умолчанию и не может быть отключен даже суперпользователем.

Файлы конфигурации сервисного юнита содержат множество информации, например, какие дополнительные службы должны быть запущены и когда какой файл среды использовать и т. д. В следующем примере показан файл конфигурации юнита демона sshd:

# cat /lib/systemd/system/sshd.service
[Unit]
Description=OpenSSH server daemon
Documentation=man:sshd(8) man:sshd_config(5)
After=network.target sshd-keygen.target

[Service]
Type=notify
EnvironmentFile=-/etc/crypto-policies/back-ends/opensshserver.config
EnvironmentFile=-/etc/sysconfig/sshd
ExecStart=/usr/sbin/sshd -D $OPTIONS $CRYPTO_POLICY
ExecReload=/bin/kill -HUP $MAINPID
KillMode=process
Restart=on-failure
RestartSec=42s

[Install]
WantedBy=multi-user.target

[Install]
WantedBy=multi-user.target

Этот базовый файл конфигурации сервисного юнита обладает следующими параметрами.

● Description — описание службы в свободной форме (строка комментария).
● Documentation — список справочных страниц для демона sshd и файла конфигурации.