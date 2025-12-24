---
source_image: page_638.png
page_number: 638
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 46.06
tokens: 11814
characters: 1551
timestamp: 2025-12-24T10:45:14.876340
finish_reason: stop
---

Таблица Б-9 показывает контексты, в которых используются фигурные скобки.

Таблица Б-9: Фигурные скобки

<table>
  <tr>
    <th>Обозначение</th>
    <th>Объяснение</th>
  </tr>
  <tr>
    <td>(expr, ...)</td>
    <td>Выражение кортежа</td>
  </tr>
  <tr>
    <td>(type, ...)</td>
    <td>Тип кортежа</td>
  </tr>
  <tr>
    <td>(type, ...)</td>
    <td>Выражение вызова функции; также используется для инициализации структур-кортежей и вариантов-кортежей перечисления</td>
  </tr>
  <tr>
    <td>expr.0, expr.1, etc.</td>
    <td>Взятие элемента по индексу в кортеже</td>
  </tr>
</table>

Таблица Б-10 показывает контексты, в которых используются квадратные скобки.

Таблица Б-10: Квадратные скобки

<table>
  <tr>
    <th>Контекст</th>
    <th>Объяснение</th>
  </tr>
  <tr>
    <td>{...}</td>
    <td>Выражение блока</td>
  </tr>
  <tr>
    <td>Type {...}</td>
    <td>struct литерал</td>
  </tr>
</table>

<table>
  <tr>
    <th>Контекст</th>
    <th>Объяснение</th>
  </tr>
  <tr>
    <td>[...]</td>
    <td>Литерал массива</td>
  </tr>
  <tr>
    <td>[expr; len]</td>
    <td>Литерал массива, содержащий len копий expr</td>
  </tr>
  <tr>
    <td>[type; len]</td>
    <td>Массив, содержащий len экземпляров типа type</td>
  </tr>
  <tr>
    <td>expr[expr]</td>
    <td>Взятие по индексу в коллекции. Возможна перегрузка (Index, IndexMut)</td>
  </tr>
  <tr>
    <td>expr[..], expr[a..], expr[..b], expr[a..b]</td>
    <td>Взятие среза коллекции по индексу, используется Range, RangeFrom, RangeTo, или RangeFull как "индекс"</td>
  </tr>
</table>