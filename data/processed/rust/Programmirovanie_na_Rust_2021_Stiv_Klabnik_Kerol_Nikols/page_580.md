---
source_image: page_580.png
page_number: 580
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 21.78
tokens: 7368
characters: 1149
timestamp: 2025-12-24T11:00:56.293526
finish_reason: stop
---

Таблица Б.9 показывает контексты, в которых используются фигурные скобки.

Таблица Б.9. Фигурные скобки

<table>
  <tr>
    <th>Символ</th>
    <th>Объяснение</th>
  </tr>
  <tr>
    <td>{...}</td>
    <td>Блочное выражение</td>
  </tr>
  <tr>
    <td>Type {...}</td>
    <td>Литерал struct</td>
  </tr>
</table>

Таблица Б.10 показывает контексты, в которых используются квадратные скобки.

Таблица Б.10. Квадратные скобки

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
    <td>Литерал массива, содержащий len копий выражения expr</td>
  </tr>
  <tr>
    <td>[type; len]</td>
    <td>Массивный тип, содержащий len экземпляров типа type</td>
  </tr>
  <tr>
    <td>expr[expr]</td>
    <td>Индексирование коллекции; перегружаемое (Index, IndexMut)</td>
  </tr>
  <tr>
    <td>expr[..], expr[a..],</td>
    <td></td>
  </tr>
  <tr>
    <td>expr[..b], expr[a..b]</td>
    <td>Индексирование коллекции, внешне похожее на нарезку коллекции, использующее Range, RangeFrom, RangeTo или RangeFull в качестве «индекса»</td>
  </tr>
</table>