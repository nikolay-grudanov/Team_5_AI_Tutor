---
source_image: page_106.png
page_number: 106
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 24.59
tokens: 5791
characters: 1829
timestamp: 2025-12-24T04:11:51.104587
finish_reason: stop
---

экономии места в книге я приведу только пять строк, но если вы сможете представить на их месте 50 строк, то получите более полное представление о возможностях описываемого приема.

ex_mode/foobar.js
http://media.pragprog.com/titles/dnvim/code/ex_mode/foobar.js

var foo = 1
var bar = 'a'
var baz = 'z'
var foobar = foo + bar
var foobarbaz = foo + bar + baz

Начнем, как и прежде, с изменения первой строки:

<table>
  <tr>
    <th>Нажатия клавиш</th>
    <th>Содержимое буфера</th>
  </tr>
  <tr>
    <td>{start}</td>
    <td>var foo = 1<br>var bar = 'a'<br>var baz = 'z'<br>var foobar = foo + bar<br>var foobarbaz = foo + bar + baz</td>
  </tr>
  <tr>
    <td>A;<Esc></td>
    <td>var foo = 1;<br>var bar = 'a'<br>var baz = 'z'<br>var foobar = foo + bar<br>var foobarbaz = foo + bar + baz</td>
  </tr>
</table>

Нам нужно применить команду «точка» не к одной строке, а к целому диапазону. Для этого можно использовать команду :normal:

<table>
  <tr>
    <th>Нажатия клавиш</th>
    <th>Содержимое буфера</th>
  </tr>
  <tr>
    <td>j VG</td>
    <td>var foo = 1;<br><span style="background-color:#e0e0e0">var bar = 'a'</span><br><span style="background-color:#e0e0e0">var baz = 'z'</span><br>var foobar = foo + bar<br><span style="background-color:#e0e0e0">var foobarbaz = foo + bar + baz</span></td>
  </tr>
  <tr>
    <td>:'<,'>normal .</td>
    <td>var foo = 1;<br>var bar = 'a';<br>var baz = 'z';<br>var foobar = foo + bar;<br>var foobarbaz = foo + bar + baz;</td>
  </tr>
</table>

Команду :'<,'>normal. можно прочитать как: «Для каждой строки в визуальном выделении выполнить команду . командного режима». Этот прием будет работать одинаково и для пяти строк, и для пятидесяти. Но истинная его прелесть состоит в том, что нам не нужно даже считать строки — мы можем избежать необходимости выделять их в визуальном режиме.