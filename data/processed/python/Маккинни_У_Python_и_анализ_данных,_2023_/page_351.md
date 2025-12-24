---
source_image: page_351.png
page_number: 351
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 30.01
tokens: 7763
characters: 2274
timestamp: 2025-12-24T02:49:41.184553
finish_reason: stop
---

Таблица 10.2. Аргументы метода pivot_table

<table>
  <tr>
    <th>Параметр</th>
    <th>Описание</th>
  </tr>
  <tr>
    <td>values</td>
    <td>Имя (или имена) одного или нескольких столбцов, по которым производится агрегирование. По умолчанию агрегируются все числовые столбцы</td>
  </tr>
  <tr>
    <td>index</td>
    <td>Имена столбцов или другие групповые ключи для группировки по строкам результирующей сводной таблицы</td>
  </tr>
  <tr>
    <td>columns</td>
    <td>Имена столбцов или другие групповые ключи для группировки по столбцам результирующей сводной таблицы</td>
  </tr>
  <tr>
    <td>aggfunc</td>
    <td>Функция агрегирования или список таких функций; по умолчанию "mean". Можно задать произвольную функцию, допустимую в контексте groupby</td>
  </tr>
  <tr>
    <td>fill_value</td>
    <td>Чем заменять отсутствующие значения в результирующей таблице</td>
  </tr>
  <tr>
    <td>dropna</td>
    <td>Если True, не включать столбцы, в которых все значения отсутствуют</td>
  </tr>
  <tr>
    <td>margins</td>
    <td>Добавлять частичные итоги и общий итог по строкам и столбцам (по умолчанию False)</td>
  </tr>
  <tr>
    <td>margins_name</td>
    <td>Как назвать маргинальную строку (столбец), если передан параметр margins=True; по умолчанию "All"</td>
  </tr>
  <tr>
    <td>observed</td>
    <td>Только для категориальных групповых ключей: если True, показывать только наблюдаемые в ключах категории, в противном случае показывать все категории</td>
  </tr>
</table>

Перекрестная табуляция: crosstab
Перекрестная таблица (cross-tabulation, или для краткости crosstab) — частный случай сводной таблицы, в которой представлены частоты групп. Приведем пример:

In [167]: from io import StringIO

In [168]: data = """Sample Nationality Handedness
.....: 1 USA Right-handed
.....: 2 Japan Left-handed
.....: 3 USA Right-handed
.....: 4 Japan Right-handed
.....: 5 Japan Left-handed
.....: 6 Japan Right-handed
.....: 7 USA Right-handed
.....: 8 USA Left-handed
.....: 9 Japan Right-handed
.....: 10 USA Right-handed"""

In [169]: data = pd.read_table(StringIO(data), sep="\s+")

In [170]: data
Out[170]:
   Sample  Nationality  Handedness
0       1           USA  Right-handed
1       2          Japan  Left-handed
2       3           USA  Right-handed