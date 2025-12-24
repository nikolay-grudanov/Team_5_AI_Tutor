---
source_image: page_042.png
page_number: 42
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 19.73
tokens: 5664
characters: 1461
timestamp: 2025-12-24T04:10:22.860221
finish_reason: stop
---

Рецепт 1. Встречайте: команда «точка»

dd, тогда под «последним изменением» Vim будет понимать удаление текущей строки:

<table>
  <tr>
    <th>Нажатия клавиш</th>
    <th>Содержимое буфера</th>
  </tr>
  <tr>
    <td>{start}</td>
    <td>Line one<br>Line two<br>Line three<br>Line four</td>
  </tr>
  <tr>
    <td>dd</td>
    <td>ine one<br>Line two<br>Line three<br>Line four</td>
  </tr>
  <tr>
    <td>.</td>
    <td>Line three<br>Line four</td>
  </tr>
</table>

Наконец, команда >G увеличивает отступ, начиная с текущей строки, до конца файла. После выполнения этой команды под «последним изменением» Vim будет понимать увеличение отступа от текущей строки до конца файла. Этот пример мы начали с того, что поместили курсор в начало второй строки, чтобы подчеркнуть отличия.

<table>
  <tr>
    <th>Нажатия клавиш</th>
    <th>Содержимое буфера</th>
  </tr>
  <tr>
    <td>{start}</td>
    <td>Line one<br>Line two<br>Line three<br>Line four</td>
  </tr>
  <tr>
    <td>>G</td>
    <td>Line one<br>Line two<br>Line three<br>Line four</td>
  </tr>
  <tr>
    <td>j</td>
    <td>Line one<br>Line two<br>Line three<br>Line four</td>
  </tr>
  <tr>
    <td>.</td>
    <td>Line one<br>Line two<br>Line three<br>Line four</td>
  </tr>
  <tr>
    <td>j.</td>
    <td>Line one<br>Line two<br>Line three<br>Line four</td>
  </tr>
</table>

Все команды — x, dd и > — выполняются в командном режиме, но изменения также создаются каждый раз при входе в режим вставки.