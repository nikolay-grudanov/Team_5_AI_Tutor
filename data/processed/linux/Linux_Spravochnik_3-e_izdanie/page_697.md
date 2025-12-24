---
source_image: page_697.png
page_number: 697
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 34.91
tokens: 11659
characters: 1230
timestamp: 2025-12-24T03:46:48.942142
finish_reason: stop
---

<table>
  <tr>
    <th>&lt;&gt;</th>
    <td>[address]&lt;[count]<br>[address]&gt;[count]</td>
    <td>Сдвинуть count строк по указанному адресу влево (&lt;) или вправо (&gt;). При сдвиге влево удаляются только пробелы и символы табуляции.</td>
  </tr>
  <tr>
    <th>address</th>
    <td>address</td>
    <td>Отобразить строку, имеющую указанный адрес.</td>
  </tr>
  <tr>
    <th>Enter</th>
    <td>Enter</td>
    <td>Отобразить следующую строку файла.</td>
  </tr>
  <tr>
    <th>&</th>
    <td>& [options][count]</td>
    <td>Повторить последнюю команду замены (s). Параметр count определяет количество строк, в которых будет производиться замена, начиная со строки address.<br><b>Примеры</b><br>:s/Overdue/Paid <i>Однократная замена в текущей строке</i><br>:g/Status/& <i>Повторить замену для всех строк, содержащих слово «Status»</i></td>
  </tr>
  <tr>
    <th>~</th>
    <td>[address]~[count]</td>
    <td>Заменить предыдущее регулярное выражение предыдущим шаблоном подстановки из команды substitute (s).</td>
  </tr>
  <tr>
    <th>^D</th>
    <td>^D</td>
    <td>Просмотр файла.</td>
  </tr>
  <tr>
    <th>^Z</th>
    <td>^Z</td>
    <td>Приостановка сеанса редактирования. Возврат по команде fg.</td>
  </tr>
</table>