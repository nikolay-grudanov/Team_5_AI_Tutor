---
source_image: page_281.png
page_number: 281
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 8.43
tokens: 7389
characters: 1459
timestamp: 2025-12-23T23:12:18.801792
finish_reason: stop
---

Проверяемый адрес электронной почты добавляется в конец URL-адреса. API вернет список нарушений, с которыми был связан данный адрес электронной почты. Список будет получен в формате JSON. В этот список будет включен большой объем информации: название нарушения, связанный домен и описание. Если электронный адрес в базе данных не найден, будет возвращен код состояния HTTP 404.

В примере 22.2 показано, как автоматизировать этот процесс.

Пример 22.2. checkemail.sh

#!/bin/bash -
#
# Bash и кибербезопасность
# checkemail.sh
#
# Описание:
# Проверка адреса электронной почты на соответствие
# базе данных сайта Have I Been Pwned?
#
# Использование: ./checkemail.sh [<email>]
# <email> E-mail для проверки; по умолчанию: читать из stdin

if (( "$#" == 0 ))    ①
then
    printf 'Enter email address: '
    read emailin
else
    emailin="$1"
fi

pwned=$(curl -s "https://haveibeenpwned.com/api/v2/breachedaccount/$emailin")  ②

if [ "$pwned" == "" ]
then
    exit 1
else
    echo 'Account pwned in the following breaches:'
    echo "$pwned" | grep -Po '"Name":".*?"' | cut -d':' -f2 | tr -d '"'  ③
    exit 0
fi

① Здесь выполняется проверка, был ли адрес электронной почты передан в качестве аргумента; если нет, пользователю будет направлен запрос.

② Запрос на веб-сайт Have I Been Pwned?.

③ Если ответ был возвращен, выполните простой синтаксический анализ JSON и извлеките пару «имя/значение». Дополнительную информацию об обработке JSON см. в главе 11.