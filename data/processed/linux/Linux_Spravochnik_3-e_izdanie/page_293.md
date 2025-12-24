---
source_image: page_293.png
page_number: 293
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 45.01
tokens: 11803
characters: 1817
timestamp: 2025-12-24T03:28:26.933258
finish_reason: stop
---

<table>
  <tr>
    <th>make</th>
    <td>
      <b>$\$(patsubst\ pattern,\ to,\ string)$</b><br>
      Аналогично <i>subst</i>, но считать символ % внутри шаблона <i>pattern</i> метасимволом. Заменяет каждое соответствие шаблону в строке <i>string</i> на <i>to</i>.

      <b>$\$(strip\ string)$</b><br>
      Удалить все лишние пробелы.

      <b>$\$(findstring\ substring,\ mainstring)$</b><br>
      Вернуть подстроку <i>substring</i>, если она найдена в строке <i>mainstring</i>, иначе вернуть нуль.

      <b>$\$(filter\ pattern,\ string)$</b><br>
      Вернуть те слова из строки <i>string</i>, которые соответствуют хотя бы одному слову шаблона <i>pattern</i>. Шаблоны могут включать символ маски %.

      <b>$\$(filter-out\ pattern,\ string)$</b><br>
      Удалить из строки <i>string</i> слова, которые соответствуют хотя бы одному слову шаблона <i>pattern</i>. Шаблоны могут включать символ маски %.

      <b>$\$(sort\ list)$</b><br>
      Вернуть список <i>list</i>, отсортированный в лексикографическом порядке.

      <b>$\$(dir\ list)$</b><br>
      Вернуть имена каталогов (все символы до последнего слэша) всех имен файлов из списка <i>list</i>.

      <b>$\$(notdir\ list)$</b><br>
      Вернуть все имена файлов (символы после последнего слэша) из списка <i>list</i>.

      <b>$\$(suffix\ list)$</b><br>
      Вернуть суффиксы имен (символы после последней точки) из списка <i>list</i>.

      <b>$\$(basename\ list)$</b><br>
      Для каждого элемента списка (имен файлов) вернуть подстроку до суффикса (все символы до последней точки).

      <b>$\$(addsuffix\ suffix,\ list)$</b><br>
      Вернуть список имен файлов, добавив к каждому имени суффикс.

      <b>$\$(addprefix\ prefix,\ list)$</b><br>
      Вернуть список имен файлов, добавив к каждому имени префикс.
    </td>
  </tr>
</table>