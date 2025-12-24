---
source_image: page_039.png
page_number: 39
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 45.48
tokens: 7488
characters: 1393
timestamp: 2025-12-24T09:21:49.213844
finish_reason: stop
---

3.12. :read-only

:read-only и read-write выбирают элементы с атрибутами readonly и disabled.

<table>
  <tr>
    <th><input type = "text" disabled readonly /></th>
  </tr>
</table>

3.13. :root

:root выбирает корневой элемент DOM (html).

<html></html>

3.14. :only-of-type

li:only-of-type

<table>
  <tr>
    <th colspan="2">&lt;div&gt;</th>
  </tr>
  <tr>
    <th>&lt;ul&gt;</th>
    <th></th>
  </tr>
  <tr>
    <td>&lt;li&gt;&lt;span&gt;Содержимое&lt;/span&gt;&lt;/li&gt;</td>
    <td></td>
  </tr>
  <tr>
    <td>&lt;li&gt;&lt;span&gt;Содержимое&lt;/span&gt;&lt;/li&gt;</td>
    <td></td>
  </tr>
  <tr>
    <td>&lt;li&gt;&lt;span&gt;Содержимое&lt;/span&gt;&lt;/li&gt;</td>
    <td></td>
  </tr>
  <tr>
    <th>&lt;/ul&gt;</th>
    <th></th>
  </tr>
  <tr>
    <th colspan="2">&lt;/div&gt;</th>
  </tr>
</table>

3.15. :first-of-type

div ul li:first-of-type

<table>
  <tr>
    <th colspan="2">&lt;div&gt;</th>
  </tr>
  <tr>
    <th>&lt;ul&gt;</th>
    <th></th>
  </tr>
  <tr>
    <td>&lt;li&gt;&lt;span&gt;Содержимое&lt;/span&gt;&lt;/li&gt;</td>
    <td></td>
  </tr>
  <tr>
    <td>&lt;li&gt;&lt;span&gt;Содержимое&lt;/span&gt;&lt;/li&gt;</td>
    <td></td>
  </tr>
  <tr>
    <td>&lt;li&gt;&lt;span&gt;Содержимое&lt;/span&gt;&lt;/li&gt;</td>
    <td></td>
  </tr>
  <tr>
    <th>&lt;/ul&gt;</th>
    <th></th>
  </tr>
  <tr>
    <th colspan="2">&lt;/div&gt;</th>
  </tr>
</table>