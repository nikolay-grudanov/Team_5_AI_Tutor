---
source_image: page_164.png
page_number: 164
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 59.98
tokens: 11841
characters: 1978
timestamp: 2025-12-24T03:22:46.102202
finish_reason: stop
---

<table>
  <tr>
    <th>lcd [directory]</th>
    <td>Сменить текущий каталог на локальной машине. Если путь не указан, выполняется переход в домашний каталог пользователя.</td>
    <td>ftp</td>
  </tr>
  <tr>
    <th>ls [remote-directory][local-file]</th>
    <td>Отобразить содержимое каталогов на удаленной машине в формате, заданном удаленным ftp-узлом. Если не задан каталог (remote-directory), команда отображает содержание текущего рабочего каталога.</td>
    <td></td>
  </tr>
  <tr>
    <th>macdef macro-name</th>
    <td>Определить макрокоманду. Последующие вводимые строки сохраняются в макрокоманде macro-name; пустая строка завершает ввод. Если макрокоманда содержит $i, то выполняется последовательный перебор аргументов из списка. Символ $ необходимо экранировать символом «\».</td>
    <td></td>
  </tr>
  <tr>
    <th>mdelete remote-files</th>
    <td>Удалить указанные файлы (remote-files) на удаленной машине.</td>
    <td></td>
  </tr>
  <tr>
    <th>mdir remote-files local-files</th>
    <td>Аналог команды dir с возможностью задания списка файлов на удаленной машине.</td>
    <td></td>
  </tr>
  <tr>
    <th>mget remote-files</th>
    <td>Произвести расширение масок имен из remote-files на удаленной машине, а затем передать каждый из найденных файлов на локальную машину посредством команды get.</td>
    <td></td>
  </tr>
  <tr>
    <th>mkdir directory-name</th>
    <td>Создать каталог (directory-name) на удаленной машине.</td>
    <td></td>
  </tr>
  <tr>
    <th>mls remote-files local-file</th>
    <td>Аналог nlist с возможностью задания списка файлов на удаленной машине. Имя локального файла должно быть задано.</td>
    <td></td>
  </tr>
  <tr>
    <th>mode [mode-name]</th>
    <td>Установить режим передачи файлов. Режим передачи по умолчанию — stream (поток).</td>
    <td></td>
  </tr>
  <tr>
    <th>modtime [file-name]</th>
    <td>Отобразить время последнего редактирования файла на удаленной машине.</td>
    <td></td>
  </tr>
</table>