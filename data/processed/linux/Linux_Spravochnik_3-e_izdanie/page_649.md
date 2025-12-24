---
source_image: page_649.png
page_number: 649
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 55.74
tokens: 12288
characters: 2688
timestamp: 2025-12-24T03:44:41.767099
finish_reason: stop
---

<table>
  <tr>
    <th>Комбинация</th>
    <th>Команда</th>
    <th>Действие</th>
  </tr>
  <tr>
    <td>(нет)</td>
    <td>backward-kill-paragraph</td>
    <td>Удаление предыдущего абзаца</td>
  </tr>
  <tr>
    <td>(нет)</td>
    <td>kill-paragraph</td>
    <td>Удаление текста от курсора и до конца абзаца</td>
  </tr>
</table>

Абзацы и области текста

<table>
  <tr>
    <th>Комбинация</th>
    <th>Команда</th>
    <th>Действие</th>
  </tr>
  <tr>
    <td>C-@</td>
    <td>set-mark-command</td>
    <td>Отметить начало (или конец) области</td>
  </tr>
  <tr>
    <td>C-пробел</td>
    <td>set-mark-command</td>
    <td>Отметить начало (или конец) области</td>
  </tr>
  <tr>
    <td>C-x C-p</td>
    <td>mark-page</td>
    <td>Выделить страницу</td>
  </tr>
  <tr>
    <td>C-x C-x</td>
    <td>exchange-point-and-mark</td>
    <td>Обменять местами курсор и отметку</td>
  </tr>
  <tr>
    <td>C-x h</td>
    <td>mark-whole-buffer</td>
    <td>Выделить буфер</td>
  </tr>
  <tr>
    <td>M-q</td>
    <td>fill-paragraph</td>
    <td>Переформатировать абзац</td>
  </tr>
  <tr>
    <td>(нет)</td>
    <td>fill-region</td>
    <td>Переформатировать отдельные абзацы выделенной области</td>
  </tr>
  <tr>
    <td>M-h</td>
    <td>mark-paragraph</td>
    <td>Выделить абзац</td>
  </tr>
  <tr>
    <td>M-{</td>
    <td>backward-paragraph</td>
    <td>Перемещение к предыдущему абзацу</td>
  </tr>
  <tr>
    <td>M-}</td>
    <td>forward-paragraph</td>
    <td>Перемещение к следующему абзацу</td>
  </tr>
  <tr>
    <td>(нет)</td>
    <td>backward-kill-paragraph</td>
    <td>Удаление предыдущего абзаца</td>
  </tr>
  <tr>
    <td>(нет)</td>
    <td>kill-paragraph</td>
    <td>Удаление текста от курсора и до конца абзаца</td>
  </tr>
</table>

Прерывание и откат команд

<table>
  <tr>
    <th>Комбинация</th>
    <th>Команда</th>
    <th>Действие</th>
  </tr>
  <tr>
    <td>C-g</td>
    <td>keyboard-quit</td>
    <td>Прекратить набор команды</td>
  </tr>
  <tr>
    <td>C-x u</td>
    <td>advertised-undo</td>
    <td>Многоуровневая отмена последнего редактирования</td>
  </tr>
  <tr>
    <td>(нет)</td>
    <td>revert-buffer</td>
    <td>Восстановить редактируемый текст из сохраненного или автоматически сохраненного файла</td>
  </tr>
</table>

Команды перестановки

<table>
  <tr>
    <th>Комбинация</th>
    <th>Команда</th>
    <th>Действие</th>
  </tr>
  <tr>
    <td>C-t</td>
    <td>transpose-chars</td>
    <td>Перестановка (обмен местами) пары букв</td>
  </tr>
  <tr>
    <td>M-t</td>
    <td>transpose-words</td>
    <td>Перестановка пары слов</td>
  </tr>
  <tr>
    <td>C-x C-t</td>
    <td>transpose-lines</td>
    <td>Перестановка пары строк</td>
  </tr>
</table>