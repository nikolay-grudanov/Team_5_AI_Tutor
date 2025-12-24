---
source_image: page_225.png
page_number: 225
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 34.58
tokens: 7852
characters: 2081
timestamp: 2025-12-24T02:46:11.674030
finish_reason: stop
---

Out[80]:
[(18, 25], (18, 25], (18, 25], (25, 35], (18, 25], ..., (25, 35], (60, 100], (35, 60], (35, 60], (25, 35)]
Length: 12
Categories (4, interval[int64, right]): [(18, 25] < (25, 35] < (35, 60] < (60, 100]]

pandas возвращает специальный объект Categorical. Показанный выше результат — интервалы, вычисленные методом pandas.cut. Каждый интервал можно рассматривать как специальное (уникальное для pandas) значение, содержащее нижнюю и верхнюю границы:

In [81]: age_categories.codes
Out[81]: array([0, 0, 0, 1, 0, 0, 2, 1, 3, 2, 2, 1], dtype=int8)

In [82]: age_categories.categories
Out[82]: IntervalIndex([(18, 25], (25, 35], (35, 60], (60, 100]], dtype='interval [int64, right]')

In [83]: age_categories.categories[0]
Out[83]: Interval(18, 25, closed='right')

In [84]: pd.value_counts(age_categories)
Out[84]:
(18, 25]    5
(25, 35]    3
(35, 60]    3
(60, 100]   1
dtype: int64

Заметим, что pd.value_counts(cats) — счетчики значений в каждом интервале, вычисленном методом pandas.cut.

В строковом представлении интервала круглая скобка означает, что соответствующий конец не включается (интервал открыт), а квадратная — что включается (интервал замкнут). Чтобы сделать открытым правый конец, следует задать параметр right=False:

In [85]: pd.cut(ages, bins, right=False)
Out[85]:
[[18, 25), [18, 25), [25, 35), [25, 35), [18, 25), ..., [25, 35), [60, 100), [35, 60), [35, 60), [25, 35]]
Length: 12
Categories (4, interval[int64, left]): [[18, 25) < [25, 35) < [35, 60) < [60, 100]]

Можно также самостоятельно задать имена интервалов, передав список или массив в параметре labels:

In [86]: group_names = ["Youth", "YoungAdult", "MiddleAged", "Senior"]

In [87]: pd.cut(ages, bins, labels=group_names)
Out[87]:
['Youth', 'Youth', 'Youth', 'YoungAdult', 'Youth', ..., 'YoungAdult', 'Senior', 'MiddleAged', 'MiddleAged', 'YoungAdult']
Length: 12
Categories (4, object): ['Youth' < 'YoungAdult' < 'MiddleAged' < 'Senior']

Если передать методу pandas.cut целое число интервалов, а не явно заданные границы, то он разобьет данные на интервалы равной длины, исходя из мини-