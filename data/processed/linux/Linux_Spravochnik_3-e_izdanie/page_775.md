---
source_image: page_775.png
page_number: 775
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 44.97
tokens: 11807
characters: 1493
timestamp: 2025-12-24T03:50:24.784130
finish_reason: stop
---

Типы записей, перечисленные в табл. 14.25, генерируются командами update.

Таблица 14.25. Типы записей истории, связанные с работой update

<table>
  <tr>
    <th>Тип</th>
    <th>Описание</th>
  </tr>
  <tr>
    <td>C</td>
    <td>Слияние было необходимо, но выявлены конфликты, которые требуют вмешательства пользователя</td>
  </tr>
  <tr>
    <td>G</td>
    <td>Успешное автоматическое слияние</td>
  </tr>
  <tr>
    <td>U</td>
    <td>Рабочий файл скопирован из репозитория</td>
  </tr>
  <tr>
    <td>W</td>
    <td>Рабочая копия удалена</td>
  </tr>
</table>

Типы записей, перечисленные в табл. 14.26, генерируются командами commit.

Таблица 14.26. Типы записей истории, связанные с работой commit

<table>
  <tr>
    <th>Тип</th>
    <th>Описание</th>
  </tr>
  <tr>
    <td>A</td>
    <td>Первоначальное добавление</td>
  </tr>
  <tr>
    <td>M</td>
    <td>Файл изменен</td>
  </tr>
  <tr>
    <td>R</td>
    <td>Файл удален</td>
  </tr>
</table>

Типы записей, перечисленные в табл. 14.27, генерируются различными командами.

Таблица 14.27. Прочие типы записей в истории

<table>
  <tr>
    <th>Тип</th>
    <th>Команда</th>
  </tr>
  <tr>
    <td>E</td>
    <td>export</td>
  </tr>
  <tr>
    <td>F</td>
    <td>release</td>
  </tr>
  <tr>
    <td>O</td>
    <td>checkout</td>
  </tr>
  <tr>
    <td>T</td>
    <td>rtag</td>
  </tr>
</table>

import

import
  [ -b branch ]
  [ -d ]
  [ -I pattern ]
  [ -k kflag ]
  [ -m message ]
  [ -W spec ]
module
vendor_tag
release_tag ...