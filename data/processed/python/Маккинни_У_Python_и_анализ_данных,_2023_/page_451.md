---
source_image: page_451.png
page_number: 451
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 22.67
tokens: 7423
characters: 1290
timestamp: 2025-12-24T02:52:40.181581
finish_reason: stop
---

6    fgroup      375176 non-null object
7    manufacturer 293054 non-null object
dtypes: float64(1), int64(1), object(6)
memory usage: 25.8+ MB

In [193]: ndata.iloc[30000]
Out[193]:
value           0.04
units           g
nutrient        Glycine
nutgroup        Amino Acids
id              6158
food            Soup, tomato bisque, canned, condensed
fgroup          Soups, Sauces, and Gravies
manufacturer
Name: 30000, dtype: object

Теперь можно построить график медианных значений по группе и типу питательного элемента (рис. 13.11):

In [195]: result = ndata.groupby(["nutrient", "fgroup"])["value"].quantile(0.5)

In [196]: result["Zinc, Zn"].sort_values().plot(kind="barh")

![Медианные значения цинка по группе питательных элементов](../images/13_11.png)

Рис. 13.11. Медианные значения цинка по группе питательных элементов

Воспользовавшись методом idxmax или argmax объекта Series, мы сможем найти, какой продукт питания наиболее богат каждым питательным элементом. Выполните следующий код в ячейке Jupyter:

by_nutrient = ndata.groupby(["nutgroup", "nutrient"])

def get_maximum(x):
    return x.loc[x.value.idxmax()]

max_foods = by_nutrient.apply(get_maximum)[["value", "food"]]

# Немного уменьшить длину названия продукта питания
max_foods["food"] = max_foods["food"].str[:50]