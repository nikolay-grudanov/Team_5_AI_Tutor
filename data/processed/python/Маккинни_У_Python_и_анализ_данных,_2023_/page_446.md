---
source_image: page_446.png
page_number: 446
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 19.95
tokens: 7315
characters: 837
timestamp: 2025-12-24T02:52:29.934026
finish_reason: stop
---

Lesley    35022
Lesli     929
Leslie    370429
Lesly     10067
Name: births, dtype: int64

Затем агрегируем по полу и году и нормируем в пределах каждого года:

In [164]: table = filtered.pivot_table("births", index="year",
.....:                                 columns="sex", aggfunc="sum")

In [165]: table = table.div(table.sum(axis="columns"), axis="index")

In [166]: table.tail()
Out[166]:
   sex   F   M
year
2006  1.0  NaN
2007  1.0  NaN
2008  1.0  NaN
2009  1.0  NaN
2010  1.0  NaN

Наконец, нетрудно построить график распределения по полу в зависимости от времени (рис. 13.10).

In [168]: table.plot(style={"M": "k-", "F": "k--"})

![График изменения доли мальчиков и девочек с именами, похожими на Lesley](https://i.imgur.com/13.10.png)

Рис. 13.10. Изменение во времени доли мальчиков и девочек с именами, похожими на Lesley