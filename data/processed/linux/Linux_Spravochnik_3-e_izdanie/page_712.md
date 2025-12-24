---
source_image: page_712.png
page_number: 712
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 58.02
tokens: 11859
characters: 1865
timestamp: 2025-12-24T03:47:51.250586
finish_reason: stop
---

<table>
  <tr>
    <th>Alфавитный перечень команд sed</th>
    <th></th>
  </tr>
  <tr>
    <td>s/\n/ /<br>p<br>}</td>
    <td>N</td>
  </tr>
  <tr>
    <td>[address1[,address2]]p</td>
    <td>p</td>
  </tr>
  <tr>
    <td colspan="2">Отобразить указанные строки. Если не задан параметр командной строки -n, эта команда приведет к дублированию строк при выводе. Обычно она используется перед командами, которые изменяют порядок работы с данными (d, N, b) и могут привести к тому, что строка вовсе не будет отображена. См. примеры для h, n и N.</td>
  </tr>
  <tr>
    <td>[address1[,address2]]P</td>
    <td>P</td>
  </tr>
  <tr>
    <td colspan="2">Отобразить первую часть (до вложенного символа новой строки) многострочной копии, созданной с помощью команды N. То же, что и p, если команда N не применялась к строке.</td>
  </tr>
  <tr>
    <td>[address]q</td>
    <td>q</td>
  </tr>
  <tr>
    <td colspan="2">Завершить работу по достижении строки address. Указанная строка предварительно посылается на вывод (если не включено подавление потока вывода по умолчанию), как и любой текст, добавленный к этой строке предшествующими командами a и r.</td>
  </tr>
  <tr>
    <td colspan="2"><b>Примеры</b></td>
  </tr>
  <tr>
    <td colspan="2">Удалить все после указанной строки:</td>
  </tr>
  <tr>
    <td>/Garbled text follows:/q</td>
    <td></td>
  </tr>
  <tr>
    <td colspan="2">Отобразить только 50 первых строк файла:</td>
  </tr>
  <tr>
    <td>50q</td>
    <td></td>
  </tr>
  <tr>
    <td>[address]r file</td>
    <td>r</td>
  </tr>
  <tr>
    <td colspan="2">Добавить содержимое файла к содержимому пространства шаблонов. Между инструкцией r и именем файла должен находиться только один пробел.</td>
  </tr>
  <tr>
    <td colspan="2"><b>Пример</b></td>
  </tr>
  <tr>
    <td>/The list of items follows:/r item_file</td>
    <td></td>
  </tr>
</table>