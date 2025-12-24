---
source_image: page_346.png
page_number: 346
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 20.97
tokens: 7447
characters: 1058
timestamp: 2025-12-24T02:49:27.395428
finish_reason: stop
---

9    4.5
10   5.5
11   6.5
Name: value, dtype: float64

Для встроенных агрегатных функций мы можем передать их официальное название в виде строки, как в случае метода agg объекта GroupBy:

In [150]: g.transform('mean')
Out[150]:
0    4.5
1    5.5
2    6.5
3    4.5
4    5.5
5    6.5
6    4.5
7    5.5
8    6.5
9    4.5
10   5.5
11   6.5
Name: value, dtype: float64

Как и apply, transform готов работать с функциями, возвращающими Series, но результат должен быть такого же размера, как вход. Например, можно умножить каждую группу на 2, воспользовавшись вспомогательной функцией:

In [151]: def times_two(group):
.....:     return group * 2

In [152]: g.transform(times_two)
Out[152]:
0    0.0
1    2.0
2    4.0
3    6.0
4    8.0
5   10.0
6   12.0
7   14.0
8   16.0
9   18.0
10  20.0
11  22.0
Name: value, dtype: float64

В качестве более сложного примера вычислим ранги элементов в каждой группе в порядке убывания:

In [153]: def get_ranks(group):
.....:     return group.rank(ascending=False)

In [154]: g.transform(get_ranks)
Out[154]:
0    4.0
1    4.0