---
source_image: page_806.png
page_number: 806
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 18.65
tokens: 7489
characters: 1507
timestamp: 2025-12-24T01:32:13.080986
finish_reason: stop
---

if (2 ** X) in L:
    print((2 ** X), 'was found at', L.index(2 ** X))
else:
    print(X, 'not found')

# г
X = 5
L = []
for i in range(7): L.append(2 ** i)
print(L)
if (2 ** X) in L:
    print((2 ** X), 'was found at', L.index(2 ** X))
else:
    print(X, 'not found')

# e
X = 5
L = list(map(lambda x: 2**x, range(7)))   # Или [2**x for x in range(7)]
print(L)                                 # list() для вывода всего в Python
3.Х, но не в Python 2.Х

if (2 ** X) in L:
    print((2 ** X), 'was found at', L.index(2 ** X))
else:
    print(X, 'not found')

5. Сопровождение кода. Какого-то фиксированного решения, которое можно было бы привести здесь, не существует; в качестве примера просмотрите в файле mypydoc.py внесенные мною правки в pydoc.py.

Часть IV, "Функции и генераторы"

Упражнения приведены в главе 21.

1. Основы. Здесь нет ничего особенного, но обратите внимание, что использование print (и, следовательно, вашей функции) формально является полиморфной операцией, которая выполняет правильные действия для каждого типа объекта:

% python
>>> def func(x): print(x)
...
>>> func("spam")
spam
>>> func(42)
42
>>> func([1, 2, 3])
[1, 2, 3]
>>> func({'food': 'spam'})
{'food': 'spam'}

2. Аргументы. Ниже приведен пример решения. Не забывайте, что для просмотра результатов тестовых вызовов вы должны применять print, поскольку код в файле отличается от кода, набираемого в интерактивной подсказке; в нормальной ситуации Python не выдает на экран результаты операторов типа выражений в файлах: