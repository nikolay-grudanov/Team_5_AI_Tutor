---
source_image: page_279.png
page_number: 279
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 8.24
tokens: 7368
characters: 1399
timestamp: 2025-12-23T23:12:13.119055
finish_reason: stop
---

# базе данных сайта Have I Been Pwned?
#
# Использование: ./checkpass.sh [<password>]
# <password> Пароль для проверки
# по умолчанию: читать из stdin

if (( "$#" == 0 ))
then
    printf 'Enter your password: '
    read -s passin
    echo
else
    passin="$1"
fi

passin=$(echo -n "$passin" | sha1sum)
passin=${passin:0:40}

firstFive=${passin:0:5}
ending=${passin:5}

pwned=$(curl -s "https://api.pwnedpasswords.com/range/$firstFive" | \
        tr -d '\r' | grep -i "$ending")
passwordFound=${pwned##*:}

if [ "$passwordFound" == "" ]
then
    exit 1
else
    printf 'Password is Pwned %d Times!\n' "$passwordFound"
    exit 0
fi

① Здесь проверяется, был ли пароль передан в качестве аргумента. Если нет, пользователю будет предложено ввести пароль.

② Чтобы не показывать вводимые пользователем данные, для команды read задан параметр -s. Это рекомендуется делать при запросе паролей или другой конфиденциальной информации. При использовании параметра -s при нажатии клавиши Enter новая строка не появится. Поэтому после оператора read мы добавляем пустой оператор echo.

③ Здесь введенный пароль преобразуется в хеш SHA-1. В следующей строке используется операция подстроки bash для извлечения первых 40 символов, удаляя любые дополнительные символы, которые sha1sum могла включить в свой вывод.

④ Первые пять символов хеша хранятся в переменной firstFive, а символы с 6-го по 40-й — в ending.