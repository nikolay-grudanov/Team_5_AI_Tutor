---
source_image: page_187.png
page_number: 187
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 6.49
tokens: 7258
characters: 931
timestamp: 2025-12-23T23:08:51.618773
finish_reason: stop
---

This is a header

this is bold text this is a link

1. This is list item 1
2. This is list item 2

<table>
  <tr>
    <th>Row 1, Column 1</th>
    <th>Row 1, Column 2</th>
  </tr>
  <tr>
    <td>Row 2, Column 1</td>
    <td>Row 2, Column 2</td>
  </tr>
</table>

Рис. 12.1. Визуализированная HTML-страница

Пример 12.2. tagit.sh

#!/bin/bash -
#
# Bash и кибербезопасность
# tagit.sh
#
# Описание:
# Поместить открывающие и закрывающие теги вокруг строки
#
# Использование:
# tagit.sh <tag> <string>
#   <tag> Используемый тег
#   <string> Строка с тегами
#

printf '<%s>%s</%s>\n' "${1}" "${2}" "${1}"

Полученный вывод также можно превратить в простую функцию, которую впоследствии можно включить в другие сценарии:

function tagit ()
{
    printf '<%s>%s</%s>\n' "${1}" "${2}" "${1}"
}

Вы можете использовать HTML-теги для переформатирования практически любого типа данных, после чего чтение этих данных значительно облегчится.