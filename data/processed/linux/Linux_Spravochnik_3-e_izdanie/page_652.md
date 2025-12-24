---
source_image: page_652.png
page_number: 652
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 61.17
tokens: 12349
characters: 2895
timestamp: 2025-12-24T03:44:59.215696
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
    <td>C-x 0</td>
    <td>delete-window</td>
    <td>Удалить текущее окно</td>
  </tr>
  <tr>
    <td>C-x 1</td>
    <td>delete-other-windows</td>
    <td>Удалить все окна кроме текущего</td>
  </tr>
  <tr>
    <td>(нет)</td>
    <td>delete-windows-on</td>
    <td>Удалить все окна определенного буфера</td>
  </tr>
  <tr>
    <td>C-x ^</td>
    <td>enlarge-window</td>
    <td>Увеличить высоту окна</td>
  </tr>
  <tr>
    <td>(нет)</td>
    <td>shrink-window</td>
    <td>Уменьшить высоту окна</td>
  </tr>
  <tr>
    <td>C-x }</td>
    <td>enlarge-window-horizontally</td>
    <td>Увеличить ширину окна</td>
  </tr>
  <tr>
    <td>C-x {</td>
    <td>shrink-window-horizontally</td>
    <td>Уменьшить ширину окна</td>
  </tr>
  <tr>
    <td>M-C-v</td>
    <td>scroll-other-window</td>
    <td>Прокрутка соседнего окна</td>
  </tr>
  <tr>
    <td>C-x 4 f</td>
    <td>find-file-other-window</td>
    <td>Поиск файла в соседнем окне</td>
  </tr>
  <tr>
    <td>C-x 4 b</td>
    <td>switch-to-buffer-other-window</td>
    <td>Выбрать буфер в соседнем окне</td>
  </tr>
  <tr>
    <td>C-x 5 f</td>
    <td>find-file-other-frame</td>
    <td>Поиск файла в новом фрейме</td>
  </tr>
  <tr>
    <td>C-x 5 b</td>
    <td>switch-to-buffer-other-frame</td>
    <td>Выбрать буфер в другом фрейме</td>
  </tr>
  <tr>
    <td>(нет)</td>
    <td>compare-windows</td>
    <td>Сравнить два буфера, отобразить различия</td>
  </tr>
</table>

Специальные символы режима командного интерпретатора

<table>
  <tr>
    <th>Комбинация</th>
    <th>Команда</th>
    <th>Действие</th>
  </tr>
  <tr>
    <td>C-c C-c</td>
    <td>interrupt-shell-subjob</td>
    <td>Принудительное завершение текущего задания</td>
  </tr>
  <tr>
    <td>C-c C-d</td>
    <td>shell-send-eof</td>
    <td>Символ конца файла</td>
  </tr>
  <tr>
    <td>C-c C-u</td>
    <td>kill-shell-input</td>
    <td>Удалить текущую строку</td>
  </tr>
  <tr>
    <td>C-c C-w</td>
    <td>backward-kill-word</td>
    <td>Удалить предыдущее слово</td>
  </tr>
  <tr>
    <td>C-c C-z</td>
    <td>stop-shell-subjob</td>
    <td>Приостановить текущее задание</td>
  </tr>
</table>

Команды отступа

<table>
  <tr>
    <th>Комбинация</th>
    <th>Команда</th>
    <th>Действие</th>
  </tr>
  <tr>
    <td>C-x .</td>
    <td>set-fill-prefix</td>
    <td>Предварить каждую строку абзаца символами от начала строки до положения курсора в строке; это можно отменить, выполнив команду с курсором в первом столбце</td>
  </tr>
  <tr>
    <td>(нет)</td>
    <td>indented-text-mode</td>
    <td>Основной режим: каждый табулятор увеличивает отступ для следующей строки</td>
  </tr>
  <tr>
    <td>(нет)</td>
    <td>text-mode</td>
    <td>Прекратить ввод текста в режиме отступов, вернуться в обычный текстовый режим</td>
  </tr>
</table>