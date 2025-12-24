---
source_image: page_238.png
page_number: 238
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 19.15
tokens: 6345
characters: 1174
timestamp: 2025-12-24T04:01:23.168908
finish_reason: stop
---

Если выполнено более 3 неудачных попыток подключения к серверу через основные порты SSH, то IP-адрес, с которого выполнялась авторизация, попадет в бан на 10 минут (600 секунд). Правило запрета будет добавлено в iptables. В то же время владелец сервера получит уведомление на e-mail, указанный в значении переменной dest, о том, что указанный IP был заблокирован за попытку получения несанкционированного доступа по протоколу SSH. Также в сообщении будет указана WHOIS информация о заблокированном IP.

Для защиты от DDoS-атаки на SSH можно создать секцию:

[ssh-ddos]
enabled = true
port    = ssh
filter  = sshd-ddos
logpath = /var/log/auth.log
maxretry = 2

Ниже представлены примеры настроек конфигурационного файла для защиты почтового сервера postfix.

[postfix]
enabled = true
port    = smtp,ssmtp,submission
action  = iptables[name=Postfix-smtp, port=smtp, protocol=tcp]
filter  = postfix
logpath = /var/log/mail.log
bantime = 86400
maxretry = 3
findtime = 3600
ignoreip = 127.0.0.1

Для защиты веб-сервера Apache можно использовать следующие настройки Fail2ban:

[apache]
enabled = true
port    = http,https
filter  = apache-auth
logpath = /var/log/apache2/error.log