---
source_image: page_338.png
page_number: 338
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 16.69
tokens: 7459
characters: 1282
timestamp: 2025-12-24T02:49:06.468342
finish_reason: stop
---

Пример: подстановка зависящих от группы значений вместо отсутствующих

Иногда отсутствующие данные требуется отфильтровать методом dropna, а иногда восполнить их, подставив либо фиксированное значение, либо значение, зависящее от данных. Для этой цели предназначен метод fillna; вот, например, как можно заменить отсутствующие значения средним:

In [102]: s = pd.Series(np.random.standard_normal(6))

In [103]: s[::2] = np.nan

In [104]: s
Out[104]:
0    NaN
1   0.227290
2    NaN
3  -2.153545
4    NaN
5  -0.375842
dtype: float64

In [105]: s.fillna(s.mean())
Out[105]:
0   -0.767366
1   0.227290
2   -0.767366
3  -2.153545
4   -0.767366
5  -0.375842
dtype: float64

А что делать, если подставляемое значение зависит от группы? Один из способов решить задачу — сгруппировать данные и вызвать метод apply, передав ему функцию, которая вызывает fillna для каждого блока данных. Ниже приведены данные о некоторых штатах США с разделением на восточные и западные:

In [106]: states = ["Ohio", "New York", "Vermont", "Florida",
      ....:         "Oregon", "Nevada", "California", "Idaho"]

In [107]: group_key = ["East", "East", "East", "East",
      ....:         "West", "West", "West", "West"]

In [108]: data = pd.Series(np.random.standard_normal(8), index=states)

In [109]: data