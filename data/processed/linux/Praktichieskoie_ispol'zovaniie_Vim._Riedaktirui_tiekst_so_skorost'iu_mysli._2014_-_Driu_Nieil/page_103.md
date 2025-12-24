---
source_image: page_103.png
page_number: 103
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 25.12
tokens: 5809
characters: 1963
timestamp: 2025-12-24T04:11:51.276251
finish_reason: stop
---

<table>
  <tr>
    <th>Нажатия клавиш</th>
    <th>Содержимое буфера</th>
  </tr>
  <tr>
    <td>{start}</td>
    <td>Shopping list<br>Hardware Store<br>Buy new hammer<br>Beauty Parlor<br>Buy nail polish remover<br>Buy nails</td>
  </tr>
  <tr>
    <td>:6copy.</td>
    <td>Shopping list<br>Hardware Store<br><b>Buy nails</b><br>Buy new hammer<br>Beauty Parlor<br>Buy nail polish remover<br>Buy nails</td>
  </tr>
</table>

В общем виде команда копирования имеет следующий формат (см. :h :copy i http://vimdoc.sourceforge.net/htmldoc/change.html#:copy):

:[range]copy{address}

В этом примере диапазон [range] определяет строку с номером 6, а в качестве адреса {address} используется символ точки (.), которому соответствует текущая строка. То есть команду :6copy. можно прочитать как: «Скопировать строку 6 и вставить ее ниже текущей строки».

Команду :copy можно сократить до двух символов, :co. А чтобы обеспечить еще большую краткость, можно воспользоваться командой :t, которая является синонимом команды :copy. Для запоминания ее можно читать как: «copy TO» (копировать в). Ниже приводится несколько примеров использования команды :t:

<table>
  <tr>
    <th>Команда</th>
    <th>Действие</th>
  </tr>
  <tr>
    <td>:6t.</td>
    <td>Вставит копию 6-й строки за текущей</td>
  </tr>
  <tr>
    <td>:t6</td>
    <td>Скопирует текущую строку и вставит ее за 6-й строкой</td>
  </tr>
  <tr>
    <td>:t.</td>
    <td>Скопирует текущую строку и вставит ее за текущей (аналог команды уур в командном режиме)</td>
  </tr>
  <tr>
    <td>:t$</td>
    <td>Скопирует текущую строку и вставит ее в конец файла</td>
  </tr>
  <tr>
    <td>:'<,'>t0</td>
    <td>Скопирует выделенные строки в начало файла</td>
  </tr>
</table>

Обратите внимание, что команда :t. дублирует текущую строку. Тот же эффект дает последовательность команд копирования и вставки в командном режиме (уур). Единственное существенное различие между этими двумя приемами состоит в том, что коман-