---
source_image: page_065.png
page_number: 65
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 19.11
tokens: 7242
characters: 902
timestamp: 2025-12-24T03:02:29.220395
finish_reason: stop
---

...
    yield first
...
>>> f = fib()
>>> next(f)
1
>>> next(f)
1
>>> next(f)
2
>>> next(f)
3

Можно также использовать генераторы в циклах for:

>>> f = fib()
>>> for x in f:
...     print(x)
...     if x > 12:
...         break
...
1
1
2
3
5
8
13

Генераторные включения

Для создания генераторов в одну строку кода можно использовать генераторные включения. Их синтаксис аналогичен списковым включениям, только вместо квадратных скобок применяются круглые:

>>> list_o_nums = [x for x in range(100)]
>>> gen_o_nums = (x for x in range(100))
>>> list_o_nums
[0, 1, 2, 3, ... 97, 98, 99]
>>> gen_o_nums
<generator object <genexpr> at 0x10ea14408>

Даже на таком маленьком примере с помощью метода sys.getsizeof, возвращающего размер объекта в байтах, можно заметить разницу в объемах используемой оперативной памяти:

>>> import sys
>>> sys.getsizeof(list_o_nums)
912
>>> sys.getsizeof(gen_o_nums)
120