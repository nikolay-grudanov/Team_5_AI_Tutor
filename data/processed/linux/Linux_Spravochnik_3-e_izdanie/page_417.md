---
source_image: page_417.png
page_number: 417
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 50.43
tokens: 11760
characters: 1803
timestamp: 2025-12-24T03:33:55.492971
finish_reason: stop
---

<table>
  <tr>
    <th>test</th>
    <td>
      <ul>
        <li><b>-eq</b> Числа равны.</li>
        <li><b>-ne</b> Числа не равны.</li>
        <li><b>-lt</b> integer1 меньше, чем integer2.</li>
        <li><b>-le</b> integer1 меньше либо равно integer2.</li>
        <li><b>-gt</b> integer1 больше, чем integer2.</li>
        <li><b>-ge</b> integer1 больше либо равно integer2.</li>
      </ul>
    </td>
  </tr>
  <tr>
    <th>tftp</th>
    <td>
      <b>tftp [host [port]]</b><br>
      Пользовательский интерфейс к протоколу TFTP (Trivial File Transfer Protocol), позволяющему передавать файлы между удаленными машинами. Может быть задан удаленный узел (<i>host</i>); в этом случае он становится узлом по умолчанию для последующих операций.<br>
      <b>Команды</b><br>
      При запуске tftp выдается приглашение:<br>
      <pre>tftp&gt;</pre>
      и воспринимаются следующие команды:
      <ul>
        <li><b>? [command-name...]</b><br>
          Вывести справочную информацию.</li>
        <li><b>ascii</b><br>
          Сокращение для перехода в режим ASCII (mode ASCII).</li>
        <li><b>binary</b><br>
          Сокращение для перехода в двоичный режим (mode binary).</li>
        <li><b>connect hostname [port]</b><br>
          Установить имя узла (<i>hostname</i>) и, при необходимости, порт для передачи файлов.</li>
        <li><b>get filename</b></li>
        <li><b>get remotename localname</b></li>
        <li><b>get filename1 filename2 filename3 ... filenameN</b><br>
          Получение файла или набора файлов из ранее указанного удаленного источника.</li>
        <li><b>mode transfer-mode</b><br>
          Установить режим передачи данных. Режим может иметь значение ASCII или binary (двоичный). По умолчанию принимается ASCII.</li>
      </ul>
    </td>
  </tr>
</table>