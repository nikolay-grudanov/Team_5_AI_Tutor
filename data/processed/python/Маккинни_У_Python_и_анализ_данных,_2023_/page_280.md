---
source_image: page_280.png
page_number: 280
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 37.03
tokens: 7791
characters: 1981
timestamp: 2025-12-24T02:47:51.083042
finish_reason: stop
---

При вызове stack также можно указать имя поворачиваемой оси:

In [143]: df.unstack(level="state").stack(level="side")
Out[143]:
state    Colorado  Ohio
number   side
one      left      3   0
         right     8   5
two      left      4   1
         right     9   6
three    left      5   2
         right    10   7

Поворот из «длинного» в «широкий» формат

Стандартный способ хранения нескольких временных рядов в базах данных и в CSV-файлах — так называемый длинный формат (в столбик). В этом формате каждое значение представлено в отдельной строке (в противоположность нескольким значениям в одной строке).

Загрузим демонстрационные данные и займемся переформатированием временных рядов и другими операциями очистки данных:

In [144]: data = pd.read_csv("examples/macrodata.csv")

In [145]: data = data.loc[:, ["year", "quarter", "realgdp", "infl", "unemp"]]

In [146]: data.head()
Out[146]:
   year  quarter  realgdp  infl  unemp
0  1959        1  2710.349  0.00   5.8
1  1959        2  2778.801  2.34   5.1
2  1959        3  2775.488  2.74   5.3
3  1959        4  2785.204  0.27   5.6
4  1960        1  2847.699  2.31   5.2

Сначала я воспользовался функцией pandas.PeriodIndex (представляющей временные интервалы, а не моменты времени), которую мы будем подробно обсуждать в главе 11. Она объединяет столбцы year и quarter, так что индекс содержит значения типа datetime в конце каждого квартала:

In [147]: periods = pd.PeriodIndex(year=data.pop("year"),
.....:                quarter=data.pop("quarter"),
.....:                name="date")

In [148]: periods
Out[148]:
PeriodIndex(['1959Q1', '1959Q2', '1959Q3', '1959Q4', '1960Q1', '1960Q2',
             '1960Q3', '1960Q4', '1961Q1', '1961Q2',
             ...
             '2007Q2', '2007Q3', '2007Q4', '2008Q1', '2008Q2', '2008Q3',
             '2008Q4', '2009Q1', '2009Q2', '2009Q3'],
            dtype='period[Q-DEC]', name='date', length=203)

In [149]: data.index = periods.to_timestamp("D")

In [150]: data.head()