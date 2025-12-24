---
source_image: page_219.png
page_number: 219
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 5.73
tokens: 7274
characters: 1036
timestamp: 2025-12-23T23:10:02.292414
finish_reason: stop
---

Сценарий, приведенный в примере 14.7, считывает указанный файл, а затем с помощью метода XOR и ключа, предоставленного пользователем, шифрует или расшифровывает его.

Пример 14.7. streamcipher.sh

#!/bin/bash -
#
# Bash и кибербезопасность
# streamcipher.sh
#
# Описание:
# Облегченная реализация потокового шифра
# Это учебный пример, который не рекомендуется для практического применения
#
# Использование:
# streamcipher.sh [-d] <key> < inputfile
#   -d Режим дешифрования
#   <key> Числовой ключ
#

source ./askey.sh

#
# Ncrypt – шифрование — считывание символов
#     на выходе двухзначный шестнадцатеричный #s
#
function Ncrypt ()
{
    TXT="$1"
    for((i=0; i< ${#TXT}; i++))
    do
        CHAR="${TXT:i:1}"
        RAW=$(asnum "$CHAR")  # " " требуется для пробелов (32)
        NUM=${RANDOM}
        COD=$(( RAW ^ ( NUM & 0x7F ) ))
        printf "%02X" "$COD"
    done
    echo
}

#
# Dcrypt - дешифрование — считывание двухзначного шестнадцатеричного #s
#     на выходе символы (буквенные и цифровые)
#

function Dcrypt ()