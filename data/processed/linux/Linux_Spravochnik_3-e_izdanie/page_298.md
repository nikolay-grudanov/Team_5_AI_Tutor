---
source_image: page_298.png
page_number: 298
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 52.16
tokens: 11901
characters: 1982
timestamp: 2025-12-24T03:28:51.827805
finish_reason: stop
---

<table>
  <tr>
    <th>–m systems, --systems=systems</th>
    <td>Искать в руководствах систем systems (перечисляются через запятую).</td>
    <td>man</td>
  </tr>
  <tr>
    <th>–p preprocessor, --preprocessor=preprocessor</th>
    <td>Предварительная обработка страниц руководств с помощью указанного препроцессора перед передачей их nroff, troff или groff. Всегда выполнять сначала команду soelim.</td>
    <td></td>
  </tr>
  <tr>
    <th>–r prompt, --prompt=prompt</th>
    <td>Установка приглашения для средства постраничного просмотра less.</td>
    <td></td>
  </tr>
  <tr>
    <th>–t, --troff</th>
    <td>Форматирование страниц руководства командой /usr/bin/groff -Tgv -mandoc. Подразумевается параметрами –T и –Z.</td>
    <td></td>
  </tr>
  <tr>
    <th>–u, --update</th>
    <td>Выполнять проверку непротиворечивости страниц, помещенных в кэш и реально существующих в системе.</td>
    <td></td>
  </tr>
  <tr>
    <th>–w, --where, --location</th>
    <td>Отображать пути файлов руководств на стандартный вывод.</td>
    <td></td>
  </tr>
  <tr>
    <th>–D, --default</th>
    <td>Использовать для всех параметров значения по умолчанию.</td>
    <td></td>
  </tr>
  <tr>
    <th>–L locale, --locale=locale</th>
    <td>Текущий набор параметров локализации имеет значение locale. Не вызывать функцию setlocale().</td>
    <td></td>
  </tr>
  <tr>
    <th>–M path, --manpath=path</th>
    <td>Искать страницы руководств в пути path. Игнорировать параметр –m.</td>
    <td></td>
  </tr>
  <tr>
    <th>–P pager, --pager=pager</th>
    <td>Предписание использовать программу постраничного просмотра pager.</td>
    <td></td>
  </tr>
  <tr>
    <th>–T device, --troff-device[=device]</th>
    <td>Форматирование groff или troff для вывода на устройство device, например dvi, latin1, X75 и X100.</td>
    <td></td>
  </tr>
  <tr>
    <th>–Z, --ditroff</th>
    <td>Запретить дополнительную обработку после завершения форматирования groff.</td>
    <td></td>
  </tr>
</table>