---
source_image: page_190.png
page_number: 190
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 62.40
tokens: 11947
characters: 2012
timestamp: 2025-12-24T03:24:04.716917
finish_reason: stop
---

<table>
  <tr>
    <th>–n, ——line-number</th>
    <td>Отображать строки и номера строк.</td>
    <td>grep</td>
  </tr>
  <tr>
    <th>–q, ——quiet, ——silent</th>
    <td>Подавлять нормальный вывод, поиск прекращается по нахождению первой строки.</td>
    <td></td>
  </tr>
  <tr>
    <th>–r, ——recursive</th>
    <td>Рекурсивно обрабатывать файлы в каталогах. Идентично заданию –d recurse.</td>
    <td></td>
  </tr>
  <tr>
    <th>–s, ——no-messages</th>
    <td>Подавлять сообщения о ненайденных или недоступных файлах.</td>
    <td></td>
  </tr>
  <tr>
    <th>–v, ——revert-match</th>
    <td>Отображать все строки, которые не совпадают с шаблоном.</td>
    <td></td>
  </tr>
  <tr>
    <th>–w, ——word-regexp</th>
    <td>Искать только целые слова, совпадающие с шаблоном. Слова состоят из букв, цифр и символов подчеркивания, остальные символы являются разделителями слов.</td>
    <td></td>
  </tr>
  <tr>
    <th>–x, ——line-regexp</th>
    <td>Отображать строку только в том случае, если она целиком совпадает с шаблоном.</td>
    <td></td>
  </tr>
  <tr>
    <th>–A num, ——after-context=num</th>
    <td>Вывести num строк текста после найденной строки.</td>
    <td></td>
  </tr>
  <tr>
    <th>–B num, ——before-context=num</th>
    <td>Вывести num строк текста перед найденной строкой.</td>
    <td></td>
  </tr>
  <tr>
    <th>–C[num], ——context=[num], –num</th>
    <td>Отображать num строк, предшествующих найденной, и num строк, следующих за ней. По умолчанию объем контекста равен 2 строкам.</td>
    <td></td>
  </tr>
  <tr>
    <th>–L, ——files-without-match</th>
    <td>Перечислить имена файлов, поиск в которых не дал положительных результатов.</td>
    <td></td>
  </tr>
  <tr>
    <th>–V, ——version</th>
    <td>Отобразить номер версии и завершить работу.</td>
    <td></td>
  </tr>
  <tr>
    <th>Примеры</th>
    <td colspan="2"></td>
  </tr>
  <tr>
    <th>Перечислить пользователей, применяющих интерпретатор tcsh:</th>
    <td colspan="2">grep -c /bin/tcsh /etc/passwd</td>
  </tr>
</table>