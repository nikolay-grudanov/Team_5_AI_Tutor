---
source_image: page_188.png
page_number: 188
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 8.22
tokens: 7327
characters: 1115
timestamp: 2025-12-23T23:08:56.551926
finish_reason: stop
---

В примере 12.3 показан сценарий, читающий файл Apache access.log, приведенный в примере 7.2. Для переформатирования и вывода файла журнала в виде HTML используется функция tagit.

Пример 12.3. weblogfmt.sh

#!/bin/bash -
#
# Bash и кибербезопасность
# weblogfmt.sh
#
# Описание:
# Чтение веб-журнала Apache и его вывод в виде HTML
#
# Использование:
# weblogfmt.sh < input.file > output.file

function tagit()
{
    printf '<%s>%s</%s>\n' "${1}" "${2}" "${1}"
}

# основные теги заголовка
echo "<html>"
echo "<body>"
echo "<h1>$1</h1>"        # заголовок

echo "<table border=1>"   # таблица с границами
echo "<tr>"               # новая строка таблицы
echo "<th>IP Address</th>" # заголовок столбца
echo "<th>Date</th>"
echo "<th>URL Requested</th>"
echo "<th>Status Code</th>"
echo "<th>Size</th>"
echo "<th>Referrer</th>"
echo "<th>User Agent</th>"
echo "</tr>"

while read f1 f2 f3 f4 f5 f6 f7 f8 f9 f10 f11 f12plus
do
    echo "<tr>"
    tagit "td" "${f1}"
    tagit "td" "${f4} ${f5}"
    tagit "td" "${f6} ${f7}"
    tagit "td" "${f9}"
    tagit "td" "${f10}"
    tagit "td" "${f11}"

    # 1
    # 2
    # 3