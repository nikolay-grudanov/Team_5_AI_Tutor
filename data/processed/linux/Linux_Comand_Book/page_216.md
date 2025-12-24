---
source_image: page_216.png
page_number: 216
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 20.64
tokens: 5944
characters: 1104
timestamp: 2025-12-24T04:09:12.593736
finish_reason: stop
---

Этот оператор осуществляет выбор между альтернативами, каждая из которых может содержать сложную проверку. Простейшая форма - это оператор if-then.

i f команда    Если статус выхода команды O then
тело
fi    -.■■,-,...
Например:
if [ 'whoami4 = "root" ] then
echo "Вы являетесь суперпользователем" fi
Затем идет оператор if-then-else.
if  команда then
тело! else
тело2 fi
Например:
if [ 4whoami" = "root" ] then
echo " Вы являетесь суперпользователем " else
echo "Вы являетесь обычным пользователем" fi
Наконец, есть формат if-then-el if-else, в котором можно реализовать столько проверок, сколько вам будет нужно.
if  команда! then
тело!
elif  команда2 then
тело2 elif ...
else
TenoN fi
Например:
if [ 'whoami1 = "root" ] then
    echo " Вы являетесь суперпользователем " elif [ "$USER" = "root" ] then
        echo " Вы, должно быть, являетесь суперпользователем "
elif [ "$bribe" -gt 10000 ] then
    echo " Вы можете заплатить за то, чтобы стать суперпользователем " else
    echo "Вы все еще обычный пользователь" fi
Оператор case оценивает одно значение и выполняет соответствующий ему кусок кода.