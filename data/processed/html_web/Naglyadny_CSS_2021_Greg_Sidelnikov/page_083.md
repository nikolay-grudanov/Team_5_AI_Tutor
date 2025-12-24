---
source_image: page_083.png
page_number: 83
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 26.30
tokens: 7173
characters: 756
timestamp: 2025-12-24T09:22:25.743890
finish_reason: stop
---

11 Плавающие элементы

Блокирующие элементы со свойствами float: left и float: right появляются в одной строке, если сумма их ширины меньше, чем ширина родительского элемента:

<table>
  <tr>
    <th>float: left</th>
    <th>float: left</th>
    <th>float: right</th>
  </tr>
</table>

Если общая сумма двух плавающих элементов превышает ширину родительского элемента, то один из них будет заблокирован другим и перейдет к следующей строке:

<table>
  <tr>
    <th>float: left</th>
    <th>float: right</th>
  </tr>
</table>

Очистить плавающие элементы и начать новую плавающую строку можно с помощью свойства clear: both:

<table>
  <tr>
    <th>float: left</th>
    <th>float: left</th>
    <th>float: left</th>
    <th>clear: both</th>
  </tr>
</table>