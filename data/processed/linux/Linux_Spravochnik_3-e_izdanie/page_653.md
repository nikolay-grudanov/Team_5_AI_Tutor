---
source_image: page_653.png
page_number: 653
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 50.05
tokens: 12192
characters: 2510
timestamp: 2025-12-24T03:44:48.676188
finish_reason: stop
---

<table>
  <tr>
    <th>Комбинация</th>
    <th>Команда</th>
    <th>Действие</th>
  </tr>
  <tr>
    <td>M-C-\</td>
    <td>indent-region</td>
    <td>Отформатировать выделенную область, выровняв отступы по первой строке</td>
  </tr>
  <tr>
    <td>M-m</td>
    <td>back-to-indentation</td>
    <td>Переход (курсора) к первому символу в строке</td>
  </tr>
  <tr>
    <td>M-^</td>
    <td>delete-indentation</td>
    <td>Объединяет текущую строку с предыдущей</td>
  </tr>
  <tr>
    <td>M-C-o</td>
    <td>split-line</td>
    <td>Разорвать строку на курсоре; отступ для продолжения строки определяется положением курсора</td>
  </tr>
  <tr>
    <td>(нет)</td>
    <td>fill-individual-paragraphs</td>
    <td>Переформатировать абзацы с отступами, сохранив отступы</td>
  </tr>
</table>

Команды центрирования

<table>
  <tr>
    <th>Комбинация</th>
    <th>Команда</th>
    <th>Действие</th>
  </tr>
  <tr>
    <td>(нет)</td>
    <td>center-line</td>
    <td>Центрировать текущую строку</td>
  </tr>
  <tr>
    <td>(нет)</td>
    <td>center-paragraph</td>
    <td>Центрировать текущий абзац</td>
  </tr>
  <tr>
    <td>(нет)</td>
    <td>center-region</td>
    <td>Центрировать выделенную область</td>
  </tr>
</table>

Макрокоманды

<table>
  <tr>
    <th>Комбинация</th>
    <th>Команда</th>
    <th>Действие</th>
  </tr>
  <tr>
    <td>C-x (</td>
    <td>start-kbd-macro</td>
    <td>Начать определение макрокоманды</td>
  </tr>
  <tr>
    <td>C-x )</td>
    <td>end-kbd-macro</td>
    <td>Закончить определение макрокоманды</td>
  </tr>
  <tr>
    <td>C-x e</td>
    <td>call-last-kbd-macro</td>
    <td>Выполнить последнюю из определенных макрокоманд</td>
  </tr>
  <tr>
    <td>M-n C-x e</td>
    <td>digit-argument и call-last-kbd-macro</td>
    <td>Выполнить последнюю из определенных макрокоманд n раз</td>
  </tr>
  <tr>
    <td>C-u C-x (</td>
    <td>start-kbd-macro</td>
    <td>Выполнить последнюю из определенных макрокоманд и добавить в нее нажатия клавиш</td>
  </tr>
  <tr>
    <td>(нет)</td>
    <td>name-last-kbd-macro</td>
    <td>Дать имя последней определенной макрокоманде (перед сохранением)</td>
  </tr>
  <tr>
    <td>(нет)</td>
    <td>insert-last-keyboard-macro</td>
    <td>Добавить определенную макрокоманду в файл</td>
  </tr>
  <tr>
    <td>(нет)</td>
    <td>load-file</td>
    <td>Прочитать ранее созданный файл макрокоманд</td>
  </tr>
  <tr>
    <td>(нет)</td>
    <td><i>macroname</i></td>
    <td>Выполнить ранее сохраненную клавиатурную макрокоманду</td>
  </tr>
</table>