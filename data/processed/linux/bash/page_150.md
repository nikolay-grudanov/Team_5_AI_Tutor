---
source_image: page_150.png
page_number: 150
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 6.87
tokens: 7290
characters: 1141
timestamp: 2025-12-23T23:07:23.461452
finish_reason: stop
---

# fd2.sh
#
# Описание:
# Сравнивает два результата сканирования портов для поиска изменений
# Основное предположение: оба файла имеют одинаковое количество строк,
# каждая строка с тем же адресом хоста,
# хотя перечисленные порты могут быть разными
#
# Использование: ./fd2.sh <file1> <file2>
#

# найти "$LOOKFOR" в списке аргументов для этой функции
# возвращает true (0), если его нет в списке
function NotInList ()
{
    for port in "$@"
    do
        if [[ $port == $LOOKFOR ]]
        then
            return 1
        fi
    done
    return 0
}

while true
do
    read aline <&4 || break      # EOF
    read bline <&5 || break      # EOF, для симметрии

    # if [[ $aline == $bline ]]; then continue; fi
    [[ $aline == $bline ]] && continue;

    # есть разница, поэтому мы
    # подразделяем на хост и порты
    HOSTA=${aline%% *}
    PORTSA=( ${aline#* } )

    HOSTB=${bline%% *}
    PORTSB=( ${bline#* } )

    echo $HOSTA      # определяем хост, в котором произошли изменения

    for porta in ${PORTSA[@]}
    do
        LOOKFOR=$porta NotInList ${PORTSB[@]} && echo " closed: $porta"
    done

    for portb in ${PORTSB[@]}