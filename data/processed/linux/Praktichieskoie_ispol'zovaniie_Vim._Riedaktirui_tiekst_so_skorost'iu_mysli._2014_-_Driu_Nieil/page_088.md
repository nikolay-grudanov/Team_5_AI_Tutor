---
source_image: page_088.png
page_number: 88
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 20.66
tokens: 5775
characters: 1687
timestamp: 2025-12-24T04:11:26.350005
finish_reason: stop
---

Допустим, что у нас имеется простая текстовая таблица, как показано ниже:

visual_mode/chapter-table.txt
http://media.pragprog.com/titles/dnvim/code/visual_mode/chapter-table.txt

<table>
  <tr>
    <th>Chapter</th>
    <th>Page</th>
  </tr>
  <tr>
    <td>Normal mode</td>
    <td>15</td>
  </tr>
  <tr>
    <td>Insert mode</td>
    <td>31</td>
  </tr>
  <tr>
    <td>Visual mode</td>
    <td>44</td>
  </tr>
</table>

Нам требуется нарисовать вертикальную линию, чтобы разделить колонки и сделать таблицу больше похожей на настоящую таблицу. Но сначала нам нужно уменьшить количество пробелов между колонками, которые сейчас отстоят друг от друга слишком далеко. Оба эти изменения можно выполнить в блочном визуальном режиме, как показано в табл. 4.3.

Таблица 4.3. Добавление вертикальной линии между колонками

<table>
  <tr>
    <th>Нажатия клавиш</th>
    <th>Содержимое буфера</th>
  </tr>
  <tr>
    <td>{start}</td>
    <td>Chapter<br>Normal mode<br>Insert mode<br>Visual mode<br>Page<br>15<br>31<br>44</td>
  </tr>
  <tr>
    <td><C-v>3j</td>
    <td>Chapter<br>Normal mode<br>Insert mode<br>Visual mode<br>Page<br>15<br>31<br>44</td>
  </tr>
  <tr>
    <td>x...</td>
    <td>Chapter<br>Normal mode<br>Insert mode<br>Visual mode<br>Page<br>15<br>31<br>44</td>
  </tr>
  <tr>
    <td>gv</td>
    <td>Chapter<br>Normal mode<br>Insert mode<br>Visual mode<br>Page<br>15<br>31<br>44</td>
  </tr>
  <tr>
    <td>r|</td>
    <td>Chapter<br>Normal mode |<br>Insert mode |<br>Visual mode |<br>Page<br>15<br>31<br>44</td>
  </tr>
  <tr>
    <td>yyp</td>
    <td>Chapter<br>Chapter<br>Normal mode |<br>Insert mode |<br>Visual mode |<br>Page<br>Page<br>15<br>31<br>44</td>
  </tr>
</table>