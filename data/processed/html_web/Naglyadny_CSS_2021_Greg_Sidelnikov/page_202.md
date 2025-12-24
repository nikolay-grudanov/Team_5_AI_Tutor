---
source_image: page_202.png
page_number: 202
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 35.14
tokens: 7381
characters: 1221
timestamp: 2025-12-24T09:25:16.848186
finish_reason: stop
---

Остаток

Оставшаяся часть вычисляет остаток от операции деления. В данном примере посмотрим, как его можно использовать при создании шаблона «полоски зебры» для произвольного набора HTML-элементов.

Начнем с создания примеси zebra. Примечание: директивы @for и @if обсуждаются в следующем разделе.

001 @mixin zebra(); {
002     @for $i from 1 through 7 {
003         @if ($i % 2 == 1) {
004             .stripe-#{$i} {
005                 background-color: black;
006                 color: white;
007             }
008         }
009     }
010 }
011
012 * { @include zebra(); }

Для этой демонстрации требуется несколько HTML-элементов.

001 <div class = "stripe-1">zebra</div>
002 <div class = "stripe-2">zebra</div>
003 <div class = "stripe-3">zebra</div>
004 <div class = "stripe-4">zebra</div>
005 <div class = "stripe-5">zebra</div>
006 <div class = "stripe-6">zebra</div>
007 <div class = "stripe-7">zebra</div>

И вот результат в браузере — чередующиеся полосы, созданные примесью zebra:

<table>
  <tr><th>zebra</th></tr>
  <tr><td>zebra</td></tr>
  <tr><td>zebra</td></tr>
  <tr><td>zebra</td></tr>
  <tr><td>zebra</td></tr>
  <tr><td>zebra</td></tr>
  <tr><td>zebra</td></tr>
  <tr><td>zebra</td></tr>
</table>