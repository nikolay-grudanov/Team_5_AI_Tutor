---
source_image: page_245.png
page_number: 245
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 23.65
tokens: 7414
characters: 1279
timestamp: 2025-12-24T02:46:39.836824
finish_reason: stop
---

Для чего это нужно
Часто бывает, что столбец таблицы содержит небольшое множество повторяющихся значений. Мы уже встречались с функциями unique и value_counts, которые позволяют соответственно получить различные значения, встречающиеся в массиве, и подсчитать их частоты:

In [199]: values = pd.Series(['apple', 'orange', 'apple',
    ....:                     'apple'] * 2)

In [200]: values
Out[200]:
0    apple
1    orange
2    apple
3    apple
4    apple
5    orange
6    apple
7    apple
dtype: object

In [201]: pd.unique(values)
Out[201]: array(['apple', 'orange'], dtype=object)

In [202]: pd.value_counts(values)
Out[202]:
apple    6
orange   2
dtype: int64

Во многих системах (для организации хранилищ данных, статистических расчетов и т. д.) разработаны специальные подходы к представлению данных с повторяющимися значениями с целью более эффективного хранения и вычислений. В хранилищах данных принято использовать так называемые таблицы измерений, которые содержат различные значения и на которые главные таблицы ссылаются по целочисленным ключам:

In [203]: values = pd.Series([0, 1, 0, 0] * 2)

In [204]: dim = pd.Series(['apple', 'orange'])

In [205]: values
Out[205]:
0    0
1    1
2    0
3    0
4    0
5    1
6    0
7    0
dtype: int64

In [206]: dim
Out[206]: