---
source_image: page_330.png
page_number: 330
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 32.28
tokens: 7825
characters: 2003
timestamp: 2025-12-24T02:49:06.379337
finish_reason: stop
---

3    23.68   3.31      No   Sun   Dinner   2
4    24.59   3.61      No   Sun   Dinner   4

Теперь добавим в него столбец tip_pct, содержащий размер чаевых в процентах от суммы счета:

In [66]: tips["tip_pct"] = tips["tip"] / tips["total_bill"]

In [67]: tips.head()
Out[67]:
   total_bill   tip  smoker  day   time  size  tip_pct
0     16.99   1.01    No   Sun  Dinner   2   0.059447
1     10.34   1.66    No   Sun  Dinner   3   0.160542
2     21.01   3.50    No   Sun  Dinner   3   0.166587
3     23.68   3.31    No   Sun  Dinner   2   0.139780
4     24.59   3.61    No   Sun  Dinner   4   0.146808

Как мы уже видели, для агрегирования объекта Series или всех столбцов объекта DataFrame достаточно воспользоваться методом aggregate, передав ему требуемую функцию, или вызвать метод mean, std и им подобный. Однако иногда нужно использовать разные функции в зависимости от столбца или сразу несколько функций. К счастью, сделать это совсем нетрудно, что я и продемонстрирую в следующих примерах. Для начала сгруппирую столбец tips по значениям sex и smoker:

In [60]: grouped = tips.groupby(['day', 'smoker'])

Отметим, что в случае описательных статистик типа тех, что приведены в табл. 10.1, можно передать имя функции в виде строки:

In [69]: grouped_pct = grouped["tip_pct"]

In [70]: grouped_pct.agg("mean")
Out[70]:
day   smoker
Fri   No         0.151650
      Yes        0.174783
Sat   No         0.158048
      Yes        0.147906
Sun   No         0.160113
      Yes        0.187250
Thur  No         0.160298
      Yes        0.163863
Name: tip_pct, dtype: float64

Если вместо этого передать список функций или имен функций, то будет возвращен объект DataFrame, в котором имена столбцов совпадают с именами функций:

In [71]: grouped_pct.agg(["mean", "std", peak_to_peak])
Out[71]:
      mean   std  peak_to_peak
day   smoker
Fri   No     0.151650  0.028123  0.067349
      Yes    0.174783  0.051293  0.159925
Sat   No     0.158048  0.039767  0.235193
      Yes    0.147906  0.061375  0.290095