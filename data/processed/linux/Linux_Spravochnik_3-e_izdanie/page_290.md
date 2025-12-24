---
source_image: page_290.png
page_number: 290
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 55.51
tokens: 11923
characters: 2238
timestamp: 2025-12-24T03:28:36.775544
finish_reason: stop
---

<table>
  <tr>
    <th>—w, —print-directory</th>
    <td>Отображать имя текущего каталога до и после сборки.</td>
    <td>make</td>
  </tr>
  <tr>
    <th>--warn-undefined-variables</th>
    <td>Вывести предупреждение, если макрос используется без предварительного определения.</td>
    <td></td>
  </tr>
  <tr>
    <th>-C directory, --directory directory</th>
    <td>Перейти (cd) в каталог directory перед началом работы make. По следующим директивам -C будет совершаться переход (cd) в соответствующий каталог относительно текущего.</td>
    <td></td>
  </tr>
  <tr>
    <th>-I directory, --include-dir directory</th>
    <td>Включить указанный каталог в список каталогов, содержащих включаемые файлы.</td>
    <td></td>
  </tr>
  <tr>
    <th>-S, --no-keep-going, --stop</th>
    <td>Отменить действие предшествующего параметра -k. Применяется при рекурсивных сборках make.</td>
    <td></td>
  </tr>
  <tr>
    <th>-W file, --what-if file, --new-file file, --assume-new file</th>
    <td>Считать файл file недавно обновленным.</td>
    <td></td>
  </tr>
  <tr>
    <th colspan="3">Строки файла описаний</th>
  </tr>
  <tr>
    <td colspan="3">Инструкции в файле описаний интерпретируются построчно. Если размер инструкции превышает длину строки, укажите обратный слэш (\) в конце строки для продолжения инструкции на следующей строке. Файл описаний может содержать следующие типы строк:</td>
  </tr>
  <tr>
    <th>Пустые строки (blank lines)</th>
    <td>Пустые строки игнорируются.</td>
    <td></td>
  </tr>
  <tr>
    <th>Комментарии (comment lines)</th>
    <td>Все символы в строке после символа «#» считаются комментарием и игнорируются.</td>
    <td></td>
  </tr>
  <tr>
    <th>Описания зависимостей (dependency lines)</th>
    <td>В зависимости от выбранной цели выполняются соответствующие команды. Варианты записи:</td>
    <td></td>
  </tr>
  <tr>
    <td colspan="3">
      targets : dependencies<br>
      targets : dependencies ; command
    </td>
  </tr>
  <tr>
    <th colspan="3">Команды выполняются в том случае, когда файлы зависимостей (dependencies), имена которых могут являться масками, не существуют или являются более новыми, чем цель сборки. Если предварительные условия отсутствуют,</th>
  </tr>
</table>