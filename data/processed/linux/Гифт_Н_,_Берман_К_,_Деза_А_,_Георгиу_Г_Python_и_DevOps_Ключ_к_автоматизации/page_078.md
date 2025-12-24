---
source_image: page_078.png
page_number: 78
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 28.88
tokens: 7523
characters: 1631
timestamp: 2025-12-24T03:02:58.359243
finish_reason: stop
---

вычисления над столбцами из нескольких строк и файл не слишком велик, имеет смысл загрузить его в память целиком.

Пакет Pandas — краеугольный камень мира науки о данных. Он содержит структуру данных pandas.DataFrame, ведущую себя наподобие таблицы данных, аналогичной электронной таблице с очень широкими возможностями. DataFrame — идеальный инструмент для статистического анализа табличных данных или каких-либо операций с их столбцами или строками. Это сторонняя библиотека, которую необходимо установить с помощью pip. Существует множество способов загрузки данных в объекты DataFrame, один из наиболее распространенных — загрузка из CSV-файла:

In [54]: import pandas as pd

In [55]: df = pd.read_csv('sample-data.csv')

In [56]: type(df)
Out[56]: pandas.core.frame.DataFrame

Можете просмотреть несколько первых строк объекта DataFrame с помощью метода head:

In [57]: df.head(3)
Out[57]:
    Attributes   open   high   low   close   volume
0      Symbols     F     F     F     F       F
1        date   NaN   NaN   NaN   NaN     NaN
2  2018-01-02  11.3007  11.4271  11.2827  11.4271  20773320

А основные статистические показатели DataFrame можно вывести с помощью метода describe:

In [58]: df.describe()
Out[58]:
    Attributes   open   high   low   close   volume
count      357   356   356   356   356   356
unique     357   290   288   297   288   356
top  2018-10-18  10.402  8.3363  10.2  9.8111  36298597
freq         1      5      4      3      4      1

Или можно просмотреть отдельный столбец данных, указав его название в квадратных скобках:

In [59]: df['close']
Out[59]:
0      F
1    NaN
2  11.4271
3  11.5174