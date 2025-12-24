---
source_image: page_154.png
page_number: 154
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 12.88
tokens: 7622
characters: 1937
timestamp: 2025-12-23T23:07:39.385488
finish_reason: stop
---

Планирование задачи в Linux

Чтобы запланировать выполнение задачи в Linux, сначала нужно перечислить все существующие файлы cron:

$ crontab -l

no crontab for paul

Как вы можете убедиться, файла cron пока не существует. Для создания и редактирования нового файла cron укажите параметр -e:

$ crontab -e

no crontab for paul - using an empty one
Select an editor. To change later, run 'select-editor'.
  1. /bin/ed
  2. /bin/nano        <---- easiest
  3. /usr/bin/vim.basic
  4. /usr/bin/vim.tiny
Choose 1-4 [2]:

В любом редакторе добавьте в файл cron следующую строку, чтобы сценарий autoscan.sh запускался в 08:00 утра каждый день:

0 8 * * * /home/paul/autoscan.sh

Первые пять элементов определяют дату и время, когда будет выполняться задача, а шестой элемент — это команда или файл, которые должны быть выполнены.
В табл. 9.1 описаны поля файла cron и их допустимые значения.

Для выполнения сценария autoscan.sh в качестве команды (вместо использования bash auto scan.sh) необходимо предоставить ему соответствующие полномочия. Например, с помощью строки chmod 750/home/paul/autoscan.sh владельцу файла (возможно, Paul) предоставляются права на чтение, запись и выполнение, а также разрешение на чтение и выполнение для группы и никаких других разрешений.

Таблица 9.1. Поля файла cron

<table>
  <tr>
    <th>Поле</th>
    <th>Разрешенные значения</th>
    <th>Пример</th>
    <th>Значение</th>
  </tr>
  <tr>
    <td>Минута</td>
    <td>0–59</td>
    <td>0</td>
    <td>00 минут</td>
  </tr>
  <tr>
    <td>Час</td>
    <td>0–23</td>
    <td>8</td>
    <td>8 часов</td>
  </tr>
  <tr>
    <td>День месяца</td>
    <td>1–31</td>
    <td>*</td>
    <td>Любой день</td>
  </tr>
  <tr>
    <td>Месяц</td>
    <td>1–12, January — December, Jan — Dec</td>
    <td>Mar</td>
    <td>Март</td>
  </tr>
  <tr>
    <td>День недели</td>
    <td>1–7, Monday — Sunday, Mon–Sun</td>
    <td>1</td>
    <td>Понедельник</td>
  </tr>
</table>