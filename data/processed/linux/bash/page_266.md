---
source_image: page_266.png
page_number: 266
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 8.28
tokens: 7344
characters: 1350
timestamp: 2025-12-23T23:11:47.026864
finish_reason: stop
---

Реализация

Для определения операционной системы мы могли бы использовать сценарий, показанный в примере 2.3. Но, кроме типа операционной системы, при работе в Linux нам необходимо определить дистрибутив Linux. Некоторые из этих дистрибутивов основаны на Debian и используют его систему управления пакетами. Другие предусматривают иной подход с соответствующим набором инструментов. Мы просто посмотрим, существует ли в нашей системе определенный исполняемый файл, и если это так, выведем соответствующий тип операционной системы (пример 20.1).

Пример 20.1. softinv.sh

#!/bin/bash -
#
# Bash и кибербезопасность
# softinv.sh
#
# Описание:
# Перечисление установленного в системе программного обеспечения
# для последующего агрегирования и анализа
#
# Использование: ./softinv.sh [filename]
# вывод записывается в $1 или <hostname>_softinv.txt
#

# задаем имя файла вывода
OUTFN="${1:-${HOSTNAME}_softinv.txt}"

# какая команда будет запущена, зависит от типа и дистрибутива ОС
OSbase=win
type -t rpm &> /dev/null
(( $? == 0 )) && OSbase=rpm
type -t dpkg &> /dev/null
(( $? == 0 )) && OSbase=deb
type -t apt &> /dev/null
(( $? == 0 )) && OSbase=apt

case ${OSbase} in
    win)
        INVCMMD="wmic product get name,version //format:csv"
        ;;
    rpm)
        INVCMMD="rpm -qa"
        ;;
    deb)
        INVCMMD="dpkg -l"
        ;;
    apt)