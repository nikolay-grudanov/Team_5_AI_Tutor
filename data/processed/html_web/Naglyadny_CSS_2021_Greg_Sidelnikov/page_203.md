---
source_image: page_203.png
page_number: 203
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 37.36
tokens: 7576
characters: 1763
timestamp: 2025-12-24T09:25:19.061116
finish_reason: stop
---

Операторы сравнения

<table>
  <tr>
    <th>Оператор</th>
    <th>Пример</th>
    <th>Описание</th>
  </tr>
  <tr>
    <td>==</td>
    <td>x==y</td>
    <td>Возвращает значение true (истина) при x, равном y</td>
  </tr>
  <tr>
    <td>!=</td>
    <td>x!=y</td>
    <td>Возвращает значение true (истина), если x и y не равны</td>
  </tr>
  <tr>
    <td>&gt;</td>
    <td>x&gt;y</td>
    <td>Возвращает значение true (истина), если x больше y</td>
  </tr>
  <tr>
    <td>&lt;</td>
    <td>x&lt;y</td>
    <td>Возвращает значение true (истина), если x меньше y</td>
  </tr>
  <tr>
    <td>&gt;=</td>
    <td>x&gt;=y</td>
    <td>Возвращает значение true (истина), если x больше или равно y</td>
  </tr>
  <tr>
    <td>&lt;=</td>
    <td>x&lt;=y</td>
    <td>Возвращает значение true (истина), если x меньше или равно y</td>
  </tr>
</table>

Как использовать операторы сравнения на практике? Можно написать примесь, которая выберет размер заполнения, если его значение больше значения внешнего отступа.

001 @mixin spacing($padding, $margin) {
002   @if ($padding > $margin) {
003     padding: $padding;
004   } @else {
005     padding: $margin;
006   }
007 }
008 .container {
009   @include spacing(10px, 20px);
010 }

После компиляции мы получим следующий код.

001 .container { padding: 20px; }

Логические операторы

<table>
  <tr>
    <th>Оператор</th>
    <th>Пример</th>
    <th>Описание</th>
  </tr>
  <tr>
    <td>and</td>
    <td>x and y</td>
    <td>Возвращает значение true (истина), если x и y true</td>
  </tr>
  <tr>
    <td>or</td>
    <td>x or y</td>
    <td>Возвращает значение true (истина), если x или y true</td>
  </tr>
  <tr>
    <td>not</td>
    <td>x not y</td>
    <td>Возвращает значение true (истина), если x не true</td>
  </tr>
</table>