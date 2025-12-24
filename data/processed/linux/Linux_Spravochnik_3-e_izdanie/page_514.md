---
source_image: page_514.png
page_number: 514
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 62.66
tokens: 11951
characters: 2076
timestamp: 2025-12-24T03:38:44.311468
finish_reason: stop
---

<table>
  <tr>
    <th>—d [packages], —–discard [packages]</th>
    <td>Удалить секции из очереди автоматической сборки. Если указаны какие-либо пакеты, удалить только секции, принадлежащие этим пакетам. В противном случае очередь очищается полностью.</td>
    <th>dpkg-split</th>
  </tr>
  <tr>
    <th>—I parts, —–info parts</th>
    <td>Отобразить информацию об указанной секции или секциях.</td>
    <td></td>
  </tr>
  <tr>
    <th>—j parts, —–join parts</th>
    <td>Объединить указанные секции файла пакета. По умолчанию создается пакет с именем вида package-version.deb.</td>
    <td></td>
  </tr>
  <tr>
    <th>—l, —–listq</th>
    <td>Отобразить содержимое очереди секций, ожидающих сборки, приведя имя пакета, секции пакета, находящиеся в очереди, и их объем в байтах.</td>
    <td></td>
  </tr>
  <tr>
    <th>—s full-package [prefix], —–full-package [prefix]</th>
    <td>Разделить указанный пакет full-package на секции, имеющиеся в формате prefixNofM.deb. По умолчанию префикс принимает значение имени пакета без расширения .deb.</td>
    <td></td>
  </tr>
  <tr>
    <th>—h, —–help</th>
    <td>Отобразить справку и завершить работу.</td>
    <td></td>
  </tr>
  <tr>
    <th>—license</th>
    <td>Отобразить информацию о лицензировании dpkg-split и завершить работу. Написание —–licence также считается верным и приводит к тому же результату.</td>
    <td></td>
  </tr>
  <tr>
    <th>—version</th>
    <td>Отобразить информацию о версии dpkg-split и завершить работу.</td>
    <td></td>
  </tr>
  <tr>
    <th>Параметры</th>
    <td colspan="2"></td>
  </tr>
  <tr>
    <th>—depotdir</th>
    <td>Указать альтернативный каталог depotdir, в котором хранятся секции в ожидании сборки. По умолчанию используется каталог /var/lib/dpkg.</td>
    <td></td>
  </tr>
  <tr>
    <th>—msdos</th>
    <td>Использовать MS-DOS-совместимые имена секций.</td>
    <td></td>
  </tr>
  <tr>
    <th>—Q, —–noquiet</th>
    <td>Не выводить сообщение об ошибке, если в очереди сборки присутствует секция, не принадлежащая собираемому пакету.</td>
    <td></td>
  </tr>
</table>