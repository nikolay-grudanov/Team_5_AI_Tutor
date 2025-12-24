---
source_image: page_155.png
page_number: 155
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 28.75
tokens: 7531
characters: 1538
timestamp: 2025-12-24T02:44:09.682026
finish_reason: stop
---

Ниже, в разделе «Выборка из DataFrame с помощью loc и iloc», мы узнаем, что переиндексировать можно также с помощью оператора loc, и многие предпочитают именно этот способ. Он работает, только если все метки нового индекса уже присутствуют в объекте DataFrame (тогда как reindex вставляет отсутствующие данные для новых меток):

In [112]: frame.loc[["a", "d", "c"], ["California", "Texas"]]
Out[112]:
    California Texas
a        2      1
d        8      7
c        5      4

Удаление элементов из оси
Удалить один или несколько элементов из оси просто, если имеется индексный массив или список, не содержащий этих значений, поскольку можно воспользоваться методом reindex или индексированием на базе .loc. Чтобы избавить нас от манипулирования данными и теоретико-множественных операций, метод drop возвращает новый объект, в котором указанные значения удалены из оси:

In [113]: obj = pd.Series(np.arange(5.), index=["a", "b", "c", "d", "e"])

In [114]: obj
Out[114]:
a    0.0
b    1.0
c    2.0
d    3.0
e    4.0
dtype: float64

In [115]: new_obj = obj.drop("c")

In [116]: new_obj
Out[116]:
a    0.0
b    1.0
d    3.0
e    4.0
dtype: float64

In [117]: obj.drop(["d", "c"])
Out[117]:
a    0.0
b    1.0
e    4.0
dtype: float64

В случае DataFrame указанные в аргументе index значения можно удалить из любой оси. Для иллюстрации сначала создадим объект DataFrame:

In [118]: data = pd.DataFrame(np.arange(16).reshape((4, 4)),
.....:     index=["Ohio", "Colorado", "Utah", "New York"],
.....:     columns=["one", "two", "three", "four"])