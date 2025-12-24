---
source_image: page_449.png
page_number: 449
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 34.50
tokens: 7702
characters: 2428
timestamp: 2025-12-24T02:52:48.362748
finish_reason: stop
---

Метод value_counts покажет распределение продуктов питания по группам:

In [180]: pd.value_counts(info["group"])[10]
Out[180]:
Vegetables and Vegetable Products    812
Beef Products                        618
Baked Products                       496
Breakfast Cereals                    403
Legumes and Legume Products          365
Fast Foods                           365
Lamb, Veal, and Game Products        345
Sweets                               341
Fruits and Fruit Juices              328
Pork Products                        328
Name: group, dtype: int64

Чтобы теперь произвести анализ данных о питательных элементах, проще всего собрать все питательные элементы для всех продуктов в одну большую таблицу. Для этого понадобится несколько шагов. Сначала я преобразую каждый список питательных элементов в объект DataFrame, добавлю столбец id, содержащий идентификатор продукта, и помещу этот DataFrame в список. После этого все объекты можно будет конкатенировать методом concat. Выполните следующий код в ячейке Jupyter:

nutrients = []
for rec in db:
    fnuts = pd.DataFrame(rec["nutrients"])
    fnuts["id"] = rec["id"]
    nutrients.append(fnuts)

nutrients = pd.concat(nutrients, ignore_index=True)

Если все пройдет хорошо, то объект nutrients будет выглядеть следующим образом:

In [182]: nutrients
Out[182]:
      value units                description   group   id
0     25.180 g                   Protein       Composition  1008
1     29.200 g                   Total lipid (fat) Composition  1008
2     3.060 g                     Carbohydrate, by difference Composition  1008
3     3.280 g                     Ash           Other         1008
4     376.000 kcal                Energy        Energy        1008
...   ...   ...                   ...           ...           ...
389350 0.000 mcg                  Vitamin B-12, added Vitamins  43546
389351 0.000 mg                   Cholesterol    Other         43546
389352 0.072 g                    Fatty acids, total saturated Other         43546
389353 0.028 g                    Fatty acids, total monounsaturated Other         43546
389354 0.041 g                    Fatty acids, total polyunsaturated Other         43546
[389355 rows x 5 columns]

Я заметил, что в этом DataFrame есть дубликаты, поэтому лучше их удалить:

In [183]: nutrients.duplicated().sum() # количество дубликатов
Out[183]: 14179

In [184]: nutrients = nutrients.drop_duplicates()