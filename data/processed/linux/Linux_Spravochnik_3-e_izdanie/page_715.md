---
source_image: page_715.png
page_number: 715
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 24.76
tokens: 11422
characters: 535
timestamp: 2025-12-24T03:47:26.914158
finish_reason: stop
---

<table>
  <tr>
    <th>х</th>
    <td>[address1[,address2]]<sup>x</sup><br>Обмен содержимого пространства шаблонов и специального буфера. См. пример к описанию команды <b>h</b>.</td>
  </tr>
  <tr>
    <th>y</th>
    <td>[address1[,address2]]<sub>y</sub> /abc/xyz/<br>Преобразование символов. Вхождения символов <i>a</i>, <i>b</i> и <i>c</i> заменяются, соответственно, на <i>x</i>, <i>y</i> и <i>z</i>.<br><b>Пример</b><br># Изменить “item 1, 2, 3...” на “Item A, B, C ...”<br>/^item [1-9]/y/123456789/ABCDEFGHI/</td>
  </tr>
</table>