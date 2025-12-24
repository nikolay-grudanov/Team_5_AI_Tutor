---
source_image: page_479.png
page_number: 479
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 27.26
tokens: 7661
characters: 1657
timestamp: 2025-12-24T02:53:31.424848
finish_reason: stop
---

In [123]: arr[::2].sort(1) # отсортировать несколько строк

In [124]: arr[:, :-1] < arr[:, 1:]
Out[124]:
array([[ True,  True,  True,  True],
       [False,  True,  True, False],
       [ True,  True,  True,  True],
       [False,  True,  True, False],
       [ True,  True,  True,  True]])

Отметим, что logical_and.reduce эквивалентно методу all.
Функция accumulate соотносится с reduce, как cumsum с sum. Она порождает массив того же размера, содержащий промежуточные «аккумулированные» значения:

In [126]: arr = np.arange(15).reshape((3, 5))

In [127]: np.add.accumulate(arr, axis=1)
Out[127]:
array([[ 0,   1,   3,   6,  10],
       [ 5,  11,  18,  26,  35],
       [10,  21,  33,  46,  60]])

Функция outer вычисляет прямое произведение двух массивов:

In [128]: arr = np.arange(3).repeat([1, 2, 2])

In [129]: arr
Out[129]: array([0, 1, 1, 2, 2])

In [130]: np.multiply.outer(arr, np.arange(5))
Out[130]:
array([[0, 0, 0, 0, 0],
       [0, 1, 2, 3, 4],
       [0, 1, 2, 3, 4],
       [0, 2, 4, 6, 8],
       [0, 2, 4, 6, 8]])

Размерность массива, возвращенного outer, является результатом конкатенации размерностей его параметров:

In [131]: x, y = rng.standard_normal((3, 4)), rng.standard_normal(5)

In [132]: result = np.subtract.outer(x, y)

In [133]: result.shape
Out[133]: (3, 4, 5)

Последний метод, reduceat, выполняет «локальную редукцию», т. е. по существу операцию groupby, в которой агрегируется сразу несколько срезов массива. Он принимает последовательность «границ интервалов», описывающую, как разбивать и агрегировать значения:

In [134]: arr = np.arange(10)

In [135]: np.add.reduceat(arr, [0, 5, 8])
Out[135]: array([10, 18, 17])