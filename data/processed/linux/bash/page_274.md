---
source_image: page_274.png
page_number: 274
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 7.80
tokens: 7273
characters: 1154
timestamp: 2025-12-23T23:12:02.408340
finish_reason: stop
---

case "$basecmd" in
    file)
        OK=1
        vfile $donot "$args"
        res=$?
        ;;
    hash)
        OK=1
        # разделить аргументы на первое слово и остаток
        vhash "${args%% *}" "${args#* }"    ⑩
        res=$?
        ;;
    reg)
        # Только для Windows!
        OK=1
        vreg $args
        res=$?
        ;;
    user)
        OK=0
        vuser $args
        res=$?
        ;;
    group)
        OK=0
        vgroup $args
        res=$?
        ;;
    *)
        errexit
        ;;
esac

if (( res != OK ))
then
    echo "FAIL: [$ln] $cmd $args"
fi
done

① errexit — удобная вспомогательная функция, предоставляющая пользователю некоторую полезную информацию о правильном использовании сценария, — с последующим завершением работы, если появится значение ошибки. Синтаксис, используемый в сообщении usage, — это типичный *nix-синтаксис: элементы, разделенные вертикальной линией, — варианты; элементы в квадратных скобках являются необязательными.

② Для проверки существования файла используется if-less-оператор f.

④ Это простой способ переключения 1 на 0 или 0 на 1 при условии, что первый аргумент не равен нулю.