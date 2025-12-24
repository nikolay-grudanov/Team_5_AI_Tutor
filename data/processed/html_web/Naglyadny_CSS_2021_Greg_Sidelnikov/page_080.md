---
source_image: page_080.png
page_number: 80
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 40.77
tokens: 7379
characters: 1304
timestamp: 2025-12-24T09:22:39.794379
finish_reason: stop
---

Позже, когда мы перейдем к главам, описывающим grid- и flex-верстку, вы увидите, как применение значений flex либо grid к свойству display может изменить поведение его элементов, находящихся внутри элемента контейнера, часто называемого их родительским.

Свойство display: block, в отличие от inline, автоматически блокирует весь ряд пространства независимо от ширины его содержимого. HTML-элементы div по умолчанию являются блокирующими элементами:

block

<table>
  <tr><th>a</th></tr>
  <tr><th>b</th></tr>
  <tr><td>Длинная строка текста. Но недостаточно.</td></tr>
  <tr><th>d</th></tr>
  <tr><th>e</th></tr>
  <tr><th>f</th></tr>
  <tr><th>g</th></tr>
</table>

Свойство display: block с явно заданной шириной элемента показывает распознавание ширины контейнера элемента и ширины его содержимого:

<div { width: n }, где n — числовое значение в пикселях или процентах от ширины контейнера

<table>
  <tr><th>a</th></tr>
  <tr><th>b</th></tr>
  <tr><th>c</th></tr>
  <tr><th>d</th></tr>
  <tr><th>e</th></tr>
  <tr><th>f</th></tr>
  <tr><th>g</th></tr>
</table>

Свойство display: inline-block сочетает в себе поведение inline и blocking, чтобы включить пользовательский размер для встроенных элементов:

<table>
  <tr><th>hello</th><th>b</th><th>c</th><th>d</th><th>e f</th><th>g</th></tr>
</table>