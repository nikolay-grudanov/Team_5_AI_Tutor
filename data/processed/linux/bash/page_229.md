---
source_image: page_229.png
page_number: 229
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 7.53
tokens: 7265
characters: 977
timestamp: 2025-12-23T23:10:25.876491
finish_reason: stop
---

# Bash и кибербезопасность
# fuzzer.sh
#
# Описание:
# Изменение указанного аргумента программы
#
# Использование:
# bash fuzzer.sh <executable> <arg1> [?] <arg3> ...
# <executable> Целевая исполняемая программа/скрипт
# <argn> Статические аргументы для исполняемого файла
# '?' Аргумент, который должен быть изменен
# пример: fuzzer.sh ./myprog -t '?' fn1 fn2

#
function usagexit ()
{
    echo "usage: $0 executable args"
    echo "example: $0 myapp -lpt arg \?"
    exit 1
} >&2

if (($# < 2))
then
    usagexit
fi
# приложение, которое мы будем изменять, — это первый аргумент
THEAPP="$1"
shift
# действительно здесь?
type -t "$THEAPP" >/dev/null || usagexit

# какой аргумент нужно изменять?
# найти ? и пометить его позицию
declare -i i
for ((i=0; $# ; i++))
do
    ALIST+=("$1")
    if [[ $1 == '?' ]]
    then
        NDX=$i
    fi
    shift
done

# printf "Executable: %s Arg: %d %s\n" "$THEAPP" $NDX "${ALIST[$NDX]}"

# теперь изменить:
MAX=10000
FUZONE="a"
FUZARG=""