---
source_image: page_450.png
page_number: 450
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 38.14
tokens: 7788
characters: 2285
timestamp: 2025-12-24T02:52:51.983993
finish_reason: stop
---

Поскольку в обоих объектах DataFrame имеются столбцы 'group' и 'description', переименуем их, чтобы было понятно, что есть что:

In [185]: col_mapping = {"description" : "food",
.....:         "group" : "fgroup"}

In [186]: info = info.rename(columns=col_mapping, copy=False)

In [187]: info.info()
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 6636 entries, 0 to 6635
Data columns (total 4 columns):
#    Column    Non-Null Count Dtype
---  ------    --------------  -----
0   food      6636 non-null   object
1   fgroup    6636 non-null   object
2   id        6636 non-null   int64
3   manufacturer  5195 non-null object
dtypes: int64(1), object(3)
memory usage: 207.5+ KB

In [188]: col_mapping = {"description" : "nutrient",
.....:         "group" : "nutgroup"}

In [189]: nutrients = nutrients.rename(columns=col_mapping, copy=False)

In [190]: nutrients
Out[190]:
    value  units                nutrient    nutgroup    id
0   25.180   g                  Protein     Composition  1008
1   29.200   g                  Total lipid (fat)  Composition  1008
2   3.060    g                  Carbohydrate, by difference  Composition  1008
3   3.280    g                  Ash           Other        1008
4   376.000  kcal                Energy       Energy       1008
...   ...     ...                ...          ...          ...
389350  0.000  mcg               Vitamin B-12, added  Vitamins  43546
389351  0.000  mg                Cholesterol     Other      43546
389352  0.072  g                 Fatty acids, total saturated  Other      43546
389353  0.028  g                 Fatty acids, total monounsaturated  Other      43546
389354  0.041  g                 Fatty acids, total polyunsaturated  Other      43546
[375176 rows x 5 columns]

Сделав все это, мы можем объединить info с nutrients:

In [191]: ndata = pd.merge(nutrients, info, on="id")

In [192]: ndata.info()
<class 'pandas.core.frame.DataFrame'>
Int64Index: 375176 entries, 0 to 375175
Data columns (total 8 columns):
#    Column    Non-Null Count Dtype
---  ------    --------------  -----
0   value     375176 non-null float64
1   units     375176 non-null object
2   nutrient  375176 non-null object
3   nutgroup  375176 non-null object
4   id        375176 non-null int64
5   food      375176 non-null object