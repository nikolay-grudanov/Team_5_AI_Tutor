---
source_image: page_306.png
page_number: 306
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 42.04
tokens: 7813
characters: 1871
timestamp: 2025-12-24T02:48:39.989471
finish_reason: stop
---

Столбчатые диаграммы полезны для визуализации частоты значений в объекте Series с применением метода value_counts: s.value_counts().plot.bar().

Рассмотрим набор данных о чаевых в ресторане. Допустим, мы хотим построить составную столбчатую диаграмму, показывающую процентную долю данных, относящихся к каждому значению количества гостей в группе за каждый день. Я загружаю данные методом read_csv и выполняю кросс-табуляцию по дню и количеству гостей. Для вычисления простой таблицы частот по двум столбцам DataFrame удобна функция pandas.crosstab:

In [77]: tips = pd.read_csv("examples/tips.csv")

In [78]: tips.head()
Out[78]:
   total_bill  tip  smoker  day  time  size
0      16.99  1.01     No  Sun  Dinner    2
1      10.34  1.66     No  Sun  Dinner    3
2      21.01  3.50     No  Sun  Dinner    3
3      23.68  3.31     No  Sun  Dinner    2
4      24.59  3.61     No  Sun  Dinner    4

In [79]: party_counts = pd.crosstab(tips["day"], tips["size"])

In [80]: party_counts = party_counts.reindex(index=["Thur", "Fri", "Sat", "Sun"])

In [81]: party_counts
Out[81]:
size   1   2   3   4   5   6
day
Thur   1  48   4   5   1   3
Fri    1  16   1   1   0   0
Sat    2  53  18  13   1   0
Sun    0  39  15  18   3   1

Поскольку групп, состоящих из одного или шести гостей, мало, я их удаляю:

In [82]: party_counts = party_counts.loc[:, 2:5]

Затем нормирую значения, так чтобы сумма в каждой строке была равна 1, и строю график (рис. 9.18):

# Нормировка на сумму 1
In [83]: party_pcts = party_counts.div(party_counts.sum(axis="columns"),
    ....:                        axis="index")

In [84]: party_pcts
Out[84]:
size   2   3   4   5
day
Thur  0.827586  0.068966  0.086207  0.017241
Fri   0.888889  0.055556  0.055556  0.000000
Sat   0.623529  0.211765  0.152941  0.011765
Sun   0.520000  0.200000  0.240000  0.040000

In [85]: party_pcts.plot.bar(stacked=True)