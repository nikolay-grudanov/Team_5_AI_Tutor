---
source_image: page_686.png
page_number: 686
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 27.77
tokens: 11727
characters: 1537
timestamp: 2025-12-24T03:46:04.952865
finish_reason: stop
---

<table>
  <tr>
    <th>[address] a[!]<br>text<br>.</th>
    <th>append</th>
  </tr>
  <tr>
    <td>Добавить текст (text) по заданному адресу (address) или по текущему адресу, если этот параметр опущен. Символ ! является переключателем автоматического отступа (autoindent). Так, если автоматический отступ был включен, использование ! отключит его на время работы команды. Ввод завершается при получении строки, содержащей единственный символ — точку.</td>
    <td></td>
  </tr>
  <tr>
    <th>ar</th>
    <th>args</th>
  </tr>
  <tr>
    <td>Перечислить аргументы файловых имен (список файлов для редактирования). Имя текущего файла заключается в квадратные скобки ([]).</td>
    <td></td>
  </tr>
  <tr>
    <th>cd dir<br>chdir dir</th>
    <th>cd</th>
  </tr>
  <tr>
    <td>Сменить текущий каталог внутри редактора.</td>
    <td></td>
  </tr>
  <tr>
    <th>[address] c[!]<br>text<br>.</th>
    <th>change</th>
  </tr>
  <tr>
    <td>Заменить указанные строки текстом text. Символ ! является переключателем autoindent на время работы команды. Ввод завершается при получении строки, содержащей единственный символ — точку.</td>
    <td></td>
  </tr>
  <tr>
    <th>[address] co destination</th>
    <th>copy</th>
  </tr>
  <tr>
    <td>Копировать строки, определяемые адресом address в указанный адрес destination. Команда t работает идентично copy.</td>
    <td></td>
  </tr>
  <tr>
    <th>Пример</th>
    <th></th>
  </tr>
  <tr>
    <td>:1,10 со 50    Скопировать первые 10 строк после строки 50</td>
    <td></td>
  </tr>
</table>