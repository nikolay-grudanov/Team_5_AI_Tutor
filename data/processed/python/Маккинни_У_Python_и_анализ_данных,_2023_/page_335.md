---
source_image: page_335.png
page_number: 335
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 27.24
tokens: 7717
characters: 1489
timestamp: 2025-12-24T02:49:11.101201
finish_reason: stop
---

In [86]: result = tips.groupby("smoker")["tip_pct"].describe()

In [87]: result
Out[87]:
         count    mean    std    min    25%    50%    75%    max
smoker
No      151.0   0.159328 0.039910 0.056797 0.136906 0.155625 0.185014
Yes     93.0    0.163196 0.085119 0.035638 0.106771 0.153846 0.195059

max
smoker
No      0.291990
Yes     0.710345

In [88]: result.unstack("smoker")
Out[88]:
           smoker
count      No  Yes
mean       0.159328 0.163196
std        0.039910 0.085119
min        0.056797 0.035638
25%        0.136906 0.106771
50%        0.155625 0.153846
75%        0.185014 0.195059
max        0.291990 0.710345
dtype: float64

Когда от имени GroupBy вызывается метод типа describe, на самом деле выполняются такие предложения:

def f(group):
    return group.describe()

grouped.apply(f)

Подавление групповых ключей
В примерах выше мы видели, что у результирующего объекта имеется иерархический индекс, образованный групповыми ключами и индексами каждой части исходного объекта. Создание этого индекса можно подавить, передав методу groupby параметр group_keys=False:

In [89]: tips.groupby("smoker", group_keys=False).apply(top)
Out[89]:
   total_bill  tip  smoker  day  time  size  tip_pct
232      11.61  3.39     No  Sat  Dinner   2  0.291990
149       7.51  2.00     No  Thur  Lunch   2  0.266312
51        10.29  2.60     No  Sun  Dinner   2  0.252672
185      20.69  5.00     No  Sun  Dinner   5  0.241663
88        24.71  5.85     No  Thur  Lunch   2  0.236746