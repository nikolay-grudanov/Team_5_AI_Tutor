---
source_image: page_225.png
page_number: 225
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 21.03
tokens: 5701
characters: 1772
timestamp: 2025-12-24T04:14:19.034015
finish_reason: stop
---

<table>
  <tr>
    <th>Нажатия клавиш</th>
    <th>Содержимое буфера</th>
  </tr>
  <tr>
    <td>Omodule Rank<Esc></td>
    <td># ...[end of copyright notice]<br>module Rank<br>class Animal<br>    # implementation...<br>end</td>
  </tr>
  <tr>
    <td>j>G</td>
    <td># ...[end of copyright notice]<br>module Rank<br>    class Animal<br>        # implementation...<br>    end</td>
  </tr>
  <tr>
    <td>Goend<Esc></td>
    <td># ...[end of copyright notice]<br>module Rank<br>    class Animal<br>        # implementation...<br>    end<br>end</td>
  </tr>
  <tr>
    <td>q</td>
    <td># ...[end of copyright notice]<br>module Rank<br>    class Animal<br>        # implementation...<br>    end<br>end</td>
  </tr>
</table>

Каждый из файлов начинается с упоминания об авторских правах, поэтому нам необходимо очень тщательно подойти к нормализации позиции курсора. Команда gg поместит курсор в начало файла, а команда /class<CR> передвинет его к первому совпадению со словом «class». После выполнения этих подготовительных шагов мы можем приступать к внесению изменений.

С помощью команды O мы вставляем новую строку над курсором и добавляем в нее текст. Затем переносим курсор на следующую строку, где командой >G оформляем отступы во всех строках ниже. Наконец, командой G мы переходим в конец файла, с помощью команды o создаем новую строку ниже курсора и добавляем в нее ключевое слово end.

Если вы следовали за примером, выполняя те же действия в своем редакторе, постарайтесь воспротивиться желанию немедленно сохранить изменения в файле командой :w. Почему следует воздержаться от нее, я объясню чуть ниже.

Параллельное выполнение макроса

Команда :argdo позволяет выполнить команду Ex для каждого буфера в списке аргументов (см. :h :argdo http://vimdoc.source-