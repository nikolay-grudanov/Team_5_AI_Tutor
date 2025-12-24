---
source_image: page_565.png
page_number: 565
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 35.87
tokens: 7792
characters: 2274
timestamp: 2025-12-24T01:25:00.018157
finish_reason: stop
---

def union(*args):
    res = []
    for seq in args:
        for x in seq:
            if not x in res:
                res.append(x)
    return res

# Для всех аргументов
# Для всех узлов
# Добавить новые элементы к результату

Из-за того, что такие инструменты заслуживают многократного применения (и слишком объемные, чтобы повторно набирать их код в интерактивной подсказке), мы сохраним функции в файле модуля по имени inter2.py (если вы забыли, как работают модули и импортирование, тогда освежите в памяти введение в главе 3 или дождитесь полного изложения в части V). В обеих функциях аргументы, переданные при вызове, поступают в виде кортежа args. Подобно первоначальной функции intersect обе работают на последовательностях любого типа. Вот как функции обрабатывают строки, разнородные типы и более двух последовательностей:

% python
>>> from inter2 import intersect, union
>>> s1, s2, s3 = "SPAM", "SCAM", "SLAM"
>>> intersect(s1, s2), union(s1, s2)           # Два операнда
(['S', 'A', 'M'], ['S', 'P', 'A', 'M', 'C'])
>>> intersect([1, 2, 3], (1, 4))                # Разнородные типы
[1]
>>> intersect(s1, s2, s3)                       # Три операнда
['S', 'A', 'M']
>>> union(s1, s2, s3)
['S', 'P', 'A', 'M', 'C', 'L']

Для более основательного тестирования мы написали функцию для применения двух инструментов к аргументам в разном порядке, используя простую методику тасования, которая встречалась в главе 13. На каждой итерации цикла она посредством нарезания перемещает первый элемент в конец, применяет * для распаковки аргументов и выполняет сортировку, чтобы результаты можно было сравнивать:

>>> def tester(func, items, trace=True):
    for i in range(len(items)):
        items = items[1:] + items[:1]
        if trace: print(items)
        print(sorted(func(*items)))

>>> tester(intersect, ('a', 'abcdefg', 'abdst', 'albmcnd'))
('abcdefg', 'abdst', 'albmcnd', 'a')
['a']
('abdst', 'albmcnd', 'a', 'abcdefg')
['a']
('albmcnd', 'a', 'abcdefg', 'abdst')
['a']
('a', 'abcdefg', 'abdst', 'albmcnd')
['a']

>>> tester(union, ('a', 'abcdefg', 'abdst', 'albmcnd'), False)
['a', 'b', 'c', 'd', 'e', 'f', 'g', 'l', 'm', 'n', 's', 't']
['a', 'b', 'c', 'd', 'e', 'f', 'g', 'l', 'm', 'n', 's', 't']
['a', 'b', 'c', 'd', 'e', 'f', 'g', 'l', 'm', 'n', 's', 't']