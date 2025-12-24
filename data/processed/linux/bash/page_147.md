---
source_image: page_147.png
page_number: 147
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 8.25
tokens: 7335
characters: 1191
timestamp: 2025-12-23T23:07:21.199096
finish_reason: stop
---

к ряду портов на хостах, упоминаемых в файле. В случае успешного подключения станет понятно, что порт открыт. Если время соединения истекло или вы получили сообщение о сбросе, значит, порт закрыт. Для этого проекта мы на каждом хосте отсканируем TCP-порты с номерами от 1 до 1023 (пример 9.1).

Пример 9.1. scan.sh

#!/bin/bash -
#
# Bash и кибербезопасность
# scan.sh
#
# Описание:
# Сканирование порта указанного хоста
#
# Использование: ./scan.sh <output file>
#   <output file> Файл, куда сохраняются результаты
#

function scan ()
{
    host=$1
    printf '%s' "$host"
    for ((port=1;port<1024;port++))
    do
        # порядок перенаправления важен по двум причинам
        echo >/dev/null 2>&1 < /dev/tcp/${host}/${port}
        if (($? == 0)) ; then printf ' %d' "${port}" ; fi
    done
    echo # или вывести '\n'
}

#
# основной цикл
#   читать имя каждого узла (из stdin)
#   и искать открытые порты
#   сохранить результаты в файл,
#   имя которого указано в качестве аргумента,
#   или задать имя по умолчанию на основе текущей даты
#

printf -v TODAY 'scan_%(%F)T' -1 # например, scan_2017-11-27
OUTFILE=${1:-$TODAY}

while read HOSTNAME
do
    scan $HOSTNAME
done > $OUTFILE