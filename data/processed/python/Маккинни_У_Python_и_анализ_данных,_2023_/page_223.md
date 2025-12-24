---
source_image: page_223.png
page_number: 223
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 22.33
tokens: 7490
characters: 1359
timestamp: 2025-12-24T02:45:58.295935
finish_reason: stop
---

In [67]: data.replace([-999, -1000], np.nan)
Out[67]:
    0   1.0
    1   NaN
    2   2.0
    3   NaN
    4   NaN
    5   3.0
dtype: float64

Если для каждого заменяемого значения нужно свое заменяющее, передайте список замен:

In [68]: data.replace([-999, -1000], [np.nan, 0])
Out[68]:
    0   1.0
    1   NaN
    2   2.0
    3   NaN
    4   0.0
    5   3.0
dtype: float64

В аргументе можно передавать также словарь:

In [69]: data.replace({-999: np.nan, -1000: 0})
Out[69]:
    0   1.0
    1   NaN
    2   2.0
    3   NaN
    4   0.0
    5   3.0
dtype: float64

Метод data.replace – не то же самое, что метод data.str.replace, который выполняет поэлементную замену строки. Методы работы со строками будут рассмотрены при обсуждении объекта Series ниже в этой главе.

Переименование индексов осей
Как и значения в объекте Series, метки осей можно преобразовывать с помощью функции или отображения, порождающего новые объекты с другими метками. Оси можно также модифицировать на месте, не создавая новую структуру данных. Вот простой пример:

In [70]: data = pd.DataFrame(np.arange(12).reshape((3, 4)),
    ....:                 index=["Ohio", "Colorado", "New York"],
    ....:                 columns=["one", "two", "three", "four"])

Как и у объекта Series, у индексов осей имеется метод map:

In [71]: def transform(x):
    ....:     return x[:4].upper()