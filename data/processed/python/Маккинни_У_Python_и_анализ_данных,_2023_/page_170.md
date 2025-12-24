---
source_image: page_170.png
page_number: 170
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 26.21
tokens: 7563
characters: 1348
timestamp: 2025-12-24T02:44:31.729616
finish_reason: stop
---

Когда мы вычитаем `agg[0]` из `agg`, операция производится один раз для каждой строки. Это называется укладыванием и подробно объясняется в приложении А, поскольку имеет отношение к массивам NumPy вообще. Операции между DataFrame и Series аналогичны:

In [211]: frame = pd.DataFrame(np.arange(12.).reshape((4, 3)),
    ....:
    columns=list("bde"),
    index=["Utah", "Ohio", "Texas", "Oregon"])

In [212]: series = frame.iloc[0]

In [213]: frame
Out[213]:
      b   d   e
Utah  0.0  1.0  2.0
Ohio  3.0  4.0  5.0
Texas 6.0  7.0  8.0
Oregon 9.0 10.0 11.0

In [214]: series
Out[214]:
b    0.0
d    1.0
e    2.0
Name: Utah, dtype: float64

По умолчанию при выполнении арифметических операций между DataFrame и Series индекс Series сопоставляется со столбцами DataFrame, а укладываются строки:

In [215]: frame - series
Out[215]:
      b   d   e
Utah  0.0  0.0  0.0
Ohio  3.0  3.0  3.0
Texas 6.0  6.0  6.0
Oregon 9.0  9.0  9.0

Если какой-нибудь индекс не найден либо в столбцах DataFrame, либо в индексе Series, то объекты переиндексируются для образования объединения:

In [216]: series2 = pd.Series(np.arange(3), index=["b", "e", "f"])

In [217]: series2
Out[217]:
b    0
e    1
f    2
dtype: int64

In [218]: frame + series2
Out[218]:
      b   d   e   f
Utah  0.0 NaN  3.0 NaN
Ohio  3.0 NaN  6.0 NaN
Texas 6.0 NaN  9.0 NaN
Oregon 9.0 NaN 12.0 NaN