---
source_image: page_074.png
page_number: 74
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 21.39
tokens: 7495
characters: 1168
timestamp: 2025-12-24T02:41:45.707390
finish_reason: stop
---

In [85]: d1
Out[85]: {'a': 'some value', 'b': [1, 2, 3, 4]}

Для доступа к элементам, вставки и присваивания применяется такой же синтаксис, как в случае списка или кортежа:

In [86]: d1[7] = "an integer"

In [87]: d1
Out[87]: {'a': 'some value', 'b': [1, 2, 3, 4], 7: 'an integer'}

In [88]: d1["b"]
Out[88]: [1, 2, 3, 4]

Проверка наличия ключа в словаре тоже производится, как для кортежа или списка:

In [89]: "b" in d1
Out[89]: True

Для удаления ключа можно использовать либо ключевое слово del, либо метод pop (который не только удаляет ключ, но и возвращает ассоциированное с ним значение):

In [90]: d1[5] = "some value"

In [91]: d1
Out[91]:
{'a': 'some value',
 'b': [1, 2, 3, 4],
 7: 'an integer',
 5: 'some value'}

In [92]: d1["dummy"] = "another value"

In [93]: d1
Out[93]:
{'a': 'some value',
 'b': [1, 2, 3, 4],
 7: 'an integer',
 5: 'some value',
 'dummy': 'another value'}

In [94]: del d1[5]

In [95]: d1
Out[95]:
{'a': 'some value',
 'b': [1, 2, 3, 4],
 7: 'an integer',
 'dummy': 'another value'}

In [96]: ret = d1.pop("dummy")

In [97]: ret
Out[97]: 'another value'

In [98]: d1
Out[98]: {'a': 'some value', 'b': [1, 2, 3, 4], 7: 'an integer'}