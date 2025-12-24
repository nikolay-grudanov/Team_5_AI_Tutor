---
source_image: page_038.png
page_number: 38
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 23.78
tokens: 7225
characters: 884
timestamp: 2025-12-24T09:21:23.951675
finish_reason: stop
---

3.8. :default

input:default выбирает элемент по умолчанию (например, флажок или переключатель).

ДА    НЕТ    ВОЗМОЖНО

<table>
  <tr>
    <th></th>
    <th></th>
    <th></th>
  </tr>
  <tr>
    <td><form></form></td>
    <td><input type = "radio" name = "answer" value = "YES" checked>ДА</br></input></td>
    <td><input type = "radio" name = "answer" value = "NO">НЕТ</br></input></td>
    <td><input type = "radio" name = "answer" value = "MAYBE">ВОЗМОЖНО</br></input></td>
  </tr>
  <tr>
    <td></td>
    <td></td>
    <td></td>
  </tr>
</table>

3.9. :indeterminate

:indeterminate выбирает флажок или переключатель, которым не назначено состояние по умолчанию.

3.10. :required

:required выбирает элемент ввода с обязательным атрибутом.

<input type = "text" required />

3.11. :optional

:optional выбирает элемент ввода без обязательного атрибута.

<input type = "text" />