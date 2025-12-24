---
source_image: page_339.png
page_number: 339
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 19.12
tokens: 7481
characters: 1070
timestamp: 2025-12-24T02:49:10.648250
finish_reason: stop
---

Out[109]:
Ohio      0.329939
New York  0.981994
Vermont   1.105913
Florida   -1.613716
Oregon    1.561587
Nevada    0.406510
California 0.359244
Idaho     -0.614436
dtype: float64

Сделаем так, чтобы некоторые значения отсутствовали:

In [110]: data[["Vermont", "Nevada", "Idaho"]] = np.nan

In [111]: data
Out[111]:
Ohio      0.329939
New York  0.981994
Vermont   NaN
Florida   -1.613716
Oregon    1.561587
Nevada    NaN
California 0.359244
Idaho     NaN
dtype: float64

In [112]: data.groupby(group_key).size()
Out[112]:
East    4
West    4
dtype: int64

In [113]: data.groupby(group_key).count()
Out[113]:
East    3
West    2
dtype: int64

In [114]: data.groupby(group_key).mean()
Out[114]:
East   -0.100594
West   0.960416
dtype: float64

Чтобы подставить вместо отсутствующих значений групповые средние, нужно поступить так:

In [115]: def fill_mean(group):
    .....:     return group.fillna(group.mean())

In [116]: data.groupby(group_key).apply(fill_mean)
Out[116]:
Ohio      0.329939
New York  0.981994
Vermont   -0.100594
Florida   -1.613716
Oregon    1.561587