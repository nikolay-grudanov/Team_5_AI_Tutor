---
source_image: page_630.png
page_number: 630
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 24.33
tokens: 7530
characters: 1817
timestamp: 2025-12-24T01:26:48.401917
finish_reason: stop
---

За счет выноса генерации значений во внешний инструмент функция tester становится проще:

```python
>>> from scramble import scramble
>>> from inter2 import intersect, union
>>>
>>> def tester(func, items, trace=True):
    for args in scramble(items):
        if trace: print(args)
        print(sorted(func(*args)))
>>> tester(intersect, ('aab', 'abcde', 'ababab'))
('aab', 'abcde', 'ababab')
['a', 'b']
('abcde', 'ababab', 'aab')
['a', 'b']
('ababab', 'aab', 'abcde')
['a', 'b']
>>> tester(intersect, ([1, 2], [2, 3, 4], [1, 6, 2, 7, 3]), False)
[2]
[2]
[2]
```

Перестановки: все возможные комбинации

С описанными методиками связаны многие другие применения в реальных приложениях — взять хотя бы генерацию вложений в сообщении электронной почты или точек, подлежащих отображению в графическом пользовательском интерфейсе. Более того, другие виды перемешивания последовательностей играют центральную роль в других приложениях, начиная с поисковых и заканчивая математическими. В том виде как есть, наша функция перемешивания последовательностей выполняет простое переупорядочивание, но определенным программам нужен более полный набор всех возможных порядков, который мы получаем из перестановок, производимых с использованием рекурсивных функций в формах построителя списка и генератора из следующего файла модуля:

```python
# Файл permute.py
def permutel(seq):
    if not seq:
        return [seq]
    else:
        res = []
        for i in range(len(seq)):
            rest = seq[:i] + seq[i+1:]
            for x in permutel(rest):
                res.append(seq[i:i+1] + x)
        return res
def permute2(seq):
    if not seq:
        yield seq
    else:
        for i in range(len(seq)):
            rest = seq[:i] + seq[i+1:]
            for x in permute2(rest):
                yield seq[i:i+1] + x
```