---
source_image: page_423.png
page_number: 423
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 30.12
tokens: 7630
characters: 1655
timestamp: 2025-12-24T02:51:59.151761
finish_reason: stop
---

In [53]: indexer = agg_counts.sum("columns").argsort()

In [54]: indexer.values[:10]
Out[54]: array([24, 20, 21, 92, 87, 53, 54, 57, 26, 55])

Я воспользуюсь методом take, чтобы выбрать строки в этом порядке, и оставлю только последние 10 строк (с наибольшими значениями):

In [55]: count_subset = agg_counts.take(indexer[-10:])

In [56]: count_subset
Out[56]:
os      Not Windows   Windows
tz
America/Sao_Paulo    13.0    20.0
Europe/Madrid        16.0    19.0
Pacific/Honolulu     0.0     36.0
Asia/Tokyo           2.0     35.0
Europe/London        43.0    31.0
America/Denver       132.0   59.0
America/Los_Angeles  130.0   252.0
America/Chicago      115.0   285.0
                245.0   276.0
America/New_York     339.0   912.0

В pandas имеется вспомогательный метод nlargest, который делает то же самое:

In [57]: agg_counts.sum(axis="columns").nlargest(10)
Out[57]:
tz
America/New_York    1251.0
                    521.0
America/Chicago     400.0
America/Los_Angeles 382.0
America/Denver      191.0
Europe/London       74.0
Asia/Tokyo          37.0
Pacific/Honolulu    36.0
Europe/Madrid       35.0
America/Sao_Paulo   33.0
dtype: float64

Теперь это можно визуализировать с помощью групповой столбчатой диаграммы для сравнения количества пользователей Windows и прочих; воспользуемся функцией barplot из библиотеки seaborn (см. рис. 13.2). Сначала я вызываю count_subset.stack(), а затем перестраиваю индекс, чтобы привести данные к форме, лучше совместимой с seaborn:

In [59]: count_subset = count_subset.stack()

In [60]: count_subset.name = "total"

In [61]: count_subset = count_subset.reset_index()

In [62]: count_subset.head(10)
Out[62]: