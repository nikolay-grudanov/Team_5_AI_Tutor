---
source_image: page_156.png
page_number: 156
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 31.76
tokens: 7564
characters: 1420
timestamp: 2025-12-24T02:44:13.141048
finish_reason: stop
---

In [119]: data
Out[119]:
    one   two   three   four
Ohio     0     1     2     3
Colorado 4     5     6     7
Utah     8     9    10    11
New York 12    13    14    15

Если вызвать drop, указав последовательность меток, то будут удалены строки с такими метками (ось 0):

In [120]: data.drop(index=["Colorado", "Ohio"])
Out[120]:
    one   two   three   four
Utah     8     9    10    11
New York 12    13    14    15

Чтобы удалить столбцы, используйте именованный аргумент 'columns':

In [121]: data.drop(columns=["two"])
Out[121]:
    one   three   four
Ohio     0     2     3
Colorado 4     6     7
Utah     8    10    11
New York 12    14    15

Столбцы можно удалить также, передав параметры axis=1 (как в NumPy) или axis="columns":

In [122]: data.drop("two", axis=1)
Out[122]:
    one   three   four
Ohio     0     2     3
Colorado 4     6     7
Utah     8    10    11
New York 12    14    15

In [123]: data.drop(["two", "four"], axis="columns")
Out[123]:
    one   three
Ohio     0     2
Colorado 4     6
Utah     8    10
New York 12    14

Доступ по индексу, выборка и фильтрация
Доступ по индексу к объекту Series (obj[...]) работает так же, как для массивов NumPy, с тем отличием, что индексами могут быть не только целые, но любые значения из индекса объекта Series. Вот несколько примеров:

In [124]: obj = pd.Series(np.arange(4.), index=["a", "b", "c", "d"])

In [125]: obj
Out[125]:
a    0.0
b    1.0