---
source_image: page_192.png
page_number: 192
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 25.32
tokens: 7616
characters: 1744
timestamp: 2025-12-24T02:45:04.070063
finish_reason: stop
---

6.1. Чтение и запись данных в текстовом формате

Out[28]:
    something   a   b   c   d   message
0      one     1   2  3.0   4   NaN
1     two     5   6   NaN   8   world
2   three     9  10  11.0  12   foo

Напомню, что pandas выводит отсутствующие значения как NaN, так что в result у нас два отсутствующих значения:

In [29]: pd.isna(result)
Out[29]:
    something   a   b   c   d   message
0      False  False  False  False   True
1      False  False  False  True   False
2      False  False  False  False   False

Параметр na_values принимает последовательность строк, добавляемых в список строк, которые по умолчанию рассматриваются как маркеры отсутствия значений:

In [30]: result = pd.read_csv("examples/ex5.csv", na_values=["NULL"])

In [31]: result
Out[31]:
    something   a   b   c   d   message
0      one     1   2  3.0   4   NaN
1     two     5   6   NaN   8   world
2   three     9  10  11.0  12   foo

pandas.read_csv поддерживает длинный список представлений отсутствующих значений, но все это по умолчанию можно отключить, задав параметр keep_default_na:

In [32]: result2 = pd.read_csv("examples/ex5.csv", keep_default_na=False)

In [33]: result2
Out[33]:
    something   a   b   c   d   message
0      one     1   2  3.0   4   NA
1     two     5   6   8   world
2   three     9  10  11.0  12   foo

In [34]: result2.isna()
Out[34]:
    something   a   b   c   d   message
0      False  False  False  False  False
1      False  False  False  False  False
2      False  False  False  False  False

In [35]: result3 = pd.read_csv("examples/ex5.csv", keep_default_na=False, na_values=["NA"])

In [36]: result3
Out[36]:
    something   a   b   c   d   message
0      one     1   2   3   4   NaN
1     two     5   6   8   world