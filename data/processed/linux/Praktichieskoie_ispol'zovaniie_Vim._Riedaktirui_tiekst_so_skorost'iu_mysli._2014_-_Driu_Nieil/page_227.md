---
source_image: page_227.png
page_number: 227
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 23.32
tokens: 5690
characters: 1624
timestamp: 2025-12-24T04:14:27.041756
finish_reason: stop
---

Таблица 11.3. Последовательное выполнение макроса

<table>
  <tr>
    <th>Нажатия клавиш</th>
    <th>Содержимое буфера</th>
  </tr>
  <tr>
    <td>qA</td>
    <td>module Rank<br>class Animal<br># implementation...<br>end<br>end</td>
  </tr>
  <tr>
    <td>:next</td>
    <td>class Banker<br># implementation...<br>end</td>
  </tr>
  <tr>
    <td>q</td>
    <td>class Banker<br># implementation...<br>end</td>
  </tr>
  <tr>
    <td>22@a</td>
    <td>class Banker<br># implementation...<br>end</td>
  </tr>
</table>

Сохранение изменений во всех файлах

Мы изменили четыре файла, но пока не сохранили их. Мы можем выполнить команду :argdo write, чтобы сохранить сразу все файлы в списке аргументов, но существует более простой способ:

⇒ :wall

Обратите внимание, что эта команда сохранит все файлы в списке буферов, поэтому она не является точным эквивалентом команды :argdo write (см. :h :wa i http://vimdoc.sourceforge.net/htmldoc/editing.html#:wa).

Еще одна полезная команда: :wnext (см. :h :wn i http://vimdoc.sourceforge.net/htmldoc/editing.html#:wn), эквивалентная вызову команды :write с последующей командой :next. Если вы применяете макрос последовательно к нескольким файлам в списке аргументов, возможно, вы предпочтете ее.

Обсуждение

Допустим, что во время выполнения макроса в третьем буфере в списке аргументов возникла какая-то ошибка, прервавшая его. Если бы мы использовали команду :argdo normal @a, макрос прервался бы только в этом буфере, а если бы мы запустили макрос последовательно, указав счетчик, выполнение остановилось бы на буфере, вызвавшем ошибку, и все остальные остались бы без изменений.