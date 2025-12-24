---
source_image: page_282.png
page_number: 282
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 6.03
tokens: 7300
characters: 1170
timestamp: 2025-12-23T23:12:19.190524
finish_reason: stop
---

Для использования сценария checkemail.sh передайте в качестве аргумента адрес электронной почты или введите его при появлении запроса:

$ ./checkemail.sh example@example.com

Account pwned in the following breaches:
000webhost
AbuseWithUs
Adobe
Apollo
.
.
.

Рассмотрим два других варианта этого сценария. Первый показан в примере 22.3.

Пример 22.3. checkemailAlt.sh

#!/bin/bash
#
# checkemail.sh – проверяем, имеется ли адрес электронной почты
#                в базе данных сайта Have I Been Pwned?
#

if (( $# == 0 ))    ①
then
    printf 'Enter email address: '
    read emailin
else
    emailin="$1"
fi

URL="https://haveibeenpwned.com/api/v2/breachedaccount/$emailin"
pwned=$(curl -s "$URL" | grep -Po '"Name":".*?"' )   ②

if [ "$pwned" == "" ]
then
    exit 1
else
    echo 'Account pwned in the following breaches:'  ③
    pwned="${pwned//\"/}"      # удалить все кавычки
    pwned="${pwned//Name:/} "  # удалить все 'Name:'
    echo "${pwned}"
    exit 0
fi

① Как и в предыдущем сценарии, чтобы определить, предоставил ли пользователь нужное количество аргументов, используйте счетчик аргументов. Если аргументов недостаточно, направьте пользователю запрос.