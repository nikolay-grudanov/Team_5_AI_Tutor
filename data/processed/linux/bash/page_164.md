---
source_image: page_164.png
page_number: 164
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 9.27
tokens: 7329
characters: 1259
timestamp: 2025-12-23T23:08:01.595556
finish_reason: stop
---

# что мы имеем: создано два файла sha1sum
declare -A BYPATH BYHASH INUSE    # ассоциативные массивы

# в качестве базового загрузите первый файл
while read HNUM FN
do
    BYPATH["$FN"]=$HNUM
    BYHASH[$HNUM]="$FN"
    INUSE["$FN"]="X"
done < "$BASE"

# ------ теперь начинаем вывод
# смотрим, есть ли каждое имя файла, указанное во втором файле,
# по такому же месторасположению (пути), что и в первом (базовом файле)

printf '<filesystem host="%s" dir="%s">\n' "$HOSTNAME" "${DIR[*]}"

while read HNUM FN
do
    WASHASH="${BYPATH[${FN}]}"
    # нашел ли он его? если нет, то это будет null
    if [[ -z $WASHASH ]]
    then
        ALTFN="${BYHASH[$HNUM]}"
        if [[ -z $ALTFN ]]
        then
            printf ' <new>%s</new>\n' "$FN"
        else
            printf ' <relocated orig="%s">%s</relocated>\n' "$ALTFN" "$FN"
            INUSE["$ALTFN"]='_'
        fi
    else
        INUSE["$FN"]='_'
        if [[ $HNUM == $WASHASH ]]
        then
            continue; # ничего не изменилось;
        else
            printf ' <changed>%s</changed>\n' "$FN"
        fi
    fi
done < "$B2ND"

for FN in "${!INUSE[@]}"
do
    if [[ "${INUSE[$FN]}" == 'X' ]]
    then
        printf ' <removed>%s</removed>\n' "$FN"
    fi
done

printf '</filesystem>\n'