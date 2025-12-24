---
source_image: page_272.png
page_number: 272
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 5.91
tokens: 7189
characters: 804
timestamp: 2025-12-23T23:11:59.530680
finish_reason: stop
---

function errexit ()
{
    echo "invalid syntax at line $ln"
    echo "usage: [!]file|hash|reg|[!]user|[!]group [args]"
    exit 2

} # errexit

# vfile - проверка наличия имени файла
# аргументы: 1: флаг "нет" - значение:1/0
#           2: имя файла
#
function vfile ()
{
    local isThere=0
    [[ -e $2 ]] && isThere=1
    (( $1 )) && let isThere=1-$isThere

    return $isThere

} # vfile
# проверить идентификатор пользователя
function vuser ()
{
    local isUser
    $UCMD $2 &>/dev/null
    isUser=$?
    if (( $1 ))
    then
        let isUser=1-$isUser
    fi

    return $isUser

} # vuser

# проверить идентификатор группы
function vgroup ()
{
    local isGroup
    id $2 &>/dev/null
    isGroup=$?
    if (( $1 ))
    then
        let isGroup=1-$isGroup
    fi

    return $isGroup

} # vgroup