---
source_image: page_159.png
page_number: 159
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 23.56
tokens: 7470
characters: 1337
timestamp: 2025-12-24T02:44:05.731550
finish_reason: stop
---

С помощью меток можно также производить вырезание, но оно отличается от обычного вырезания в Python тем, что конечная точка включается:

In [141]: obj2.loc["b":"c"]
Out[141]:
    b   2
    c   3
dtype: int64

Присваивание с помощью этих методов модифицирует соответствующий участок Series:

In [142]: obj2.loc["b":"c"] = 5

In [143]: obj2
Out[143]:
    a   1
    b   5
    c   5
dtype: int64

Начинающие часто допускают ошибку: пытаются вызывать loc или iloc как функции вместо использования синтаксиса индексирования с квадратными скобками. Эта нотация применяется, чтобы можно было использовать операции вырезания и индексировать по нескольким осям при работе с объектами DataFrame.

Обращение по индексу к DataFrame предназначено для получения одного или нескольких столбцов путем задания одного значения или последовательности:

In [144]: data = pd.DataFrame(np.arange(16).reshape((4, 4)),
.....: index=["Ohio", "Colorado", "Utah", "New York"],
.....: columns=["one", "two", "three", "four"])

In [145]: data
Out[145]:
      one  two  three  four
Ohio    0    1     2     3
Colorado 4    5     6     7
Utah    8    9    10    11
New York 12  13    14    15

In [146]: data["two"]
Out[146]:
Ohio    1
Colorado 5
Utah    9
New York 13
Name: two, dtype: int64

In [147]: data[["three", "one"]]
Out[147]:
      three  one
Ohio     2    0