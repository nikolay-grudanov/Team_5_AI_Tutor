---
source_image: page_277.png
page_number: 277
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 23.13
tokens: 7466
characters: 1381
timestamp: 2025-12-24T02:47:30.193326
finish_reason: stop
---

Out[125]:
    a   b   c
0  1.0 NaN  2.0
1  4.0  2.0  6.0
2  5.0  4.0 10.0
3  3.0  6.0 14.0
4  7.0  8.0 NaN

В результате combine_first применительно к объектам DataFrame будут присутствовать имена всех столбцов.

8.3. Изменение формы и поворот

Существует ряд фундаментальных операций реорганизации табличных данных. Иногда их называют изменением формы (reshape), а иногда — поворотом (pivot).

Изменение формы с помощью иерархического индексирования

Иерархическое индексирование дает естественный способ реорганизовать данные в DataFrame. Есть два основных действия:

stack
Это «поворот», который переносит данные из столбцов в строки.

unstack
Обратный поворот, который переносит данные из строк в столбцы.

Проиллюстрирую эти операции на примерах. Рассмотрим небольшой DataFrame, в котором индексы строк и столбцов — массивы строк.

In [126]: data = pd.DataFrame(np.arange(6).reshape((2, 3)),
    ....: index=pd.Index(["Ohio", "Colorado"], name="state"),
    ....: columns=pd.Index(["one", "two", "three"], name="number"))

In [127]: data
Out[127]:
      number  one  two  three
state
Ohio        0    1    2
Colorado    3    4    5

Метод stack поворачивает таблицу, так что столбцы оказываются строками, и в результате получается объект Series:

In [128]: result = data.stack()

In [129]: result
Out[129]:
state    number
Ohio     one    0
         two    1
         three  2