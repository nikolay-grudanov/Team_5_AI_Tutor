---
source_image: page_076.png
page_number: 76
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 32.89
tokens: 7482
characters: 1331
timestamp: 2025-12-24T00:53:28.555745
finish_reason: stop
---

76 Глава 2 • Введение в библиотеку NumPy

In[48]: x = np.array([1, 2, 3])
    grid = np.array([[9, 8, 7],
                     [6, 5, 4]])

    # Объединяет массивы по вертикали
    np.vstack([x, grid])

Out[48]: array([[1, 2, 3],
                [9, 8, 7],
                [6, 5, 4]])

In[49]: # Объединяет массивы по горизонтали
    y = np.array([[99],
                  [99]])
    np.hstack([grid, y])

Out[49]: array([[ 9,  8,  7, 99],
                [ 6,  5,  4, 99]])

Функция np.dstack аналогично объединяет массивы по третьей оси.

Разбиение массивов

Противоположностью слияния является разбиение, выполняемое с помощью функций np.split, np.hsplit и np.vsplit. Каждой из них необходимо передавать список индексов, задающих точки раздела:

In[50]: x = [1, 2, 3, 99, 99, 3, 2, 1]
    x1, x2, x3 = np.split(x, [3, 5])
    print(x1, x2, x3)

[1 2 3] [99 99] [3 2 1]

Обратите внимание, что N точек раздела означают N + 1 подмассив. Соответствующие функции np.hsplit и np.vsplit действуют аналогично:

In[51]: grid = np.arange(16).reshape((4, 4))
    grid

Out[51]: array([[ 0,  1,  2,  3],
                [ 4,  5,  6,  7],
                [ 8,  9, 10, 11],
                [12, 13, 14, 15]])

In[52]: upper, lower = np.vsplit(grid, [2])
    print(upper)
    print(lower)
[[0 1 2 3]
 [4 5 6 7]]
[[ 8  9 10 11]
 [12 13 14 15]]