---
source_image: page_349.png
page_number: 349
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 51.71
tokens: 8416
characters: 2628
timestamp: 2025-12-24T02:50:02.419991
finish_reason: stop
---

Вернемся к набору данных о чаевых и вычислим таблицу групповых средних (тип агрегирования по умолчанию, подразумеваемый pivot_table) по столбцам day и smoker, расположив их в строках:

In [161]: tips.head()
Out[161]:
    total_bill   tip  smoker  day   time  size  tip_pct
0      16.99  1.01    No  Sun  Dinner    2  0.059447
1      10.34  1.66    No  Sun  Dinner    3  0.160542
2      21.01  3.50    No  Sun  Dinner    3  0.166587
3      23.68  3.31    No  Sun  Dinner    2  0.139780
4      24.59  3.61    No  Sun  Dinner    4  0.146808

In [162]: tips.pivot_table(index=["day", "smoker"])
Out[162]:
          size   tip  tip_pct  total_bill
day smoker
Fri  No     2.250000  2.812500  0.151650  18.420000
      Yes    2.066667  2.714000  0.174783  16.813333
Sat  No     2.555556  3.102889  0.158048  19.661778
      Yes    2.476190  2.875476  0.147906  21.276667
Sun  No     2.929825  3.167895  0.160113  20.506667
      Yes    2.578947  3.516842  0.187250  24.120000
Thur No     2.488889  2.673778  0.160298  17.113111
      Yes    2.352941  3.030000  0.163863  19.190588

Это можно было бы легко сделать и непосредственно с помощью groupby, написав tips.groupby(["day", "smoker"]).mean(). Пусть теперь требуется вычислить среднее только для tip_pct и size, добавив еще группировку по time. Я помещу smoker в столбцы таблицы, а time и day — в строки:

In [163]: tips.pivot_table(index=["time", "day"], columns="smoker",
.....:     values=["tip_pct", "size"])
Out[163]:
           size   tip_pct
smoker      No   Yes   No   Yes
time   day
Dinner Fri   2.000000 2.222222 0.139622 0.165347
        Sat   2.555556 2.476190 0.158048 0.147906
        Sun   2.929825 2.578947 0.160113 0.187250
        Thur  2.000000 NaN   0.159744 NaN
Lunch Fri   3.000000 1.833333 0.187735 0.188937
        Thur  2.500000 2.352941 0.160311 0.163863

Эту таблицу можно было бы дополнить, включив частичные итоги, для чего следует задать параметр margins=True. Тогда будут добавлены строка и столбец с меткой All, значениями в которых будут групповые статистики по всем данным на одном уровне.

In [164]: tips.pivot_table(index=["time", "day"], columns="smoker",
.....:     values=["tip_pct", "size"], margins=True)
Out[164]:
           size   tip_pct
smoker      No   Yes   All   No   Yes   All
time   day
Dinner Fri   2.000000 2.222222 0.139622 0.165347 0.150484
        Sat   2.555556 2.476190 0.158048 0.147906 0.152977
        Sun   2.929825 2.578947 0.160113 0.187250 0.173681
        Thur  2.000000 NaN   0.159744 NaN  0.159744
Lunch Fri   3.000000 1.833333 0.187735 0.188937 0.188334
        Thur  2.500000 2.352941 0.160311 0.163863 0.162087