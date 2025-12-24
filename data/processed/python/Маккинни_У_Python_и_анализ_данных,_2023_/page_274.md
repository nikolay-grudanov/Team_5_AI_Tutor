---
source_image: page_274.png
page_number: 274
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 39.11
tokens: 7888
characters: 1833
timestamp: 2025-12-24T02:47:43.059638
finish_reason: stop
---

8.2. Комбинирование и слияние наборов данных

In [108]: pd.concat({"level1": df1, "level2": df2}, axis="columns")
Out[108]:
    level1   level2
      one   two three four
a     0     1   5.0   6.0
b     2     3   NaN   NaN
c     4     5   7.0   8.0

Дополнительные аргументы управляют созданием иерархического индекса (см. табл. 8.3). Например, можно поименовать созданные уровни на оси с помощью аргумента names:

In [109]: pd.concat([df1, df2], axis="columns", keys=["level1", "level2"], names=["upper", "lower"])
Out[109]:
upper level1   level2
lower   one   two three four
a     0     1   5.0   6.0
b     2     3   NaN   NaN
c     4     5   7.0   8.0

Последнее замечание касается объектов DataFrame, в которых индекс строк не содержит никаких релевантных данных:

In [110]: df1 = pd.DataFrame(np.random.standard_normal((3, 4)),
.....:         columns=["a", "b", "c", "d"])

In [111]: df2 = pd.DataFrame(np.random.standard_normal((2, 3)),
.....:         columns=["b", "d", "a"])

In [112]: df1
Out[112]:
      a      b      c      d
0  1.248804  0.774191 -0.319657 -0.624964
1  1.078814  0.544647  0.855588  1.343268
2 -0.267175  1.793095 -0.652929 -1.886837

In [113]: df2
Out[113]:
      b      d      a
0  1.059626  0.644448 -0.007799
1 -0.449204  2.448963  0.667226

В таком случае можно передать параметр ignore_index=True, тогда индексы из всех объектов DataFrame отбрасываются, а конкатенируются только данные в столбцах. При этом назначается новый индекс по умолчанию.

In [114]: pd.concat([df1, df2], ignore_index=True)
Out[114]:
      a      b      c      d
0  1.248804  0.774191 -0.319657 -0.624964
1  1.078814  0.544647  0.855588  1.343268
2 -0.267175  1.793095 -0.652929 -1.886837
3 -0.007799  1.059626      NaN  0.644448
4  0.667226 -0.449204      NaN  2.448963

В табл. 8.3 описаны аргументы функции pandas.concat.