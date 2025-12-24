---
source_image: page_229.png
page_number: 229
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 29.36
tokens: 7799
characters: 1413
timestamp: 2025-12-24T02:46:16.079785
finish_reason: stop
---

4   28   29   30   31   32   33   34
2   14   15   16   17   18   19   20
0   0   1   2   3   4   5   6

In [108]: df.iloc[sampler]
Out[108]:
    0   1   2   3   4   5   6
3   21   22   23   24   25   26   27
1   7   8   9   10   11   12   13
4   28   29   30   31   32   33   34
2   14   15   16   17   18   19   20
0   0   1   2   3   4   5   6

Вызвав take с параметром axis="columns", мы могли бы также произвести перестановку столбцов:

In [109]: column_sampler = np.random.permutation(7)

In [110]: column_sampler
Out[110]: array([4, 6, 3, 2, 1, 0, 5])

In [111]: df.take(column_sampler, axis="columns")
Out[111]:
    4   6   3   2   1   0   5
0   4   6   3   2   1   0   5
1   11  13  10  9   8   7   12
2   18  20  17  16  15  14  19
3   25  27  24  23  22  21  26
4   32  34  31  30  29  28  33

Чтобы выбрать случайное подмножество без возвращения, можно использовать метод sample объектов Series и DataFrame:

In [112]: df.sample(n=3)
Out[112]:
    0   1   2   3   4   5   6
2   14  15  16  17  18  19  20
4   28  29  30  31  32  33  34
0   0   1   2   3   4   5   6

Чтобы сгенерировать выборку с возвращением (когда разрешается выбирать один и тот же элемент несколько раз), передайте методу sample аргумент replace=True:

In [113]: choices = pd.Series([5, 7, -1, 6, 4])

In [114]: choices.sample(n=10, replace=True)
Out[114]:
2   -1
0   5
3   6
1   7
4   4
0   5
4   4
0   5
4   4
4   4
dtype: int64