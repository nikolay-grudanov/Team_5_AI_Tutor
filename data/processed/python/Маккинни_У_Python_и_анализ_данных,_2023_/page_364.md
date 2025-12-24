---
source_image: page_364.png
page_number: 364
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 38.81
tokens: 8155
characters: 2666
timestamp: 2025-12-24T02:50:17.779368
finish_reason: stop
---

щий последний рабочий день каждого месяца, то следует передать в качестве частоты значение 'BM', и тогда будут включены только даты, попадающие внутрь или на границу интервала:

In [78]: pd.date_range("2000-01-01", "2000-12-01", freq="BM")
Out[78]:
DatetimeIndex(['2000-01-31', '2000-02-29', '2000-03-31', '2000-04-28',
               '2000-05-31', '2000-06-30', '2000-07-31', '2000-08-31',
               '2000-09-29', '2000-10-31', '2000-11-30'],
              dtype='datetime64[ns]', freq='BM')

Таблица 11.4. Базовые частоты временных рядов (список неполный)

<table>
  <tr>
    <th>Обозначение</th>
    <th>Тип смещения</th>
    <th>Описание</th>
  </tr>
  <tr>
    <td>D</td>
    <td>Day</td>
    <td>Ежедневно</td>
  </tr>
  <tr>
    <td>B</td>
    <td>BusinessDay</td>
    <td>Каждый рабочий день</td>
  </tr>
  <tr>
    <td>H</td>
    <td>Hour</td>
    <td>Ежечасно</td>
  </tr>
  <tr>
    <td>T или min</td>
    <td>Minute</td>
    <td>Ежеминутно</td>
  </tr>
  <tr>
    <td>S</td>
    <td>Second</td>
    <td>Ежесекундно</td>
  </tr>
  <tr>
    <td>L или ms</td>
    <td>Milli</td>
    <td>Каждую миллисекунду</td>
  </tr>
  <tr>
    <td>U</td>
    <td>Micro</td>
    <td>Каждую микросекунду</td>
  </tr>
  <tr>
    <td>M</td>
    <td>MonthEnd</td>
    <td>Последний календарный день месяца</td>
  </tr>
  <tr>
    <td>BM</td>
    <td>BusinessMonthEnd</td>
    <td>Последний рабочий день месяца</td>
  </tr>
  <tr>
    <td>MS</td>
    <td>MonthBegin</td>
    <td>Первый календарный день месяца</td>
  </tr>
  <tr>
    <td>BMS</td>
    <td>BusinessMonthBegin</td>
    <td>Первый рабочий день месяца</td>
  </tr>
  <tr>
    <td>W-MON, W-TUE, ...</td>
    <td>Week</td>
    <td>Еженедельно в указанный день: MON, TUE, WED, THU, FRI, SAT, SUN</td>
  </tr>
  <tr>
    <td>WOM-1MON, WOM-2MON, ...</td>
    <td>WeekOfMonth</td>
    <td>Указанный день первой, второй, третьей или четвертой недели месяца. Например, WOM-3FRI означает третью пятницу каждого месяца</td>
  </tr>
  <tr>
    <td>Q-JAN, Q-FEB, ...</td>
    <td>QuarterEnd</td>
    <td>Ежеквартально с привязкой к последнему календарному дню каждого месяца, считая, что год заканчивается в указанном месяце: JAN, FEB, MAR, APR, MAY, JUN, JUL, AUG, SEP, OCT, NOV, DEC</td>
  </tr>
  <tr>
    <td>BQ-JAN, BQ-FEB, ...</td>
    <td>BusinessQuarterEnd</td>
    <td>Ежеквартально с привязкой к последнему рабочему дню каждого месяца, считая, что год заканчивается в указанном месяце</td>
  </tr>
  <tr>
    <td>QS-JAN, QS-FEB, ...</td>
    <td>QuarterBegin</td>
    <td>Ежеквартально с привязкой к первому календарному дню каждого месяца, считая, что год заканчивается в указанном месяце</td>
  </tr>
</table>