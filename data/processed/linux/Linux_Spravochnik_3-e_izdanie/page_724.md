---
source_image: page_724.png
page_number: 724
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 61.95
tokens: 11981
characters: 2024
timestamp: 2025-12-24T03:48:23.137817
finish_reason: stop
---

Перечень команд awk по группам

Команды gawk можно классифицировать следующим образом:

<table>
  <tr>
    <th>Арифметические функции</th>
    <th>Строковые функции</th>
    <th>Операторы управления</th>
    <th>Обработка ввода/вывода</th>
    <th>Функции времени</th>
    <th>Прочие</th>
  </tr>
  <tr>
    <td>atan2</td>
    <td>gensub</td>
    <td>break</td>
    <td>close</td>
    <td>strftime</td>
    <td>delete</td>
  </tr>
  <tr>
    <td>cos</td>
    <td>gsub</td>
    <td>continue</td>
    <td>fflush</td>
    <td>systime</td>
    <td>function</td>
  </tr>
  <tr>
    <td>exp</td>
    <td>index</td>
    <td>do/while</td>
    <td>getline</td>
    <td></td>
    <td>system</td>
  </tr>
  <tr>
    <td>int</td>
    <td>length</td>
    <td>exit</td>
    <td>next</td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>log</td>
    <td>match</td>
    <td>for</td>
    <td>nextfile</td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>rand</td>
    <td>split</td>
    <td>if</td>
    <td>print</td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>sin</td>
    <td>sub</td>
    <td>return</td>
    <td>printf</td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>sqrt</td>
    <td>substr</td>
    <td></td>
    <td>sprintf</td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>srand</td>
    <td>tolower</td>
    <td></td>
    <td>while</td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td></td>
    <td>toupper</td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
  </tr>
</table>

Алфавитный перечень команд

В следующий перечень включены все доступные в Linux операторы и функции gawk.

atan2 (y, x)
Вернуть арктангенс y/x в радианах.

break
Прекратить выполнение цикла while или for.

close (filename-expr)
close (command-expr)
Закрыть канал или файл, из которого выполняется чтение по команде getline; в качестве аргумента принимается то же выражение, что использовалось для открытия файла или канала.

continue
Перейти к следующей итерации цикла while или for, не дожидаясь завершения текущей.