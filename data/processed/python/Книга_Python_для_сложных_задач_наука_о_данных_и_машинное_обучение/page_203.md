---
source_image: page_203.png
page_number: 203
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 26.84
tokens: 7574
characters: 2031
timestamp: 2025-12-24T00:56:34.738789
finish_reason: stop
---

Объект GroupBy

Объект GroupBy — очень гибкая абстракция. Во многом с ним можно обращаться как с коллекцией объектов DataFrame, и вся сложность будет скрыта от пользователя. Рассмотрим примеры на основе набора данных «Планеты».

Вероятно, самые важные из доступных благодаря объекту GroupBy операций — агрегирование, фильтрация, преобразование и применение. Мы обсудим каждую из них более подробно в пункте «Агрегирование, фильтрация, преобразование, применение» данного подраздела, но сначала познакомимся с другой функциональностью, которую можно использовать вместе с базовой операцией GroupBy.

Индексация по столбцам. Объект GroupBy поддерживает индексацию по столбцам аналогично объекту DataFrame, с возвратом модифицированного объекта GroupBy. Например:

In[14]: planets.groupby('method')

Out[14]: <pandas.core.groupby.DataFrameGroupBy object at 0x1172727b8>

In[15]: planets.groupby('method')['orbital_period']

Out[15]: <pandas.core.groupby.SeriesGroupBy object at 0x117272da0>

Здесь мы выбрали конкретную группу Series из исходной группы DataFrame, сославшись на соответствующее имя столбца. Как и в случае с объектом GroupBy, никаких вычислений не происходит до вызова для этого объекта какого-нибудь агрегирующего метода:

In[16]: planets.groupby('method')['orbital_period'].median()

Out[16]: method
    Astrometry           631.180000
    Eclipse Timing Variations   4343.500000
    Imaging                27500.000000
    Microlensing            3300.000000
    Orbital Brightness Modulation   0.342887
    Pulsar Timing             66.541900
    Pulsation Timing Variations 1170.000000
    Radial Velocity          360.200000
    Transit                  5.714932
    Transit Timing Variations 57.011000
Name: orbital_period, dtype: float64

Результат дает нам общее представление о масштабе чувствительности каждого из методов к периодам обращения (в днях).

Цикл по группам. Объект GroupBy поддерживает непосредственное выполнение циклов по группам с возвратом каждой группы в виде объекта Series или DataFrame: