---
source_image: page_321.png
page_number: 321
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 31.11
tokens: 7675
characters: 1507
timestamp: 2025-12-24T02:48:51.477347
finish_reason: stop
---

In [19]: means = df["data1"].groupby([df["key1"], df["key2"]]).mean()

In [20]: means
Out[20]:
key1   key2
a      1    -0.204708
        2     0.478943
B      1     1.965781
        2    -0.555730
Name: data1, dtype: float64

В этом случае данные сгруппированы по двум ключам, а у результирующего объекта Series имеется иерархический индекс, который состоит из уникальных пар значений ключей, встретившихся в исходных данных:

In [21]: means.unstack()
Out[21]:
key2    1     2
key1
a     -0.204708  0.478943
b     1.965781   -0.555730

В этом примере групповыми ключами были объекты Series, но можно было бы использовать и произвольные массивы правильной длины:

In [22]: states = np.array(["OH", "CA", "CA", "OH", "OH", "CA", "OH"])

In [23]: years = [2005, 2005, 2006, 2005, 2006, 2005, 2006]

In [24]: df["data1"].groupby([states, years]).mean()
Out[24]:
CA  2005   0.936175
     2006  -0.519439
OH  2005  -0.380219
     2006   1.029344
Name: data1, dtype: float64

Часто информация о группировке находится в том же объекте DataFrame, что и группируемые данные. В таком случае в качестве групповых ключей можно передать имена столбцов (не важно, что они содержат: строки, числа или другие объекты Python):

In [25]: df.groupby("key1").mean()
Out[25]:
    key2   data1   data2
key1
a     1.5  0.555881  0.441920
      1.5  0.705025 -0.144516

In [26]: df.groupby("key2").mean()
Out[26]:
    data1   data2
key2
1     0.333636  0.115218
2    -0.038393  0.888106

In [27]: df.groupby(["key1", "key2"]).mean()