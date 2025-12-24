---
source_image: page_243.png
page_number: 243
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 29.38
tokens: 7599
characters: 1761
timestamp: 2025-12-24T02:46:41.520894
finish_reason: stop
---

Out[195]:
Dave    (dave, google, com)
Steve   (steve, gmail, com)
Rob     (rob, gmail, com)
Wes     NaN
dtype: object

In [196]: matches.str.get(1)
Out[196]:
Dave    google
Steve   gmail
Rob     gmail
Wes     NaN
dtype: object

Аналогичный синтаксис позволяет вырезать строки:

In [197]: data.str[:5]
Out[197]:
Dave    dave@
Steve   steve
Rob     rob@g
Wes     NaN
dtype: object

Метод str.extract возвращает запомненные группы регулярного выражения в виде объекта DataFrame:

In [198]: data.str.extract(pattern, flags=re.IGNORECASE)
Out[198]:
      0    1    2
Dave  dave  google  com
Steve  steve  gmail  com
Rob   rob   gmail  com
Wes   NaN   NaN   NaN

В табл. 7.6 перечислены дополнительные методы строк в pandas.

Таблица 7.6. Неполный перечень векторных методов строковых объектов

<table>
  <tr>
    <th>Метод</th>
    <th>Описание</th>
  </tr>
  <tr>
    <td>cat</td>
    <td>Поэлементно конкатенирует строки с необязательным разделителем</td>
  </tr>
  <tr>
    <td>contains</td>
    <td>Возвращает булев массив, показывающий, содержит ли каждая строка указанный образец</td>
  </tr>
  <tr>
    <td>count</td>
    <td>Подсчитывает количество вхождений образца</td>
  </tr>
  <tr>
    <td>extract</td>
    <td>Использует регулярное выражение с группами, чтобы выделить одну или несколько строк из объекта Series, содержащего строки; результатом является DataFrame, содержащий по одному столбцу на каждую группу</td>
  </tr>
  <tr>
    <td>endswith</td>
    <td>Эквивалентно x.endswith(pattern) для каждого элемента</td>
  </tr>
  <tr>
    <td>startswith</td>
    <td>Эквивалентно x.startswith(pattern) для каждого элемента</td>
  </tr>
  <tr>
    <td>findall</td>
    <td>Возвращает список всех вхождений образца для каждой строки</td>
  </tr>
</table>