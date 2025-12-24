---
source_image: page_375.png
page_number: 375
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 25.57
tokens: 7572
characters: 2269
timestamp: 2025-12-24T04:55:48.556098
finish_reason: stop
---

# Provides UDP syslog reception
# for parameters see http://www.rsyslog.com/doc/imudp.html
#module(load="imudp") # needs to be done just once
#input(type="imudp" port="514")

# Provides TCP syslog reception
# for parameters see http://www.rsyslog.com/doc/imtcp.html
#module(load="imtcp") # needs to be done just once
#input(type="imtcp" port="514")

Строки, начинающиеся с module(load=, загружают соответствующие модули. Перед модулями, которые в данный момент отключены, стоит знак фунта (#).
Модуль imjournal позволяет службе rsyslog получить доступ к журналу systemd. Модуль imuxsock необходим для приема сообщений из локальной системы. (Он не должен быть закомментирован, то есть перед ним должен стоять знак фунта (#).) Модуль imklog собирает сообщения ядра.
Модули, не включенные по умолчанию, включают модуль immark, который позволяет регистрировать сообщения с помощью параметра --MARK-- (используется для указания того, что служба активна). Модули imudp и imtcp и связанные с ними записи номеров портов применяются для того, чтобы служба rsyslog могла принимать сообщения удаленного журнала, и более подробно рассматриваются в пункте «Настройка и использование узла ведения журнала с помощью службы rsyslogd» далее в этом разделе.
Большая часть работы, выполняемой в файле конфигурации /etc/rsyslog.conf, заключается в изменении раздела RULES. Далее приведен пример правил из раздела RULES файла /etc/rsyslog.conf (обратите внимание на то, что в дистрибутиве Ubuntu эта информация хранится в каталоге /etc/rsyslog.d):

#### RULES ####
# Log all kernel messages to the console.

# Logging much else clutters up the screen.

#kern.*				/dev/console
# Log anything (except mail) of level info or higher.
# Don't log private authentication messages!
*.info;mail.none;authpriv.none;cron.none	/var/log/messages
# The authpriv file has restricted access.
authpriv.*
# Log all the mail messages in one place.
mail.*
# Log cron stuff
cron.* /var/log/cron

Записи с правилами делятся на две колонки. В левой приведена информация о том, какие сообщения совпадают, в правой показано, куда (имя каталога) переходят совпадающие сообщения. Сообщения сопоставляются на основе функции (mail, cron, kern и т. д.) и приоритета (начиная с debug, info, notice вплоть до crit, alert