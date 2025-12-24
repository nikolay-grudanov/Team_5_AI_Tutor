---
source_image: page_161.png
page_number: 161
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 24.52
tokens: 7474
characters: 1244
timestamp: 2025-12-24T02:44:16.174061
finish_reason: stop
---

In [153]: data
Out[153]:
    one   two   three   four
Ohio     0     0     0     0
Colorado 0     5     6     7
Utah     8     9    10    11
New York 12    13    14    15

In [154]: data.loc["Colorado"]
Out[154]:
One    0
two    5
three  6
four   7
Name: Colorado, dtype: int64

Результатом выбора одной строки является объект Series с индексом, содержащим метки столбцов DataFrame. Чтобы выбрать несколько строк и тем самым создать новый объект DataFrame, передадим последовательность меток:

In [155]: data.loc[["Colorado", "New York"]]
Out[155]:
    one   two   three   four
Colorado 0     5     6     7
New York 12    13    14    15

Оператор loc позволяет выбрать одновременно строки и столбцы — нужно только разделить указания тех и других запятой:

In [156]: data.loc["Colorado", ["two", "three"]]
Out[156]:
two    5
three  6
Name: Colorado, dtype: int64

Затем произведем аналогичную выборку, но уже по целочисленным индексам с помощью iloc:

In [157]: data.iloc[2]
Out[157]:
one    8
two    9
three  10
four   11
Name: Utah, dtype: int64

In [158]: data.iloc[[2, 1]]
Out[158]:
    one   two   three   four
Utah   8     9     10    11
Colorado 0     5     6     7

In [159]: data.iloc[2, [3, 0, 1]]
Out[159]:
four   11
one    8
two    9