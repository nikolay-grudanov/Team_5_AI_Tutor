---
source_image: page_571.png
page_number: 571
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 47.82
tokens: 11745
characters: 1485
timestamp: 2025-12-24T03:41:11.026907
finish_reason: stop
---

<table>
  <tr>
    <th>test</th>
    <td>
      <i>string</i><br>
      Строка не пуста.<br>
      <b>Целочисленные сравнения</b><br>
      <i>n1 -eq n2</i><br>
      <i>n1</i> равно <i>n2</i>.<br>
      <i>n1 -ge n2</i><br>
      <i>n1</i> больше либо равно <i>n2</i>.<br>
      <i>n1 -gt n2</i><br>
      <i>n1</i> больше <i>n2</i>.<br>
      <i>n1 -le n2</i><br>
      <i>n1</i> меньше либо равно <i>n2</i>.<br>
      <i>n1 -lt n2</i><br>
      <i>n1</i> меньше <i>n2</i>.<br>
      <i>n1 -ne n2</i><br>
      <i>n1</i> не равно <i>n2</i>.<br>
      <b>Сочетание условий</b><br>
      <i>! condition</i><br>
      Истинно, если условие <i>condition</i> ложно.<br>
      <i>condition1 -a condition2</i><br>
      Истинно, если истинны оба условия.<br>
      <i>condition1 -o condition2</i><br>
      Истинно, если истинно хотя бы одно из условий.<br>
      <b>Примеры</b><br>
      Каждый из следующих примеров представляет собой первую строку какого-либо оператора, использующего проверку условий:<br>
      <pre>
      while test $# -gt 0        Пока есть аргументы...
      while [ -n "$1" ]          Пока первый аргумент не пуст...
      if [ $count -lt 10 ]       Если $count меньше 10...
      if [ -d RCS ]              Если существует каталог RCS...
      if [ "$answer" != "y" ]    Если ответ — не y...
      if [ ! -r "$1" -o ! -f "$1" ] Если первый аргумент является файлом, запрещенным для чтения, или не является обычным файлом...
      </pre>
    </td>
  </tr>
</table>