---
source_image: page_251.png
page_number: 251
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 25.59
tokens: 7486
characters: 1467
timestamp: 2025-12-24T02:46:49.516942
finish_reason: stop
---

Переход к категориальной форме может значительно ускорить операции группировки, потому что лежащие в их основе алгоритмы теперь работают с массивом целочисленных кодов, а не строк. Ниже приведено сравнение быстродействия функции value_counts(), в которой используется механизм группировки:

In [249]: %timeit labels.value_counts()
840 ms +- 10.9 ms per loop (mean +- std. dev. of 7 runs, 1 loop each)

In [250]: %timeit categories.value_counts()
30.1 ms +- 549 us per loop (mean +- std. dev. of 7 runs, 10 loops each)

Категориальные методы
Объект Series, содержащий категориальные данные, имеет специальные методы для работы со строками, похожие на Series.str. Он также предоставляет удобный доступ к категориям и кодам. Рассмотрим следующий объект Series:

In [251]: s = pd.Series(['a', 'b', 'c', 'd'] * 2)

In [252]: cat_s = s.astype('category')

In [253]: cat_s
Out[253]:
0    a
1    b
2    c
3    d
4    a
5    b
6    c
7    d
dtype: category
Categories (4, object): ['a', 'b', 'c', 'd']

Специальный акцессор cat открывает доступ к категориальным методам:

In [254]: cat_s.cat.codes
Out[254]:
0    0
1    1
2    2
3    3
4    0
5    1
6    2
7    3
dtype: int8

In [255]: cat_s.cat.categories
Out[255]: Index(['a', 'b', 'c', 'd'], dtype='object')

Допустим, что нам известно, что множество категорий для этих данных не ограничивается четырьмя наблюдаемыми в конкретном наборе значениями. Чтобы изменить множество категорий, воспользуемся методом set_categories: