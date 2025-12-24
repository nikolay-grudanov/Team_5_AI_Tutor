---
source_image: page_273.png
page_number: 273
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 26.69
tokens: 7553
characters: 1399
timestamp: 2025-12-24T02:47:30.263403
finish_reason: stop
---

In [101]: result.unstack()
Out[101]:
    a   b   f   g
one  0   1 <NA> <NA>
two  0   1 <NA> <NA>
three <NA> <NA> 5   6

При комбинировании Series вдоль оси axis="columns" элементы списка keys становятся заголовками столбцов объекта DataFrame:

In [102]: pd.concat([s1, s2, s3], axis="columns", keys=["one", "two", "three"])
Out[102]:
    one   two   three
a     0   <NA>   <NA>
b     1   <NA>   <NA>
c   <NA>   2   <NA>
d   <NA>   3   <NA>
e   <NA>   4   <NA>
f   <NA>   <NA>   5
g   <NA>   <NA>   6

Эта логика обобщается и на объекты DataFrame:

In [103]: df1 = pd.DataFrame(np.arange(6).reshape(3, 2), index=["a", "b", "c"], columns=["one", "two"])
In [104]: df2 = pd.DataFrame(5 + np.arange(4).reshape(2, 2), index=["a", "c"], columns=["three", "four"])

In [105]: df1
Out[105]:
    one  two
a    0    1
b    2    3
c    4    5

In [106]: df2
Out[106]:
    three  four
a      5    6
c      7    8

In [107]: pd.concat([df1, df2], axis="columns", keys=["level1", "level2"])
Out[107]:
    level1   level2
        one   two   three   four
a      0    1    5.0    6.0
b      2    3    NaN    NaN
c      4    5    7.0    8.0

Здесь аргумент keys используется для создания иерархического индекса, первый уровень которого будет использован для идентификации каждого из конкатенированных объектов DataFrame.
Если передать не список, а словарь объектов, то роль аргумента keys будут играть ключи словаря: