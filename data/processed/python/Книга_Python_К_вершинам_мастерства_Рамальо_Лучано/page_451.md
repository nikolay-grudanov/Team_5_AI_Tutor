---
source_image: page_451.png
page_number: 451
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 44.48
tokens: 12009
characters: 2025
timestamp: 2025-12-24T01:55:50.335706
finish_reason: stop
---

Таблица 14.2. Отображающие генераторные функции

<table>
  <tr>
    <th>Модуль</th>
    <th>Функция</th>
    <th>Описание</th>
  </tr>
  <tr>
    <td colspan="3">itertools accumulate(it, [func])</td>
    <td>Отдает накопленные суммы; если задана функция func, то отдает результат применения ее к первой паре элементов, затем к первому результату и следующему элементу и т. д.</td>
  </tr>
  <tr>
    <td colspan="3">встроенная enumerate(iterable, start=0)</td>
    <td>Отдает 2-кортежи вида (index, item), где index начинается со значения start, а item извлекается из iterable</td>
  </tr>
  <tr>
    <td colspan="3">встроенная map(func, it1, [it2, ..., itN])</td>
    <td>Применяет func к каждому элементу it и отдает результат; если задано N итерируемых объектов, то func должна принимать N аргументов, и все итерируемые объекты обходятся параллельно</td>
  </tr>
  <tr>
    <td colspan="3">itertools starmap(func, it)</td>
    <td>Применяет func к каждому элементу it и отдает результат; входной итерируемый объект должен отдавать итерируемые элементы iit, а func вызывается в виде func(*iit)</td>
  </tr>
</table>

В примере 14.15 демонстрируется несколько применений функции itertools.accumulate.

Пример 14.15. Примеры применения генераторной функции itertools.accumulate

```python
>>> sample = [5, 4, 2, 8, 7, 6, 3, 0, 9, 1]
>>> import itertools
>>> list(itertools.accumulate(sample)) # 1
[5, 9, 11, 19, 26, 32, 35, 35, 44, 45]
>>> list(itertools.accumulate(sample, min)) # 2
[5, 4, 2, 2, 2, 2, 0, 0, 0]
>>> list(itertools.accumulate(sample, max)) # 3
[5, 5, 5, 8, 8, 8, 8, 9, 9]
>>> import operator
>>> list(itertools.accumulate(sample, operator.mul)) # 4
[5, 20, 40, 320, 2240, 13440, 40320, 0, 0, 0]
>>> list(itertools.accumulate(range(1, 11), operator.mul)) # 5
[1, 2, 6, 24, 120, 720, 5040, 40320, 362880, 3628800]
```

1 Частичные суммы.
2 Частичные минимумы.
3 Частичные максимумы.
4 Частичные произведения.
5 Факториалы от 1! до 10!.

Применение остальных функций из табл. 10.2 иллюстрируется в примере 14.16.