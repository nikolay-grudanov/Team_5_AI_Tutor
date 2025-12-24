---
source_image: page_197.png
page_number: 197
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 21.25
tokens: 5743
characters: 1898
timestamp: 2025-12-24T04:13:45.314349
finish_reason: stop
---

Регистр захвата («0)

При выполнении команды y{motion} текст копируется не только в неименованный регистр, но также в дополнительный регистр захвата, который адресуется символом 0 (см.: h quote0 http://vimdoc.sourceforge.net/htmldoc/change.html#quote0).

Как следует из названия, регистр захвата изменяется только командой y{motion}. Иными словами, его содержимое не изменяется командами x, s, c{motion} и d{motion}. Если вы захватили некоторый текст, то можете быть уверены, что он сохранится в регистре 0, пока явно не будет затерт другой командой захвата. Регистр захвата обеспечивает надежность в ситуациях, когда нельзя положиться на неименованный регистр.

Регистр захвата с успехом можно использовать для решения проблемы, с которой мы столкнулись в разделе «Ой! Я затер свою копию»:

<table>
  <tr>
    <th>Нажатия клавиш</th>
    <th>Содержимое буфера</th>
  </tr>
  <tr>
    <td>yiw</td>
    <td>collection = getCollection();<br>process(somethingInTheWay, target);</td>
  </tr>
  <tr>
    <td>jww</td>
    <td>collection = getCollection();<br>process(somethingInTheWay, target);</td>
  </tr>
  <tr>
    <td>diw</td>
    <td>collection = getCollection();<br>process(, target);</td>
  </tr>
  <tr>
    <td>"0p</td>
    <td>collection = getCollection();<br>process(collection, target);</td>
  </tr>
</table>

Команда diw все еще затирает неименованный регистр, но оставляет регистр захвата нетронутым. Мы без опаски можем вставить текст из регистра захвата, нажав последовательность "0p, и Vim вставит тот текст, который нам необходим.

Если попробовать исследовать содержимое неименованного регистра и регистра захвата, мы увидим в них удаленный и захваченный текст соответственно:

⇒ :reg "0
--- Registers ---
" " somethingInTheWay
"0 collection

Именованные регистры ("a–"z)

В редакторе Vim имеется по одному именованному регистру для каждой буквы латинского алфавита (см.: h quote_alpha