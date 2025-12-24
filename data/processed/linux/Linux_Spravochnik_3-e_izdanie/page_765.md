---
source_image: page_765.png
page_number: 765
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 74.72
tokens: 12230
characters: 2478
timestamp: 2025-12-24T03:50:20.566666
finish_reason: stop
---

Таблица 14.18 (продолжение)

<table>
  <tr>
    <th>Команда</th>
    <th>-D</th>
    <th>-f</th>
    <th>-k</th>
    <th>-l</th>
    <th>-n</th>
    <th>-R</th>
    <th>-r</th>
  </tr>
  <tr>
    <td>logout</td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>rdiff</td>
    <td>•</td>
    <td>•</td>
    <td></td>
    <td>•</td>
    <td></td>
    <td>•</td>
    <td>•</td>
  </tr>
  <tr>
    <td>release</td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>remove</td>
    <td></td>
    <td></td>
    <td></td>
    <td>•</td>
    <td></td>
    <td>•</td>
    <td></td>
  </tr>
  <tr>
    <td>rtag</td>
    <td>•</td>
    <td>•</td>
    <td></td>
    <td>•</td>
    <td></td>
    <td>•</td>
    <td>•</td>
  </tr>
  <tr>
    <td>status</td>
    <td></td>
    <td></td>
    <td></td>
    <td>•</td>
    <td></td>
    <td>•</td>
    <td></td>
  </tr>
  <tr>
    <td>tag</td>
    <td></td>
    <td></td>
    <td></td>
    <td>•</td>
    <td></td>
    <td>•</td>
    <td></td>
  </tr>
  <tr>
    <td>unedit</td>
    <td></td>
    <td></td>
    <td></td>
    <td>•</td>
    <td></td>
    <td>•</td>
    <td></td>
  </tr>
  <tr>
    <td>update</td>
    <td>•</td>
    <td>•</td>
    <td>•</td>
    <td>•</td>
    <td></td>
    <td>•</td>
    <td>•</td>
  </tr>
  <tr>
    <td>watch</td>
    <td></td>
    <td></td>
    <td></td>
    <td>•</td>
    <td></td>
    <td>•</td>
    <td></td>
  </tr>
  <tr>
    <td>watchers</td>
    <td></td>
    <td></td>
    <td></td>
    <td>•</td>
    <td></td>
    <td>•</td>
    <td></td>
  </tr>
</table>

Форматы дат

CVS позволяет использовать самые различные форматы задания дат, среди которых:

Стандарт ISO
Предпочтительно задание дат в виде YYYY-MM-DD HH:MM, который будет выглядеть как 2000-05-17 или 2000-05-17 22:00. Технические детали использования формата определяются стандартом ISO 8601.

Стандарт Email
17 May 2000. Технические детали использования формата определяются стандартами RFC 822 и RFC 1123.

Относительный
10 days ago, 4 years ago (10 дней назад, 4 года назад).

Общий
month/day/year. Этот формат может вызывать путаницу, поскольку в различных странах используется различный порядок следования первых двух полей (дата 1/2/2000 является двусмысленной).

Другие
Другие форматы также допустимы, в частности YYYY/MM/DD и форматы без указания года (год принимает значение текущего).