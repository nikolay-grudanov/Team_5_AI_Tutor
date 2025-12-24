---
source_image: page_439.png
page_number: 439
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 10.10
tokens: 7252
characters: 808
timestamp: 2025-12-24T02:52:05.631264
finish_reason: stop
---

Number of births per year

![Распределение нескольких имен мальчиков и девочек по годам](https://i.imgur.com/3Q5z5QG.png)

Рис. 13.5. Распределение нескольких имен мальчиков и девочек по годам

Измерение роста разнообразия имен
Убывание кривых на рисунках выше можно объяснить тем, что меньше родителей стали выбирать для своих детей распространенные имена. Эту гипотезу можно проверить и подтвердить имеющимися данными. Один из возможных показателей — доля родившихся в наборе 1000 самых популярных имен, который я агрегирую по году и полу (результат показан на рис. 13.6):

In [131]: table = top1000.pivot_table("prop", index="year",
.....:                columns="sex", aggfunc=sum)

In [132]: table.plot(title="Sum of table1000.prop by year and sex",
.....:                yticks=np.linspace(0, 1.2, 13))