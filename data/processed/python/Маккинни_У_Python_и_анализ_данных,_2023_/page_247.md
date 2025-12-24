---
source_image: page_247.png
page_number: 247
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 29.51
tokens: 7576
characters: 1599
timestamp: 2025-12-24T02:46:49.960835
finish_reason: stop
---

In [212]: df
Out[212]:
    basket_id  fruit  count   weight
0           0  apple     11  1.564438
1           1 orange      5  1.331256
2           2  apple     12  2.393235
3           3  apple      6  0.746937
4           4  apple      5  2.691024
5           5 orange     12  3.767211
6           6  apple     10  0.992983
7           7  apple     11  3.795525

Здесь df['fruit'] — массив строковых объектов. Его можно следующим образом преобразовать в категориальную форму:

In [213]: fruit_cat = df['fruit'].astype('category')

In [214]: fruit_cat
Out[214]:
0    apple
1   orange
2    apple
3    apple
4    apple
5   orange
6    apple
7    apple
Name: fruit, dtype: category
Categories (2, object): ['apple', 'orange']

Теперь значением fruit_cat является экземпляр типа pandas.Categorical, который можно получить с помощью атрибута .array:

In [215]: c = fruit_cat.array

In [216]: type(c)
Out[216]: pandas.core.arrays.categorical.Categorical
Объект Categorical имеет атрибуты categories и codes:
In [217]: c.categories
Out[217]: Index(['apple', 'orange'], dtype='object')

In [218]: c.codes
Out[218]: array([0, 1, 0, 0, 0, 1, 0, 0], dtype=int8)

К ним можно обратиться проще, воспользовавшись акцессором cat, о котором я расскажу ниже в разделе «Категориальные методы».
Для получения отображения между кодами и категориями есть полезный прием:

In [219]: dict(enumerate(c.categories))
Out[219]: {0: 'apple', 1: 'orange'}

Столбец DataFrame можно преобразовать в категориальную форму с помощью такого присваивания:

In [220]: df['fruit'] = df['fruit'].astype('category')

In [221]: df["fruit"]