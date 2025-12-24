---
source_image: page_450.png
page_number: 450
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 40.35
tokens: 11882
characters: 1989
timestamp: 2025-12-24T01:55:42.387993
finish_reason: stop
---

<table>
  <tr>
    <th>Модуль</th>
    <th>Функция</th>
    <th>Описание</th>
  </tr>
  <tr>
    <td colspan="3">itertools filterfalse(predicate, it)</td>
    <td>То же, что filter, но логика инвертирована: отдаются элементы, для которых предиката принимает похожее на ложь значение</td>
  </tr>
  <tr>
    <td colspan="3">itertools islice(it, stop) ИЛИ islice(it, start, stop, step=1)</td>
    <td>Отдает элементы из среза it по аналогии с s[:stop] или s[start:stop:step], только it может быть произвольным итерируемым объектом, а операция ленивая</td>
  </tr>
  <tr>
    <td colspan="3">itertools takewhile(predicate, it)</td>
    <td>Отдает элементы, пока predicate принимает похожее на истину значение, затем останавливается, больше никаких проверок не делается</td>
  </tr>
</table>

В распечатке сеанса оболочки ниже показано применение всех функций из табл. 14.1

Пример 14.14. Примеры фильтрующих генераторных функций

```python
>>> def vowel(c):
...     return c.lower() in 'aeiou'
...
>>> list(filter(vowel, 'Aardvark'))
['A', 'a', 'a']
>>> import itertools
>>> list(itertools.filterfalse(vowel, 'Aardvark'))
['r', 'd', 'v', 'r', 'k']
>>> list(itertools.dropwhile(vowel, 'Aardvark'))
['r', 'd', 'v', 'a', 'r', 'k']
>>> list(itertools.takewhile(vowel, 'Aardvark'))
['A', 'a']
>>> list(itertools.compress('Aardvark', (1,0,1,1,0,1)))
['A', 'r', 'd', 'a']
>>> list(itertools.islice('Aardvark', 4))
['A', 'a', 'r', 'd']
>>> list(itertools.islice('Aardvark', 4, 7))
['v', 'a', 'r']
>>> list(itertools.islice('Aardvark', 1, 7, 2))
['a', 'd', 'a']
```

Следующая группа — отображающие генераторы: они отдают элементы, вычисленные для каждого элемента входного итерируемого объекта — или нескольких таких объектов, как в случае map и starmap. Генераторы, перечисленные в табл. 14.2, отдают по одному результату для каждого элемента входного итерируемого объекта. Если на вход подается несколько итерируемых объектов, то процесс прекращается, как только будет исчерпан хотя бы один из них.