---
source_image: page_184.png
page_number: 184
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 55.44
tokens: 11831
characters: 1744
timestamp: 2025-12-24T03:23:41.615199
finish_reason: stop
---

<table>
  <tr>
    <th>–m size</th>
    <td>Указать максимальный размер сегмента данных.</td>
  </tr>
  <tr>
    <th>–n</th>
    <td>Запретить редактирование таблицы ретрансляции ядра.</td>
  </tr>
  <tr>
    <th>–q</th>
    <td>Тихий режим. Предупреждения не выводятся, сообщения об ошибках направляются в syslogd, а не в стандартный поток ошибок.</td>
  </tr>
  <tr>
    <th>–s size</th>
    <td>Указать максимальный размер стека.</td>
  </tr>
  <tr>
    <th>–t seconds</th>
    <td>Выждать указанное количество секунд (по умолчанию равно 10). Время отводится на завершение операций gated при запуске и останове.</td>
  </tr>
  <tr>
    <th colspan="2">Команды</th>
  </tr>
  <tr>
    <th>BACKOUT</th>
    <td>Восстановить файл /etc/gated.conf из файла /etc/gated.conf−, независимо от того, существует ли последний.</td>
  </tr>
  <tr>
    <th>backout</th>
    <td>Восстановить файл /etc/gated.conf из файла /etc/gated.conf−, предполагая, что последний существует.</td>
  </tr>
  <tr>
    <th>checkconf</th>
    <td>Сообщить о любых синтаксических ошибках в файле /etc/gated.conf.</td>
  </tr>
  <tr>
    <th>checknew</th>
    <td>Сообщить о любых синтаксических ошибках в файле /etc/gated.conf+.</td>
  </tr>
  <tr>
    <th>COREDUMP</th>
    <td>Принудительно создать файл образа памяти и завершить работу.</td>
  </tr>
  <tr>
    <th>createconf</th>
    <td>Создать пустой файл /etc/gated.conf+, если таковой еще не существует, и установить права доступа в 664 с владельцем root и группой gdmaint.</td>
  </tr>
  <tr>
    <th>dump</th>
    <td>Принудительный сброс данных в файл /usr/tmp/gated_dump и продолжение нормальной работы.</td>
  </tr>
  <tr>
    <th>interface</th>
    <td>Перезагрузить настройки интерфейса.</td>
  </tr>
</table>