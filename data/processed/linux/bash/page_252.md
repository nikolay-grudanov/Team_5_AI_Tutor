---
source_image: page_252.png
page_number: 252
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 7.56
tokens: 7356
characters: 1284
timestamp: 2025-12-23T23:11:19.188896
finish_reason: stop
---

С помощью команды getfacl можно проверить, что список управления доступом был изменен:

$ getfacl report.txt

# файл: report.txt
# владелец: fsmith
# группа: accounting
user::rwx
user:djones:rwx
group::rw-
mask::rwx
other:r-x

Для удаления записи ACL добавьте опцию -x:

setfacl -x u:djones report.txt

Права доступа к файлам Windows

Команда icacls в среде Windows может использоваться для просмотра полномочий и списков управления доступом к файлу/каталогу и управления ими. Чтобы просмотреть текущие права доступа к файлу report.txt, выполните следующие действия:

$ icacls report.txt

report.txt NT AUTHORITY\SYSTEM:(F)
    BUILTIN\Administrators:(F)

Successfully processed 1 files; Failed processing 0 files

В табл. 17.1 перечислены пять простых полномочий для файлов, используемые в Windows.

Таблица 17.1. Простые полномочия доступа к файлам Windows

<table>
  <tr>
    <th>Полномочия</th>
    <th>Значение</th>
  </tr>
  <tr>
    <td>F</td>
    <td>Максимальные (Full)</td>
  </tr>
  <tr>
    <td>M</td>
    <td>Изменение (Modify)</td>
  </tr>
  <tr>
    <td>RX</td>
    <td>Чтение и выполнение (Read and execute)</td>
  </tr>
  <tr>
    <td>R</td>
    <td>Только чтение (Read only)</td>
  </tr>
  <tr>
    <td>W</td>
    <td>Только запись (Write only)</td>
  </tr>
</table>