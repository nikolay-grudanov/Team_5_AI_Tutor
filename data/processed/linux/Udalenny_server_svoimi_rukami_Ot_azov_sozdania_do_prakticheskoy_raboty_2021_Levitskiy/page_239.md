---
source_image: page_239.png
page_number: 239
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 15.79
tokens: 6326
characters: 1168
timestamp: 2025-12-24T04:01:19.800247
finish_reason: stop
---

maxretry = 3

[apache-multiport]
enabled = true
port    = http,https
filter  = apache-auth
logpath = /var/log/apache2/error.log
maxretry = 3

[apache-noscript]
enabled = true
port    = http,https
filter  = apache-noscript
logpath = /var/log/apache2/error.log
maxretry = 3

Как вы уже могли заметить, в используемых выше секциях конфигурации отсутствуют значения параметра action. В этом случае при обнаружении атаки на сервис Apache программа Fail2ban будет выполнять действие, определенное в секции [DEFAULT], а именно action = iptables-multiport. Это значит, что атакующий IP-адрес будет заблокирован в iptables при помощи так называемого модуля multiports. Модуль multiports позволяет настроить правило сразу для диапазонов портов.

Для защиты FTP-сервера vsftpd с помощью Fail2ban можно использовать следующие параметры:

[vsftpd]
enabled = true
port    = ftp,ftp-data,ftps,ftps-data
filter  = vsftpd
logpath = /var/log/vsftpd.log
action = iptables[name=VSFTPD, port=21, protocol=tcp]
bantime = 600
maxretry = 3
findtime = 1800

Не забудьте о необходимости перезапуска Fail2ban после каждого редактирования конфигурационного файла:

sudo systemctl restart fail2ban