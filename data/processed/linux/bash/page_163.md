---
source_image: page_163.png
page_number: 163
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 6.16
tokens: 7209
characters: 907
timestamp: 2025-12-23T23:07:56.097380
finish_reason: stop
---

find "${DIR[@]}" -type f | xargs -d '\n' sha1sum
}
function parseArgs ()
{
    while getopts "d:" MYOPT
        do
            # не проверяется MYOPT, так как существует только один вариант
            DIR+=("$OPTARG")
        done
    shift $((OPTIND-1))

    # нет аргументов? слишком много?
    (( $# == 0 || $# > 2 )) && usageErr

    (( $#{#DIR[*]} == 0 )) && DIR=( "/")
}
declare -a DIR

# создайте базовый файл (предоставляется только одно имя файла)
# либо сделайте вторичные краткие выводы (при наличии двух имен файлов)

parseArgs
BASE="$1"
B2ND="$2"

if (( $# == 1 )) # только один аргумент
then
    # создание "$BASE"
    dosumming > "$BASE"
    # все сделано для базового файла
    exit
fi

if [[ ! -r "$BASE" ]]
then
    usageErr
fi

# если второй файл существует, сравнить оба файла
# иначе создать/заполнить его
if [[ ! -e "$B2ND" ]]
then
    echo creating "$B2ND"
    dosumming > "$B2ND"
fi