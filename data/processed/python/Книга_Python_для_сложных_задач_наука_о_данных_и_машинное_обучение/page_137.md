---
source_image: page_137.png
page_number: 137
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 22.00
tokens: 7422
characters: 1520
timestamp: 2025-12-24T00:54:58.091904
finish_reason: stop
---

лучше рассматривать как обобщенные словари, а не обобщенные массивы, хотя обе точки зрения имеют право на жизнь. Мы изучим более гибкие средства индексации объектов DataFrame в разделе «Индексация и выборка данных» этой главы.

Создание объектов DataFrame

Существует множество способов создания объектов DataFrame библиотеки Pandas. Вот несколько примеров.

Из одного объекта Series. Объект DataFrame — набор объектов Series. DataFrame, состоящий из одного столбца, можно создать на основе одного объекта Series:

In[23]: pd.DataFrame(population, columns=['population'])

Out[23]:
      population
California   38332521
Florida      19552860
Illinois     12882135
New York     19651127
Texas        26448193

Из списка словарей. Любой список словарей можно преобразовать в объект DataFrame. Мы воспользуемся простым списковым включением для создания данных:

In[24]: data = [{'a': i, 'b': 2 * i}
                for i in range(3)]
    pd.DataFrame(data)

Out[24]:   a   b
0   0   0
1   1   2
2   2   4

Даже если некоторые ключи в словаре отсутствуют, библиотека Pandas просто заполнит их значениями NaN (то есть Not a number — «не является числом»):

In[25]: pd.DataFrame([{'a': 1, 'b': 2}, {'b': 3, 'c': 4}])

Out[25]:   a   b   c
0   1.0   2   NaN
1   NaN   3   4.0

Из словаря объектов Series. Объект DataFrame также можно создать на основе словаря объектов Series:

In[26]: pd.DataFrame({'population': population,
                     'area': area})

Out[26]:
      area   population
California   423967   38332521