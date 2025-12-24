---
source_image: page_073.png
page_number: 73
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 9.43
tokens: 7462
characters: 1536
timestamp: 2025-12-23T23:04:22.081299
finish_reason: stop
---

Таблица 5.2. Файлы журналов Linux

<table>
  <tr>
    <th>Расположение журнала</th>
    <th>Описание</th>
  </tr>
  <tr>
    <td>/var/log/apache2/</td>
    <td>Журналы доступа и ошибок для веб-сервера Apache</td>
  </tr>
  <tr>
    <td>/var/log/auth.log</td>
    <td>Сведения о входе пользователя в систему, привилегированном доступе и удаленной проверке подлинности</td>
  </tr>
  <tr>
    <td>/var/log/kern.log</td>
    <td>Журналы ядра</td>
  </tr>
  <tr>
    <td>/var/log/messages</td>
    <td>Общая некритическая системная информация</td>
  </tr>
  <tr>
    <td>/var/log/syslog</td>
    <td>Общие системные журналы</td>
  </tr>
</table>

Чтобы получить больше информации о том, где хранятся файлы журналов для данной системы, в большинстве дистрибутивов Linux обратитесь к файлам /etc/syslog.conf или /etc/rsyslog.conf.

Собираем файлы журналов Windows

В среде Windows команду wevtutil можно использовать для сбора лог-файлов и управления ими. К счастью, эта команда вызывается из Git Bash. Сценарий winlogs.sh, показанный в примере 5.2, использует для вывода списка всех доступных журналов параметр el команды wevtutil, а для экспорта каждого журнала в файл — параметр ep1.

Пример 5.2. Сценарий winlogs.sh

#!/bin/bash -
#
# Bash и кибербезопасность
# winlogs.sh
#
# Описание:
# Собираем копии файлов журнала Windows
#
# Использование:
# winlogs.sh [-z]
#   -z Заархивировать вывод
#
TGZ=0
if (( $# > 0 ))
then
    if [[ ${1:0:2} == '-z' ]]
    then
        TGZ=1 # флаг tgz для tar/zip-архивирования лог-файлов
    shift
    fi