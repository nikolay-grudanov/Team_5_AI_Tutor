---
source_image: page_284.png
page_number: 284
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 24.69
tokens: 7487
characters: 1309
timestamp: 2025-12-24T02:47:47.806279
finish_reason: stop
---

2   baz    A    3
3   foo    B    4
4   bar    B    5
5   baz    B    6
6   foo    C    7
7   bar    C    8
8   baz    C    9

Применив pivot, мы можем вернуться к исходной форме:

In [170]: reshaped = melted.pivot(index="key", columns="variable", values="value")
......:

In [171]: reshaped
Out[171]:
variable  A  B  C
key
bar      2  5  8
baz      3  6  9
foo      1  4  7

Поскольку в результате работы pivot из столбца создается индекс, используемый как метки строк, возможно, понадобится вызвать reset_index, чтобы переместить данные обратно в столбец:

In [172]: reshaped.reset_index()
Out[172]:
variable  key  A  B  C
0        bar  2  5  8
1        baz  3  6  9
2        foo  1  4  7

Можно также указать, какое подмножество столбцов следует использовать в роли значений:

In [173]: pd.melt(df, id_vars="key", value_vars=["A", "B"])
Out[173]:
    key variable value
0   foo      A     1
1   bar      A     2
2   baz      A     3
3   foo      B     4
4   bar      B     5
5   baz      B     6

Функцию pandas.melt можно использовать и без идентификаторов групп:

In [174]: pd.melt(df, value_vars=["A", "B", "C"])
Out[174]:
    variable value
0         A     1
1         A     2
2         A     3
3         B     4
4         B     5
5         B     6
6         C     7
7         C     8
8         C     9