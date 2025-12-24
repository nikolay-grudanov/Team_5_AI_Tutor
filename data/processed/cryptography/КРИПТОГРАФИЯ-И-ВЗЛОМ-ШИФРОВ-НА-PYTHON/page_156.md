---
source_image: page_156.png
page_number: 156
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 30.99
tokens: 7438
characters: 1540
timestamp: 2025-12-24T08:49:50.585303
finish_reason: stop
---

каждое из выражений \(10 < 5\) и \(4 != 4\) равно False, второе выражение вычисляется как False or False, что дает False.

Таблица истинности для оператора or приведена в табл. 8.2.

Таблица 8.2. Таблица истинности оператора or

<table>
  <tr>
    <th>A or B</th>
    <th>Результат</th>
  </tr>
  <tr>
    <td>True or True</td>
    <td>True</td>
  </tr>
  <tr>
    <td>True or False</td>
    <td>True</td>
  </tr>
  <tr>
    <td>False or True</td>
    <td>True</td>
  </tr>
  <tr>
    <td>False or False</td>
    <td>False</td>
  </tr>
</table>

Есть еще третий булев оператор — not (логическое НЕ). Оператор not возвращает булево значение, противоположное операнду. Поэтому not True равно False, а not False равно True. Введите в интерактивной оболочке следующие инструкции.

>>> not 10 > 5
False
>>> not 10 < 5
True
>>> not False
True
>>> not not False
False
>>> not not not not False
True

Как показывают последние два выражения, допускается использовать несколько операторов not подряд. Таблица истинности оператора not приведена в табл. 8.3.

Таблица 8.3. Таблица истинности оператора not

<table>
  <tr>
    <th>not A</th>
    <th>Результат</th>
  </tr>
  <tr>
    <td>not True</td>
    <td>False</td>
  </tr>
  <tr>
    <td>not False</td>
    <td>True</td>
  </tr>
</table>

Сокращение выражений с помощью операторов and и or

Аналогично тому как цикл for позволяет выполнить ту же работу, что и цикл while, но при меньшем объеме кода, операторы and и or также дают возможность немного сократить код. Введите в интерактивной оболочке