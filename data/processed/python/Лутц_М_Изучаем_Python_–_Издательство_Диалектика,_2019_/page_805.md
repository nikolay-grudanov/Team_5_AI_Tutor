---
source_image: page_805.png
page_number: 805
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 20.53
tokens: 7537
characters: 1351
timestamp: 2025-12-24T01:32:13.081133
finish_reason: stop
---

В более поздних выпусках Python достичь того же эффекта можно также с помощью встроенной функции sorted:

```python
>>> D = {'a':1, 'b':2, 'c':3, 'd':4, 'e':5, 'f':6, 'g':7}
>>> D
{'f': 6, 'c': 3, 'a': 1, 'g': 7, 'e': 5, 'd': 4, 'b': 2}
>>>
>>> keys = list(D.keys())    # list() требуется в Python 3.x, но не в Python 2.x
>>> keys.sort()
>>> for key in keys:
...     print(key, '=>', D[key])
...
a => 1
b => 2
c => 3
d => 4
e => 5
f => 6
g => 7

>>> for key in sorted(D):    # Лучше в более поздних выпусках Python
...     print(key, '=>', D[key])
```

4. Альтернативные варианты программной логики. Примеры решений показаны ниже. Для шага д присвойте результат 2 ** X переменной за пределами циклов на шагах а и б, после чего используйте ее в цикле. Ваши результаты могут слегка варьироваться; данное упражнение в основном предназначено для того, чтобы дать вам возможность попрактиковаться с альтернативными вариантами кода, поэтому подойдут любые разумные версии:

# a
L = [1, 2, 4, 8, 16, 32, 64]
X = 5
i = 0
while i < len(L):
    if 2 ** X == L[i]:
        print('at index', i)
        break
    i += 1
else:
    print(X, 'not found')

# б
L = [1, 2, 4, 8, 16, 32, 64]
X = 5
for p in L:
    if (2 ** X) == p:
        print((2 ** X), 'was found at', L.index(p))
        break
else:
    print(X, 'not found')

# в
L = [1, 2, 4, 8, 16, 32, 64]
X = 5