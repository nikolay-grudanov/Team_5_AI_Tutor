---
source_image: page_325.png
page_number: 325
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 33.32
tokens: 7841
characters: 1905
timestamp: 2025-12-24T02:48:59.788907
finish_reason: stop
---

In [39]: s_grouped = df.groupby(["key1", "key2"])["data2"]

In [40]: s_grouped
Out[40]: <pandas.core.groupby.generic.SeriesGroupBy object at 0x7fa9270e3520>

In [41]: s_grouped.mean()
Out[41]:
    key1   key2
a      1   0.281746
        2   0.769023
b      1  -1.296221
        2   1.007189
Name: data2, dtype: float64

Группировка с помощью словарей и объектов Series
Информацию о группировке можно передавать не только в виде массива. Рассмотрим еще один объект DataFrame:

In [42]: people = pd.DataFrame(np.random.standard_normal((5, 5)),
    ....:                 columns=["a", "b", "c", "d", "e"],
    ....:                 index=["Joe", "Steve", "Wanda", "Jill", "Trey"])

In [43]: people.iloc[2:3, [1, 2]] = np.nan # Add a few NA values

In [44]: people
Out[44]:
         a         b         c         d         e
Joe  1.352917  0.886429 -2.001637 -0.371843  1.669025
Steve -0.438570 -0.539741  0.476985  3.248944 -1.021228
Wanda -0.577087     NaN     NaN  0.523772  0.000940
Jill  1.343810 -0.713544 -0.831154 -2.370232 -1.860761
Trey -0.860757  0.560145 -1.265934  0.119827 -1.063512

Теперь предположим, что имеется соответствие между столбцами и группами и нужно просуммировать столбцы для каждой группы:

In [45]: mapping = {"a": "red", "b": "red", "c": "blue",
    ....:           "d": "blue", "e": "red", "f": "orange"}

Из этого словаря нетрудно построить массив и передать его groupby, но можно вместо этого передать и сам словарь (я включил ключ "f", чтобы показать, что неиспользуемые ключи группировки не составляют проблемы):

In [46]: by_column = people.groupby(mapping, axis="columns")

In [47]: by_column.sum()
Out[47]:
         blue     red
Joe   -2.373480  3.908371
Steve  3.725929 -1.999539
Wanda  0.523772 -0.576147
Jill  -3.201385 -1.230495
Trey  -1.146107 -1.364125

То же самое относится и к объекту Series, который можно рассматривать как отображение фиксированного размера.