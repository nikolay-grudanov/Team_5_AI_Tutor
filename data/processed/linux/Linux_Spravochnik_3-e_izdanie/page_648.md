---
source_image: page_648.png
page_number: 648
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 66.05
tokens: 12421
characters: 3030
timestamp: 2025-12-24T03:44:52.096434
finish_reason: stop
---

Конспект команд по группам

<table>
  <tr>
    <th>Комбинация</th>
    <th>Команда</th>
    <th>Действие</th>
  </tr>
  <tr>
    <td>C-a</td>
    <td>beginning-of-line</td>
    <td>Переход к началу строки</td>
  </tr>
  <tr>
    <td>C-e</td>
    <td>end-of-line</td>
    <td>Переход к концу строки</td>
  </tr>
  <tr>
    <td>M-a</td>
    <td>backward-sentence</td>
    <td>Переход к предыдущему предложению</td>
  </tr>
  <tr>
    <td>M-e</td>
    <td>forward-sentence</td>
    <td>Переход к следующему предложению</td>
  </tr>
  <tr>
    <td>M-{</td>
    <td>backward-paragraph</td>
    <td>Переход к предыдущему абзацу</td>
  </tr>
  <tr>
    <td>M-}</td>
    <td>forward-paragraph</td>
    <td>Переход к следующему абзацу</td>
  </tr>
  <tr>
    <td>C-v</td>
    <td>scroll-up</td>
    <td>Переход к следующей экранной странице</td>
  </tr>
  <tr>
    <td>M-v</td>
    <td>scroll-down</td>
    <td>Переход к предыдущей экранной странице</td>
  </tr>
  <tr>
    <td>C-x [</td>
    <td>backward-page</td>
    <td>Переход к предыдущей странице текста</td>
  </tr>
  <tr>
    <td>C-x ]</td>
    <td>forward-page</td>
    <td>Переход к следующей странице текста</td>
  </tr>
  <tr>
    <td>M-></td>
    <td>end-of-buffer</td>
    <td>Переход к концу текста</td>
  </tr>
  <tr>
    <td>M-<</td>
    <td>beginning-of-buffer</td>
    <td>Переход к началу текста</td>
  </tr>
  <tr>
    <td>(нет)</td>
    <td>goto-line</td>
    <td>Перейти к строке n файла</td>
  </tr>
  <tr>
    <td>(нет)</td>
    <td>goto-char</td>
    <td>Перейти к символу n файла</td>
  </tr>
  <tr>
    <td>C-l</td>
    <td>recenter</td>
    <td>Обновить окно с текстом так, чтобы текущая строка с курсором оказалась в центре окна</td>
  </tr>
  <tr>
    <td>M-n</td>
    <td>digit-argument</td>
    <td>Повторить следующую команду n раз</td>
  </tr>
  <tr>
    <td>C-u n</td>
    <td>universal-argument</td>
    <td>Повторить следующую команду n раз</td>
  </tr>
</table>

Команды удаления

<table>
  <tr>
    <th>Комбинация</th>
    <th>Команда</th>
    <th>Действие</th>
  </tr>
  <tr>
    <td>Del</td>
    <td>backward-delete-char</td>
    <td>Удаление символа перед курсором</td>
  </tr>
  <tr>
    <td>C-d</td>
    <td>delete-char</td>
    <td>Удаление символа под курсором</td>
  </tr>
  <tr>
    <td>M-Del</td>
    <td>backward-kill-word</td>
    <td>Удаление предыдущего слова</td>
  </tr>
  <tr>
    <td>M-d</td>
    <td>kill-word</td>
    <td>Удаление слова под курсором</td>
  </tr>
  <tr>
    <td>C-k</td>
    <td>kill-line</td>
    <td>Удаление от курсора и до конца строки</td>
  </tr>
  <tr>
    <td>M-k</td>
    <td>kill-sentence</td>
    <td>Удаление предложения, на котором находится курсор</td>
  </tr>
  <tr>
    <td>C-x Del</td>
    <td>backward-kill-sentence</td>
    <td>Удаление предыдущего предложения</td>
  </tr>
  <tr>
    <td>C-y</td>
    <td>yank</td>
    <td>Возврат удаленного текста</td>
  </tr>
  <tr>
    <td>C-w</td>
    <td>kill-region</td>
    <td>Удаление выделенной области (см. следующую таблицу)</td>
  </tr>
</table>