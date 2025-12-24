---
source_image: page_448.png
page_number: 448
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 29.58
tokens: 7575
characters: 1799
timestamp: 2025-12-24T02:52:42.989214
finish_reason: stop
---

13.4. База данных о продуктах питания министерства сельского хозяйства...

Out[173]:
{'value': 25.18,
 'units': 'g',
 'description': 'Protein',
 'group': 'Composition'}

In [174]: nutrients = pd.DataFrame(db[0]["nutrients"])

In [175]: nutrients.head(7)
Out[175]:
    value  units      description        group
0   25.18   g         Protein           Composition
1   29.20   g   Total lipid (fat)   Composition
2   3.06    g Carbohydrate, by difference Composition
3   3.28    g                Ash           Other
4  376.00  kcal          Energy           Energy
5   39.28   g         Water           Composition
6  1573.00  kJ          Energy           Energy

Преобразуя список словарей в DataFrame, можно задать список полей, подлежащих извлечению. Мы ограничимся названием продукта, группой, идентификатором и производителем:

In [176]: info_keys = ["description", "group", "id", "manufacturer"]

In [177]: info = pd.DataFrame(db, columns=info_keys)

In [178]: info.head()
Out[178]:
    description        group  id  manufacturer
0  Cheese, caraway  Dairy and Egg Products  1008
1  Cheese, cheddar  Dairy and Egg Products  1009
2  Cheese, edam     Dairy and Egg Products  1018
3  Cheese, feta     Dairy and Egg Products  1019
4  Cheese, mozzarella, part skim milk  Dairy and Egg Products  1028

In [179]: info.info()
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 6636 entries, 0 to 6635
Data columns (total 4 columns):
#    Column    Non-Null Count Dtype
---  ------    --------------  -----
0   description    6636 non-null object
1   group          6636 non-null object
2   id              6636 non-null int64
3   manufacturer   5195 non-null object
dtypes: int64(1), object(3)
memory usage: 207.5+ KB

Из результата info.info() видно, что в столбце manufacturer есть отсутствующие данные.