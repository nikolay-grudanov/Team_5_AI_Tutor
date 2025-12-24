---
source_image: page_305.png
page_number: 305
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 21.40
tokens: 5629
characters: 1418
timestamp: 2025-12-24T04:15:59.082023
finish_reason: stop
---

Таблица 15.1. Сортировка фрагмента файла

<table>
  <tr>
    <th>Нажатия клавиш</th>
    <th>Содержимое буфера</th>
  </tr>
  <tr>
    <td>{start}</td>
    <td>html {
      margin: 0;
      padding: 0;
      border: 0;
      font-size: 100%;
      font: inherit;
      vertical-align: baseline;
    }</td>
  </tr>
  <tr>
    <td>vi{</td>
    <td>html {
      <span style="background-color:#e0f2f1">margin: 0;</span>
      <span style="background-color:#e0f2f1">padding: 0;</span>
      <span style="background-color:#e0f2f1">border: 0;</span>
      <span style="background-color:#e0f2f1">font-size: 100%;</span>
      <span style="background-color:#e0f2f1">font: inherit;</span>
      <span style="background-color:#e0f2f1">vertical-align: baseline;</span>
    }</td>
  </tr>
  <tr>
    <td>:'<,'>sort</td>
    <td>html {
      <span style="background-color:#e0f2f1">border: 0;</span>
      font-size: 100%;
      font: inherit;
      margin: 0;
      padding: 0;
      vertical-align: baseline;
    }</td>
  </tr>
</table>

Сортировка свойств во всех блоках

Мы можем отсортировать свойства во всех блоках единственной командой :global. Например, если применить следующую команду к нашей таблице стилей:

⇒ :g/{/ .+1,/}-1 sort

Мы получим:

html {
  border: 0;
  font-size: 100%;
  font: inherit;
  margin: 0;
  padding: 0;
  vertical-align: baseline;
}
body {
  background: white;
  color: black;
  line-height: 1.5;