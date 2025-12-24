---
source_image: page_078.png
page_number: 78
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 5.47
tokens: 7249
characters: 1045
timestamp: 2025-12-23T23:04:29.289796
finish_reason: stop
---

# bash getlocal.sh < cmds.txt
#   cmds.txt — это файл со списком команд для выполнения

# SepCmds - отделение команд от строки ввода
function SepCmds()
{
    LCMD=${ALINE%%|*}
    REST=${ALINE#*|}
    WCMD=${REST%%|*}
    REST=${REST#*|}
    TAG=${REST%%|*}

    if [[ $OSTYPE == "MSWin" ]]
    then
        CMD="$WCMD"
    else
        CMD="$LCMD"
    fi
}

function DumpInfo ()
{
    printf '<systeminfo host="%s" type="%s"' "$HOSTNAME" "$OSTYPE"
    printf ' date="%s" time="%s">\n' "$(date '+%F')" "$(date '+%T')"
    readarray CMDS
    for ALINE in "${CMDS[@]}"
    do
        # игнорировать комментарии
        if [[ ${ALINE:0:1} == '#' ]]; then continue ; fi

        SepCmds

        if [[ ${CMD:0:3} == N/A ]]
        then
            continue
        else
            printf "<%s>\n" $TAG
            $CMD
            printf "</%s>\n" $TAG
        fi
    done
    printf "</systeminfo>\n"
}

OSTYPE=$(./osdetect.sh)
HOSTNM=$(hostname)
TMPFILE="${HOSTNM}.info"

# собрать в tmp-файл как информацию, так и ошибки
DumpInfo > $TMPFILE 2>&1