---
source_image: page_273.png
page_number: 273
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 5.55
tokens: 7158
characters: 731
timestamp: 2025-12-23T23:11:59.289061
finish_reason: stop
---

# проверить хеш файла
function vhash ()
{
    local res=0
    local X=$(sha1sum $2)
    if [[ ${X%% *} == $1 ]]
    then
        res=1
    fi

    return $res
} # vhash

# проверить системный реестр windows
function vreg ()
{
    local res=0
    local keypath=$1
    local value=$2
    local expected=$3
    local REGVAL=$(query $keypath //v $value)

    if [[ $REGVAL == $expected ]]
    then
        res=1
    fi
    return $res
} # vreg

#
# main
#

# выполнить один раз, чтобы использовать в проверке идентификаторов пользователей
UCMD="net user"
type -t net &>/dev/null || UCMD="id"

ln=0
while read cmd args
do
    let ln++

    donot=0
    if [[ ${cmd:0:1} == '!' ]]
    then
        donot=1
        basecmd=${cmd#\!}
    fi