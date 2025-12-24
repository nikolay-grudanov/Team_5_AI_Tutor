---
source_image: page_809.png
page_number: 809
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 25.97
tokens: 7602
characters: 1650
timestamp: 2025-12-24T01:32:26.917465
finish_reason: stop
---

Ищите примеры применения dict.update в главе 8, а дополнительные сведения в руководстве по библиотеке Python или в книге Python Pocket Reference (http://www.oreilly.com/catalog/9780596158088). Для словарей X[:] не работает, т.к. они не являются последовательностями (за подробностями обращайтесь в главу 8). Кроме того, помните о том, что если вместо копирования вы присваиваете (e = d), то генерируете ссылку на разделяемый словарный объект; изменение d изменяет также и e:

def copyDict(old):
    new = {}
    for key in old.keys():
        new[key] = old[key]
    return new

def addDict(d1, d2):
    new = {}
    for key in d1.keys():
        new[key] = d1[key]
    for key in d2.keys():
        new[key] = d2[key]
    return new

% python
>>> from dicts import *
>>> d = {1: 1, 2: 2}
>>> e = copyDict(d)
>>> d[2] = '?'
>>> d
{1: 1, 2: '?'}
>>> e
{1: 1, 2: 2}
>>> x = {1: 1}
>>> y = {2: 2}
>>> z = addDict(x, y)
>>> z
{1: 1, 2: 2}

6. См. упражнение 5.

7. Дополнительные примеры сопоставления аргументов. Далее представлено взаимодействие, которое вы должны получить, вместе с поясняющими комментариями:

def f1(a, b): print(a, b)    # Нормальные аргументы
def f2(a, *b): print(a, b)   # Переменное количество позиционных аргументов
def f3(a, **b): print(a, b)  # Переменное количество ключевых аргументов
def f4(a, *b, **c): print(a, b, c)  # Смешанные режимы
def f5(a, b=2, c=3): print(a, b, c)  # Стандартные значения
def f6(a, b=2, *c): print(a, b, c)  # Стандартные значения и переменное
                                    # кол-во позиционных аргументов

% python
>>> f1(1, 2)      # Сопоставляются по позиции (порядок имеет значение)
1 2