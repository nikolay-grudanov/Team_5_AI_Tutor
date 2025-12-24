---
source_image: page_175.png
page_number: 175
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 17.98
tokens: 7485
characters: 1035
timestamp: 2025-12-24T02:44:31.163170
finish_reason: stop
---

In [247]: frame = pd.DataFrame({"b": [4, 7, -3, 2], "a": [0, 1, 0, 1]})

In [248]: frame
Out[248]:
   b  a
0  4  0
1  7  1
2 -3  0
3  2  1

In [249]: frame.sort_values("b")
Out[249]:
   b  a
2 -3  0
3  2  1
0  4  0
1  7  1

Для сортировки по нескольким столбцам следует передать список имен:

In [250]: frame.sort_values(["a", "b"])
Out[250]:
   b  a
2 -3  0
0  4  0
3  2  1
1  7  1

Ранжирование заключается в присваивании рангов — от единицы до числа присутствующих в массиве элементов, начиная с наименьшего значения. Для ранжирования применяется метод rank объектов Series и DataFrame; по умолчанию rank обрабатывает равные ранги, присваивая каждой группе средний ранг:

In [251]: obj = pd.Series([7, -5, 7, 4, 2, 0, 4])

In [252]: obj.rank()
Out[252]:
0    6.5
1    1.0
2    6.5
3    4.5
4    3.0
5    2.0
6    4.5
dtype: float64

Ранги можно также присваивать в соответствии с порядком появления в данных:

In [253]: obj.rank(method="first")
Out[253]:
0    6.0
1    1.0
2    7.0
3    4.0
4    3.0
5    2.0
6    5.0
dtype: float64