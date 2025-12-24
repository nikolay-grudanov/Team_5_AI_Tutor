---
source_image: page_350.png
page_number: 350
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 32.13
tokens: 7823
characters: 1594
timestamp: 2025-12-24T02:49:43.301954
finish_reason: stop
---

Для применения функции агрегирования, отличной от mean, передайте ее в именованном параметре aggfunc. Например, передача "count" или len даст перекрестную таблицу (счетчики или частоты) размеров групп (хотя "count" не учитывает значения null, встречающиеся в группах, а len учитывает):

In [165]: tips.pivot_table(index=["time", "smoker"], columns="day",
    ....:                 values="tip_pct", aggfunc=len, margins=True)
Out[165]:
day      Fri   Sat   Sun   Thur   All
time smoker
Dinner  No     3.0   45.0   57.0   1.0   106
        Yes    9.0   42.0   19.0   NaN   70
Lunch   No     1.0   NaN    NaN    44.0   45
        Yes    6.0   NaN    NaN    17.0   23
All     19.0  87.0  76.0  62.0  244

Для восполнения отсутствующих комбинаций можно задать параметр fill_value:

In [166]: tips.pivot_table(index=["time", "size", "smoker"], columns="day",
    ....:                 values="tip_pct", fill_value=0)
Out[166]:
day
time size smoker
Dinner  1   No     0.000000  0.137931  0.000000  0.000000
        Yes   0.000000  0.325733  0.000000  0.000000
        2   No     0.139622  0.162705  0.168859  0.159744
        Yes   0.171297  0.148668  0.207893  0.000000
        3   No     0.000000  0.154661  0.152663  0.000000
...
Lunch   3   Yes   0.000000  0.000000  0.000000  0.204952
        4   No     0.000000  0.000000  0.000000  0.138919
        Yes   0.000000  0.000000  0.000000  0.155410
        5   No     0.000000  0.000000  0.000000  0.121389
        6   No     0.000000  0.000000  0.000000  0.173706
[21 rows x 4 columns]

В табл. 10.2 приведена сводка аргументов метода pivot_table.