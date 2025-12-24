---
source_image: page_658.png
page_number: 658
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 64.06
tokens: 12313
characters: 2806
timestamp: 2025-12-24T03:45:22.600689
finish_reason: stop
---

Конспект команд Emacs по клавишам

<table>
  <tr>
    <th>Комбинация</th>
    <th>Команда</th>
    <th>Действие</th>
  </tr>
  <tr>
    <td>C-x C-s</td>
    <td>save-buffer</td>
    <td>Сохранить файл (при блокировании терминала нажать клавиши <Ctrl>+<q> для перезапуска)</td>
  </tr>
  <tr>
    <td>C-x C-t</td>
    <td>transpose-lines</td>
    <td>Перестановка пары строк</td>
  </tr>
  <tr>
    <td>C-x C-u</td>
    <td>upcase-region</td>
    <td>Сделать прописными все буквы в выделенной области</td>
  </tr>
  <tr>
    <td>C-x C-v</td>
    <td>find-alternate-file</td>
    <td>Чтение другого файла; файл заменяет прочитанный по C-x C-f</td>
  </tr>
  <tr>
    <td>C-x C-w</td>
    <td>write-file</td>
    <td>Записать содержимое буфера в файл</td>
  </tr>
  <tr>
    <td>C-x C-x</td>
    <td>exchange-point-and-mark</td>
    <td>Обменять местами курсор и отметку</td>
  </tr>
  <tr>
    <td>C-x Del</td>
    <td>backward-kill-sentence</td>
    <td>Удаление предыдущего предложения</td>
  </tr>
  <tr>
    <td>C-x e</td>
    <td>call-last-kbd-macro</td>
    <td>Выполнить последнюю из определенных макрокоманд</td>
  </tr>
  <tr>
    <td>C-x h</td>
    <td>mark-whole-buffer</td>
    <td>Выделить буфер</td>
  </tr>
  <tr>
    <td>C-x i</td>
    <td>insert-file</td>
    <td>Вставить файл в текущей позиции курсора</td>
  </tr>
  <tr>
    <td>C-x k</td>
    <td>kill-buffer</td>
    <td>Удалить указанный буфер</td>
  </tr>
  <tr>
    <td>C-x o</td>
    <td>other-window</td>
    <td>Переход в соседнее окно</td>
  </tr>
  <tr>
    <td>C-x q</td>
    <td>kbd-macro-query</td>
    <td>Вставить запрос в определение макрокоманды</td>
  </tr>
  <tr>
    <td>C-x s</td>
    <td>save-some-buffers</td>
    <td>Подтверждение сохранения каждого из измененных буферов</td>
  </tr>
  <tr>
    <td>C-x u</td>
    <td>advertised-undo</td>
    <td>Многоуровневая отмена последнего редактирования</td>
  </tr>
  <tr>
    <td>C-y</td>
    <td>yank</td>
    <td>Возврат удаленного текста</td>
  </tr>
  <tr>
    <td>C-z</td>
    <td>suspend-emacs</td>
    <td>Приостановить выполнение Emacs (возврат по команде exit или fg)</td>
  </tr>
</table>

Комбинации с клавишей <Meta>

<table>
  <tr>
    <th>Комбинация</th>
    <th>Команда</th>
    <th>Действие</th>
  </tr>
  <tr>
    <td>M-- M-c</td>
    <td>negative-argument; capitalize-word</td>
    <td>Сделать прописной первую букву предыдущего слова</td>
  </tr>
  <tr>
    <td>M-- M-l&gt;</td>
    <td>negative-argument; downcase-word</td>
    <td>Сделать строчными все буквы предыдущего слова</td>
  </tr>
  <tr>
    <td>M-- M-u&gt;</td>
    <td>negative-argument; upcase-word</td>
    <td>Сделать прописными все буквы предыдущего слова</td>
  </tr>
  <tr>
    <td>M-$</td>
    <td>spell-word</td>
    <td>Проверить орфографию следующего слова</td>
  </tr>
</table>