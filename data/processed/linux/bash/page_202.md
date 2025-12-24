---
source_image: page_202.png
page_number: 202
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 8.41
tokens: 7350
characters: 1278
timestamp: 2025-12-23T23:09:28.070282
finish_reason: stop
---

Команда telnet доступна в большинстве версий Linux, но в Git Bash и во многих версиях Windows она отсутствует. В этих случаях, чтобы получить аналог команды telnet, вы можете написать небольшой сценарий, используя дескриптор bash /dev/tcp.

В примере 13.1 показано, как для подключения к SMTP-серверу и захвата баннера использовать файловый дескриптор bash TCP.

Пример 13.1. smtpconnect.sh

#!/bin/bash -
#
# Bash и кибербезопасность
# smtpconnect.sh
#
# Описание:
# Подключение к SMTP-серверу и печать приветственного баннера
#
# Использование:
# smtpconnect.sh <host>
#   <host> SMTP-сервер для соединения

exec 3<>/dev/tcp/"$1"/25
echo -e 'quit\r\n' >&3
cat <&3

При запуске этого сценария мы получим следующий вывод:

$ ./smtpconnect.sh 192.168.0.16

220 localhost.localdomain ESMTP Postfix (Ubuntu)

В примере 13.2 показано, как это все объединить для автоматического извлечения баннеров с серверов FTP, SMTP и HTTP.

Пример 13.2. bannergrabber.sh

#!/bin/bash -
#
# Bash и кибербезопасность
# bannergrabber.sh
#
# Описание:
# Автоматическое извлечение баннеров с HTTP-, SMTP- и FTP-серверов
#
# Использование: ./bannergrabber.sh hostname [scratchfile]
#   scratchfile используется во время обработки, но удаляется;
#   по умолчанию: "scratch.file" или сгенерированное имя