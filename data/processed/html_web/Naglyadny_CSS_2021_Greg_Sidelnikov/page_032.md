---
source_image: page_032.png
page_number: 32
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 22.96
tokens: 7177
characters: 756
timestamp: 2025-12-24T09:21:13.949359
finish_reason: stop
---

2 Псевдоэлементы

Псевдоэлементы начинаются с двойного двоеточия ::. В данном контексте псевдо означает, что они не ссылаются на явные элементы DOM, вручную добавленные в документ HTML, например элемент выделения текста.

2.1. ::after

p::after { content: "Добавлено после"; }

<table>
  <tr>
    <th>Одной из часто упускаемых особенностей CSS являются псевдоэлементы.</th>
    <th>Добавлено после</th>
  </tr>
</table>

2.2. ::before

p::before { content: "Добавлено до"; }

<table>
  <tr>
    <th>Добавлено до</th>
    <td><p>Одной из часто упускаемых особенностей CSS являются псевдоэлементы.</p></td>
  </tr>
</table>

2.3. ::first-letter

p::first-letter { font-size: 200%; }

<p>Одной из часто упускаемых особенностей CSS являются псевдоэлементы.</p>