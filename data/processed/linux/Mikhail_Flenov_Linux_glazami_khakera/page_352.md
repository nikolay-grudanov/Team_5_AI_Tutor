---
source_image: page_352.png
page_number: 352
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 21.69
tokens: 7689
characters: 1621
timestamp: 2025-12-24T04:28:41.804150
finish_reason: stop
---

Мониторинг системы

строки журналов находятся в файле /etc/syslog.conf. Пример содержимого файла можно увидеть в листинге 12.3.

Листинг 12.3. Файл конфигурации программы syslogd

# Log all kernel messages to the console.
# Logging much else clutters up the screen.
# Выводить все сообщения ядра на экран.
# Вывод других сообщений создаст на экране беспорядок.
#kern.*                /dev/console

# Log anything (except mail) of level info or higher.
# Don't log private authentication messages!
# Протоколировать в указанный файл все сообщения уровня info и выше.
# Исключения составляют письма, сообщения аутентификации и демона cron.
*.info;mail.none;authpriv.none;cron.none    /var/log/messages

# The authpriv file has restricted access.
# Файл authpriv содержит ограниченный доступ.
authpriv.*                /var/log/secure

# Log all the mail messages in one place.
# Сохранять все события почтовой системы в указанное место.
mail.*                    /var/log/maillog

# Log cron stuff.
# Протоколировать сообщения cron.
cron.*                    /var/log/cron

# Everybody gets emergency messages.
# Все получают критические сообщения.
*.emerg                   *

# Save news errors of level crit and higher in a special file.
# Сохранять сообщения новостей уровня crit (критический) и выше
# в специальный файл.
uucp,news.crit            /var/log/spooler

# Save boot messages also to boot.log.
# Сохранять сообщения, происходящие во время загрузки в указанный файл.
local7.*                  /var/log/boot.log

Назначение директив легко можно проследить по комментариям. Все они имеют вид:

название.уровень