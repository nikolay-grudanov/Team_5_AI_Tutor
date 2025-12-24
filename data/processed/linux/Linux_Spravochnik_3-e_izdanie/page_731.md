---
source_image: page_731.png
page_number: 731
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 31.68
tokens: 11707
characters: 1478
timestamp: 2025-12-24T03:48:12.020745
finish_reason: stop
---

<table>
  <tr>
    <th>system</th>
    <td><b>system (command)</b><br>Выполнить указанную команду в интерпретаторе и вернуть код завершения. Как правило, код завершения определяет результат работы программы: обычно 1 означает успешное завершение, 0 — простое завершение, а −1 — непредвиденный сбой. Вывод команды <i>command</i> не доступен для обработки в сценарии gawk.</td>
  </tr>
  <tr>
    <th>systime</th>
    <td><b>systime ()</b><br>Вернуть количество секунд, прошедших с полуночи первого января 1970 года по UTC.<br><b>Пример</b><br>Записать время начала и конца обработки данных программой:
      <pre>
BEGIN {
    now = systime()
    mesg = strftime("Started at %m/%d/%Y %H:%M:%S", now)
    print mesg
}
process data...
END {
    now = systime()
    mesg = strftime("Ended at %m/%d/%Y %H:%M:%S", now)
    print mesg
}
      </pre>
    </td>
  </tr>
  <tr>
    <th>tolower</th>
    <td><b>tolower (str)</b><br>Перевести все прописные символы строки <i>str</i> в нижний регистр и вернуть измененную строку.</td>
  </tr>
  <tr>
    <th>toupper</th>
    <td><b>toupper (str)</b><br>Перевести все строчные символы строки <i>str</i> в верхний регистр и вернуть измененную строку.</td>
  </tr>
  <tr>
    <th>while</th>
    <td><b>while (condition)<br>command</b><br>Выполнять команду <i>command</i>, пока истинно условие <i>condition</i> (допустимые условия см. в описании оператора if). Последовательность команд должна заключаться в фигурные скобки.</td>
  </tr>
</table>