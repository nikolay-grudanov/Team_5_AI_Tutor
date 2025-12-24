---
source_image: page_166.png
page_number: 166
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 55.94
tokens: 11831
characters: 1905
timestamp: 2025-12-24T03:22:53.761593
finish_reason: stop
---

<table>
  <tr>
    <th>prompt</th>
    <td>Переключение диалогового режима работы.</td>
    <th>ftp</th>
  </tr>
  <tr>
    <th>proxy ftp-command</th>
    <td>Выполнить команду FTP через второе контрольное соединение. Например, одновременно послать команду двум различным удаленным узлам.</td>
    <th></th>
  </tr>
  <tr>
    <th>put local-file [remote-file]</th>
    <td>Передать файл (local-file) на удаленную машину. Если имя конечного файла (remote-file) не задано, то в качестве такого имени используется исходное имя файла, обработанное в соответствии с установками ntrans и nmap. При передаче файла действуют текущие настройки типа, файла, структуры и режима передачи.</td>
    <th></th>
  </tr>
  <tr>
    <th>pwd</th>
    <td>Отобразить имя текущего рабочего каталога на удаленной машине.</td>
    <th></th>
  </tr>
  <tr>
    <th>quit</th>
    <td>Синоним bye.</td>
    <th></th>
  </tr>
  <tr>
    <th>quote arg1 arg2...</th>
    <td>Послать перечисленные команды удаленному FTP-серверу.</td>
    <th></th>
  </tr>
  <tr>
    <th>recv remote-file [local-file]</th>
    <td>Синоним get.</td>
    <th></th>
  </tr>
  <tr>
    <th>reget remote-file [local-file]</th>
    <td>Получить файл (аналогично get). При указании имени локального файла (local-file) производится «докачка» (команду удобно использовать при обрыве связи или временном рассоединении).</td>
    <th></th>
  </tr>
  <tr>
    <th>remotehelp [command-name]</th>
    <td>Запросить справку по существующим командам с удаленного FTP-сервера либо справку по указанной команде command-name.</td>
    <th></th>
  </tr>
  <tr>
    <th>remotestatus [filename]</th>
    <td>Отобразить состояние удаленного узла или файла на удаленном узле, если указано имя файла (filename).</td>
    <th></th>
  </tr>
  <tr>
    <th>rename [from] [to]</th>
    <td>Переименовать файл from на удаленной машине в файл to.</td>
    <th></th>
  </tr>
</table>