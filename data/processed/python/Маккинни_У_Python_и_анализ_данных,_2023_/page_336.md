---
source_image: page_336.png
page_number: 336
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 25.46
tokens: 7671
characters: 1602
timestamp: 2025-12-24T02:49:11.101088
finish_reason: stop
---

Квантильный и интервальный анализ

Напомним, что в главе 8 шла речь о некоторых средствах библиотеки pandas, в том числе функциях pandas.cut и pandas.qcut, которые позволяют распределить данные по интервалам, размер которых задан вами или определяется выборочными квантилями. В сочетании с функцией groupby эти методы позволяют очень просто подвергнуть набор данных интервальному или квантильному анализам. Рассмотрим простой набор случайных данных и распределение по интервалам равной длины с помощью pandas.cut:

In [90]: frame = pd.DataFrame({"data1": np.random.standard_normal(1000),
    ....: "data2": np.random.standard_normal(1000)})

In [91]: frame.head()
Out[91]:
   data1    data2
0 -0.660524 -0.612905
1  0.862580  0.316447
2 -0.010032  0.838295
3  0.050009 -1.034423
4  0.670216  0.434304

In [92]: quartiles = pd.cut(frame["data1"], 4)

In [93]: quartiles.head(10)
Out[93]:
0   (-1.23, 0.489]
1   (0.489, 2.208]
2   (-1.23, 0.489]
3   (-1.23, 0.489]
4   (0.489, 2.208]
5   (0.489, 2.208]
6   (-1.23, 0.489]
7   (-1.23, 0.489]
8   (-2.956, -1.23]
9   (-1.23, 0.489]
Name: data1, dtype: category
Categories (4, interval[float64, right]): [(-2.956, -1.23] < (-1.23, 0.489] < (0.489, 2.208] < (2.208, 3.928]]

Объект Categorical, возвращаемый функцией cut, можно передать непосредственно groupby. Следовательно, набор групповых статистик для квартилей можно вычислить следующим образом:

In [94]: def get_stats(group):
    ....:     return pd.DataFrame(
    ....:         {"min": group.min(), "max": group.max(),
    ....:          "count": group.count(), "mean": group.mean()}
    ....:     )