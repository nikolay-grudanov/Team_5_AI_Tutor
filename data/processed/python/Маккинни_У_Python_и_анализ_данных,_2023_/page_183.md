---
source_image: page_183.png
page_number: 183
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 23.69
tokens: 7441
characters: 1266
timestamp: 2025-12-24T02:44:51.407478
finish_reason: stop
---

In [290]: obj = pd.Series(["c", "a", "d", "a", "a", "b", "b", "c", "c"])

Метод unique возвращает массив уникальных значений в Series:

In [291]: uniques = obj.unique()

In [292]: uniques
Out[292]: array(['c', 'a', 'd', 'b'], dtype=object)

Уникальные значения необязательно возвращаются в отсортированном порядке, но могут быть отсортированы впоследствии, если это необходимо (uniques.sort()). Метод value_counts вычисляет объект Series, содержащий частоты встречаемости значений:

In [293]: obj.value_counts()
Out[293]:
c    3
a    3
b    2
d    1
dtype: int64

Для удобства этот объект отсортирован по значениям в порядке убывания. Функция value_counts может быть также вызвана как метод pandas верхнего уровня и в таком случае применима к массивам NumPy и другим последовательностям Python:

In [294]: pd.value_counts(obj.to_numpy(), sort=False)
Out[294]:
c    3
a    3
d    1
b    2
dtype: int64

Метод isin вычисляет булев вектор членства в множестве и может быть полезен для фильтрации набора данных относительно подмножества значений в объекте Series или столбце DataFrame:

In [295]: obj
Out[295]:
0    c
1    a
2    d
3    a
4    a
5    b
6    b
7    c
8    c
dtype: object

In [296]: mask = obj.isin(["b", "c"])

In [297]: mask
Out[297]:
0   True
1  False