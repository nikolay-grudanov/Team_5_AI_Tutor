---
source_image: page_296.png
page_number: 296
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 61.17
tokens: 11932
characters: 2107
timestamp: 2025-12-24T03:28:55.125160
finish_reason: stop
---

<table>
  <tr>
    <th>–i ур_input_file</th>
    <td>Создать специальную запись с ключом ур_input_file.</td>
    <th>makedbm</th>
  </tr>
  <tr>
    <th>–l</th>
    <td>Преобразовать ключи указанной карты в нижний регистр.</td>
    <td></td>
  </tr>
  <tr>
    <th>–m ур_master_name</th>
    <td>Создать специальную запись с ключом ур_master_name.<br>Если не задано имя узла-хозяина, установить ключ в локальное имя узла.</td>
    <td></td>
  </tr>
  <tr>
    <th>–o ур_output_file</th>
    <td>Создать специальную запись с ключом ур_output_file.</td>
    <td></td>
  </tr>
  <tr>
    <th>–s</th>
    <td>Безопасная карта. Устанавливать соединения только с авторизованными NIS-сетями.</td>
    <td></td>
  </tr>
  <tr>
    <th>–u dbm filename</th>
    <td>Обратить dbm-файл: распечатать построчно базу данных, отделяя ключи от значений пробелом.</td>
    <td></td>
  </tr>
  <tr>
    <th colspan="3">Пример</th>
  </tr>
  <tr>
    <td colspan="3">Несложно создать сценарий интерпретатора для преобразования стандартных файлов (например, /etc/passwd) в формат ключ-значение, используемый makedbm. Например, следующая программа на awk:</td>
  </tr>
  <tr>
    <td colspan="3">
      BEGIN { FS=":"; OFS = "\t"; }<br>
      { print $1, $0}
    </td>
  </tr>
  <tr>
    <td colspan="3">преобразует /etc/passwd в исходный файл для makedbm, после чего можно создать NIS-файл passwd.byname. То есть ключом является имя пользователя, а значением — остаток строки из файла /etc/passwd.</td>
  </tr>
  <tr>
    <th>makemap [options] type name</th>
    <td>Команда системного администрирования. Переход от стандартного ввода к базам данных sendmail. Исходные данные должны быть представлены в виде:</td>
    <th>makemap</th>
  </tr>
  <tr>
    <td colspan="3"><i>key value</i></td>
  </tr>
  <tr>
    <td colspan="3">Строки комментариев начинаются с символа #; можно производить подстановку параметров по %n, а собственно символ % необходимо экранировать (% %). Аргумент type может принимать значения dbm, btree или hash, а name — это имя файла, к которому makemap добавляет стандартные суффиксы.</td>
  </tr>
</table>