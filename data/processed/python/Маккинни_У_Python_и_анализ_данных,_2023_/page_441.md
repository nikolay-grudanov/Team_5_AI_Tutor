---
source_image: page_441.png
page_number: 441
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 35.28
tokens: 7688
characters: 1649
timestamp: 2025-12-24T02:52:34.480985
finish_reason: stop
---

searchsorted, то будет возвращена позиция в массиве накопительных сумм, в которую нужно было бы вставить \(0.5\), чтобы не нарушить порядок сортировки:

In [135]: pgor_cumsum = df["pgor"].sort_values(ascending=False).cumsum()

In [136]: pgor_cumsum[:10]
Out[136]:
260877    0.011523
260878    0.020934
260879    0.029959
260880    0.038930
260881    0.047817
260882    0.056579
260883    0.065155
260884    0.073414
260885    0.081528
260886    0.089621
Name: pgor, dtype: float64

In [137]: pgor_cumsum.searchsorted(0.5)
Out[137]: 116

Поскольку индексация массивов начинается с нуля, то нужно прибавить к результату 1 — получится 117. Заметим, что в 1900 году этот показатель был гораздо меньше:

In [138]: df = boys[boys.year == 1900]

In [139]: in1900 = df.sort_values("pgor", ascending=False).pgor.cumsum()

In [140]: in1900.searchsorted(0.5) + 1
Out[140]: 25

Теперь можно применить эту операцию к каждой комбинации года и пола, произвести группировку по этим полям с помощью метода groupby, а затем с помощью метода apply применить функцию, возвращающую счетчик для каждой группы:

def get_quantile_count(group, q=0.5):
    group = group.sort_values("pgor", ascending=False)
    return group.pgor.cumsum().searchsorted(q) + 1

diversity = top1000.groupby(["year", "sex"]).apply(get_quantile_count)
diversity = diversity.unstack()

В получившемся объекте DataFrame с именем diversity хранится два временных ряда, по одному для каждого пола, индексированные по году. Его можно исследовать и, как и раньше, нанести на график (рис. 13.7).

In [143]: diversity.head()
Out[143]:
   sex  F  M
year
1880  38  14
1881  38  14
1882  38  15
1883  39  15