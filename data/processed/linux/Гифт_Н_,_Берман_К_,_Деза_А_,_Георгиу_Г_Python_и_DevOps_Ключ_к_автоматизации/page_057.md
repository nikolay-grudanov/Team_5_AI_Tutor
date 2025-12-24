---
source_image: page_057.png
page_number: 57
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 17.19
tokens: 7242
characters: 1176
timestamp: 2025-12-24T03:02:15.290636
finish_reason: stop
---

Для указания этого значения применяется ключевое слово return. Если оператор return в теле функции не описан, она возвращает None:

```python
>>> def no_return():
...     '''Оператор return не описан'''
...     pass
...
>>> result = no_return()
>>> print(result)
None
>>> def return_one():
...     '''Возвращает 1'''
...     return 1
...
>>> result = return_one()
>>> print(result)
1
```

Функции как объекты

Функции являются объектами. Их можно передавать и хранить в структурах данных. Можно описать две функции, поместить их в список, а затем пройти в цикле по этому списку для их вызова:

```python
>>> def double(input):
...     '''Удваивает input'''
...     return input*2
...
>>> double
<function double at 0x107d34ae8>
>>> type(double)
<class 'function'>
>>> def triple(input):
...     '''Утраивает input'''
...     return input*3
...
>>> functions = [double, triple]
>>> for function in functions:
...     print(function(3))
...
6
9
```

Анонимные функции

Если требуется очень маленькая функция, можно с помощью ключевого слова lambda создать безымянную (анонимную) функцию. В общем случае следует ограничить их применение ситуациями, в которых одна функция ожидает