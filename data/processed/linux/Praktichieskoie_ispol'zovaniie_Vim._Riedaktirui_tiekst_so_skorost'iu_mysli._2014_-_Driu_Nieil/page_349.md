---
source_image: page_349.png
page_number: 349
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 23.11
tokens: 5672
characters: 1537
timestamp: 2025-12-24T04:16:56.219146
finish_reason: stop
---

Рецепт 115. Автодополнение целых строк

Во всех примерах, приводившихся до сих пор, демонстрировалось дополнение отдельных слов, но Vim способен также производить дополнение целых строк.

Режим автодополнения целых строк активируется нажатием <C-x><C-l> (см. :h compl-whole-line http://vimdoc.sourceforge.net/htmldoc/insert.html#compl-whole-line).

Допустим, у нас имеется следующий фрагмент:

auto_complete/bg-colors.css
http://media.pragprog.com/titles/dnvim/code/auto_complete/bg-colors.css

.top {
    background-color: #ef66ef; }
.bottom {

Нам требуется вставить в конец файла копию второй строки. Ниже показано, как этого добиться с применением автодополнения целых строк (табл. 19.3).

Таблица 19.3. Добавление в конец файла копии второй строки

<table>
  <tr>
    <th>Нажатия клавиш</th>
    <th>Содержимое буфера</th>
  </tr>
  <tr>
    <td>{start}</td>
    <td>.top {<br>background-color: #ef66ef; }<br>.bottom {</td>
  </tr>
  <tr>
    <td>oba</td>
    <td>.top {<br>background-color: #ef66ef; }<br>.bottom {<br>ba</td>
  </tr>
  <tr>
    <td><C-x><C-l><Esc></td>
    <td>.top {<br>background-color: #ef66ef; }<br>.bottom {<br>background-color: #ef66ef; }</td>
  </tr>
</table>

Функция автодополнения целых строк использует те же источники, что и функция обобщенного автодополнения (см. рецепт 113 выше), а также генерирует список целых строк. При этом Vim игнорирует любые отступы в начале строки.

Вся прелесть автодополнения целыми строками — в отсутствии необходимости знать, где находится требуемая строка, которую тре-