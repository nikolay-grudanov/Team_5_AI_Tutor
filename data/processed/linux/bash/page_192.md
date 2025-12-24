---
source_image: page_192.png
page_number: 192
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 7.24
tokens: 7330
characters: 1182
timestamp: 2025-12-23T23:09:03.832825
finish_reason: stop
---

# Заголовок
# -------------
# Однострочный вывод
# -------------
# Вывод из пяти строк
# ...
# -------------
# Метки столбцов, а затем
# восемь строк гистограммы
# ...
# -------------

# некоторые важные постоянные строки
UPTOP=$(tput cup 0 0)
ERAS2EOL=$(tput el)
REV=$(tput rev)        # негативное изображение
OFF=$(tput sgr0)       # общий сброс
SMUL=$(tput smul)      # режим подчеркивания включен (пуск)
RMUL=$(tput rmul)      # режим подчеркивания выключен (сброс)
COLUMNS=$(tput cols)   # ширина нашего окна
# DASHES(ТИРЕ)=------------------------------
printf -v DASHES '%*s' $COLUMNS '-'
DASHES=${DASHES// /-}

#
# prSection – напечатать фрагмент экрана
#    напечатать $1-many строк из stdin
#    каждая строка представляет собой полную строку текста
#    с последующим стиранием до конца строки
#    разделы заканчиваются штриховой линией
#
function prSection ()
{
    local -i i
    for((i=0; i < ${1:-5}; i++))
    do
        read aline
        printf '%s%s\n' "$aline" "${ERAS2EOL}"
    done
    printf '%s%s\n%s' "$DASHES" "${ERAS2EOL}" "${ERAS2EOL}"
}

function cleanup()
{
    if [[ -n $BGPID ]]
    then
        kill %1
        rm -f $TMPFILE
    fi
} &> /dev/null