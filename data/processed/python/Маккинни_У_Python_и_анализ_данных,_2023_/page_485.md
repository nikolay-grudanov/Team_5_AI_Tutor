---
source_image: page_485.png
page_number: 485
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 30.09
tokens: 7688
characters: 1582
timestamp: 2025-12-24T02:53:45.143128
finish_reason: stop
---

In [179]: values = np.array([5, 0, 1, 3, 2])

In [180]: indexer = values.argsort()

In [181]: indexer
Out[181]: array([1, 2, 4, 3, 0])

In [182]: values[indexer]
Out[182]: array([0, 1, 2, 3, 5])

А в следующем, более сложном примере двумерный массив переупорядочивается по первой строке:

In [183]: arr = rng.standard_normal((3, 5))

In [184]: arr[0] = values

In [185]: arr
Out[185]:
array([[ 5.   ,  0.   ,  1.   ,  3.   ,  2.   ],
       [-0.7503, -2.1268, -1.391 , -0.4922,  0.4505],
       [ 0.8926, -1.0479,  0.9553,  0.2936,  0.5379]])

In [186]: arr[:, arr[0].argsort()]
Out[186]:
array([[ 0.   ,  1.   ,  2.   ,  3.   ,  5.   ],
       [-2.1268, -1.391 ,  0.4505, -0.4922, -0.7503],
       [-1.0479,  0.9553,  0.5379,  0.2936,  0.8926]])

Метод lexsort аналогичен argsort, но выполняет косвенную лексикографическую сортировку по нескольким массивам ключей. Пусть требуется отсортировать данные, идентифицируемые именем и фамилией:

In [187]: first_name = np.array(['Bob', 'Jane', 'Steve', 'Bill', 'Barbara'])

In [188]: last_name = np.array(['Jones', 'Arnold', 'Arnold', 'Jones', 'Walters'])

In [189]: sorter = np.lexsort((first_name, last_name))

In [190]: sorter
Out[190]: array([1, 2, 3, 0, 4])

In [191]: list(zip(last_name[sorter], first_name[sorter]))
Out[191]:
[('Arnold', 'Jane'),
 ('Arnold', 'Steve'),
 ('Jones', 'Bill'),
 ('Jones', 'Bob'),
 ('Walters', 'Barbara')]

Поначалу метод lexsort может вызвать недоумение, потому что первым для сортировки используется ключ, указанный в последнем массиве. Как видите, ключ last_name использовался раньше, чем first_name.