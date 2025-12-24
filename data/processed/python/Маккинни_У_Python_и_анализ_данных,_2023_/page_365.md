---
source_image: page_365.png
page_number: 365
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 32.84
tokens: 7917
characters: 2301
timestamp: 2025-12-24T02:50:14.076407
finish_reason: stop
---

<table>
  <tr>
    <th>Обозначение</th>
    <th>Тип смещения</th>
    <th>Описание</th>
  </tr>
  <tr>
    <td>BQS-JAN, BQS-FEB, ...</td>
    <td>BusinessQuarterBegin</td>
    <td>Ежеквартально с привязкой к первому рабочему дню каждого месяца, считая, что год заканчивается в указанном месяце</td>
  </tr>
  <tr>
    <td>A-JAN, A-FEB, ...</td>
    <td>YearEnd</td>
    <td>Ежегодно с привязкой к последнему календарному дню указанного месяца: JAN, FEB, MAR, APR, MAY, JUN, JUL, AUG, SEP, OCT, NOV, DEC</td>
  </tr>
  <tr>
    <td>BA-JAN, BA-FEB, ...</td>
    <td>BusinessYearEnd</td>
    <td>Ежегодно с привязкой к последнему рабочему дню указанного месяца</td>
  </tr>
  <tr>
    <td>AS-JAN, AS-FEB, ...</td>
    <td>YearBegin</td>
    <td>Ежегодно с привязкой к первому календарному дню указанного месяца</td>
  </tr>
  <tr>
    <td>BAS-JAN, BAS-FEB, ...</td>
    <td>BusinessYearBegin</td>
    <td>Ежегодно с привязкой к первому рабочему дню указанного месяца</td>
  </tr>
</table>

По умолчанию метод pandas.date_range сохраняет время (если оно было задано) начальной и конечной временной метки:

In [79]: pd.date_range("2012-05-02 12:56:31", periods=5)
Out[79]:
DatetimeIndex(['2012-05-02 12:56:31', '2012-05-03 12:56:31',
               '2012-05-04 12:56:31', '2012-05-05 12:56:31',
               '2012-05-06 12:56:31'],
              dtype='datetime64[ns]', freq='D')

Иногда начальная или конечная дата содержит время, но требуется сгенерировать нормализованный набор временных меток, в которых время совпадает с полуночью. Для этого задайте параметр normalize:

In [80]: pd.date_range("2012-05-02 12:56:31", periods=5, normalize=True)
Out[80]:
DatetimeIndex(['2012-05-02', '2012-05-03', '2012-05-04', '2012-05-05',
               '2012-05-06'],
              dtype='datetime64[ns]', freq='D')

Частоты и смещения дат
Частота в pandas состоит из базовой частоты и кратности. Базовая частота обычно обозначается строкой, например 'M' означает раз в месяц, а 'H' — раз в час. Для каждой базовой частоты определен объект, называемый смещением даты (date offset). Так, частоту «раз в час» можно представить классом Hour:

In [81]: from pandas.tseries.offsets import Hour, Minute

In [82]: hour = Hour()

In [83]: hour
Out[83]: <Hour>

Для определения кратности смещения нужно задать целое число: