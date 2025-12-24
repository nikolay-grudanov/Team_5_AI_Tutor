---
source_image: page_352.png
page_number: 352
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 16.72
tokens: 7462
characters: 1430
timestamp: 2025-12-24T02:49:31.755915
finish_reason: stop
---

3   4   Japan   Right-handed
4   5   Japan   Left-handed
5   6   Japan   Right-handed
6   7   USA     Right-handed
7   8   USA     Left-handed
8   9   Japan   Right-handed
9   10  USA     Right-handed

В ходе анализа-обследования мы могли бы обобщить эти данные по национальности и праворукости/леворукости. Для этой цели можно использовать метод pivot_table, но функция pandas.crosstab удобнее:

In [171]: pd.crosstab(data["Nationality"], data["Handedness"], margins=True)
Out[171]:
Handedness    Left-handed  Right-handed  All
Nationality
Japan           2            3             5
USA              1            4             5
All              3            7            10

Каждый из первых двух аргументов crosstab может быть массивом, объектом Series или списком массивов. Например, в случае данных о чаевых:

In [172]: pd.crosstab([tips["time"], tips["day"]], tips["smoker"], margins=True)
Out[172]:
smoker      No  Yes  All
time day
Dinner Fri   3   9   12
         Sat  45  42  87
         Sun  57  19  76
         Thur  1   0   1
Lunch Fri   1   6   7
         Thur 44  17  61
All        151 93  244

10.5. Заключение

Уверенное владение средствами группировки, имеющимися в pandas, поможет вам как при очистке данных, так и в процессе моделирования или статистического анализа. В главе 13 мы рассмотрим дополнительные примеры использования groupby для реальных данных.

А в следующей главе обратимся к временным рядам.