---
source_image: page_445.png
page_number: 445
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 22.12
tokens: 7386
characters: 1030
timestamp: 2025-12-24T02:52:29.857419
finish_reason: stop
---

In [158]: dny_ts.plot()

![Зависимость доли мальчиков с именами, заканчивающимися на буквы d, n, y, от времени](../images/13_9.png)

Рис. 13.9. Зависимость доли мальчиков с именами, заканчивающимися на буквы d, n, y, от времени

Мужские имена, ставшие женскими, и наоборот
Еще одно интересное упражнение — изучить имена, которые раньше часто давали мальчикам, а затем «сменили пол». Возьмем, к примеру, имя Lesley или Leslie. По набору top1000 вычисляю список имен, начинающихся с 'lesl':

In [159]: all_names = pd.Series(top1000["name"].unique())

In [160]: lesley_like = all_names[all_names.str.contains("Lesl")]

In [161]: lesley_like
Out[161]:
   632    Leslie
  2294    Lesley
  4262    Leslee
  4728    Lesli
  6103    Lesly
dtype: object

Далее можно оставить только эти имена и просуммировать количество родившихся, сгруппировав по имени, чтобы найти относительные частоты:

In [162]: filtered = top1000[top1000["name"].isin(lesley_like)]

In [163]: filtered.groupby("name")[["births"]].sum()
Out[163]:
name
Leslee    1082