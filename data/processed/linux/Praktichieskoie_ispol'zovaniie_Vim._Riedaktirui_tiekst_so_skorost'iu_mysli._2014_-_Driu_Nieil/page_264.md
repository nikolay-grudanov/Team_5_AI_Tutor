---
source_image: page_264.png
page_number: 264
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 28.10
tokens: 5902
characters: 2337
timestamp: 2025-12-24T04:15:16.116114
finish_reason: stop
---

Для преобразования символов в верхний регистр можно было бы использовать команду gU{motion}, но какую команду перемещения можно было бы использовать здесь?

Если бы нужно было преобразовать только слово «Xml», для выполнения операции с тремя символами, следующими за курсором, можно было бы использовать команду gU3l (или 3gUl). Если бы нужно было преобразовать только классы с префиксом «Document», можно было бы использовать команду gUtD, чтобы выполнить операцию со всеми символами, вплоть до символа «D». Но ни одно из этих решений не подходит в данном случае.

Одно из возможных решений представлено в табл. 13.3.

Прежде всего напишем регулярное выражение, совпадающее с «Xml» или «Xhtml». Это достаточно просто: команда поиска /\vX(ht)?ml\C<CR> обеспечит достижение желаемого результата. Специальный символ \C включает чувствительность к регистру, поэтому данное регулярное выражение должно работать независимо от значений параметров настройки ignorecase и smartcase. После выполнения поиска с применением этого шаблона подсвеченными оказываются четыре фрагмента, которые требуется изменить, и курсор устанавливается в начало первого совпадения.

Таблица 13.3. Выполнение операций над полным совпадением

<table>
  <tr>
    <th>Нажатия клавиш</th>
    <th>Содержимое буфера</th>
  </tr>
  <tr>
    <td>{start}</td>
    <td>class XhtmlDocument &lt; XmlDocument; end<br>class XhtmlTag &lt; XmlTag; end</td>
  </tr>
  <tr>
    <td>/\vX(ht)?ml\C<CR></td>
    <td>class XhtmlDocument &lt; XmlDocument; end<br>class XhtmlTag &lt; XmlTag; end</td>
  </tr>
  <tr>
    <td>gU//e<CR></td>
    <td>class XHTMLDocument &lt; XmlDocument; end<br>class XhtmlTag &lt; XmlTag; end</td>
  </tr>
  <tr>
    <td>//<CR></td>
    <td>class XHTMLDocument &lt; XmlDocument; end<br>class XhtmlTag &lt; XmlTag; end</td>
  </tr>
  <tr>
    <td>.</td>
    <td>class XHTMLDocument &lt; XMLDocument; end<br>class XhtmlTag &lt; XmlTag; end</td>
  </tr>
  <tr>
    <td>//<CR>.</td>
    <td>class XHTMLDocument &lt; XMLDocument; end<br>class XHTMLTag &lt; XmlTag; end</td>
  </tr>
</table>

Здесь используется следующий трюк: gU//e<CR>. Команда //e<CR> применяется как команда перемещения, которая перемещает курсор от начала до конца совпадения. Независимо от длины совпадения, три («Xml») или пять («Xhtml») символов, команда //e<CR> охватит совпадение целиком.