---
source_image: page_416.png
page_number: 416
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 34.28
tokens: 11802
characters: 1739
timestamp: 2025-12-24T01:53:51.827520
finish_reason: stop
---

Глава 13. Перегрузка операторов: как правильно?

Чтобы продемонстрировать код оператора «на месте», мы расширим класс BingoCage из примера 11.12, реализовав в нем методы __add__ и __iadd__.
Назовем подкласс AddableBingoCage. В примере 13.16 показано, какое поведение мы ожидаем от оператора +.

Пример 13.16. При создании объекта AddableBingoCage можно задать строку

```python
>>> vowels = 'AEIOU'
>>> globe = AddableBingoCage(vowels) ①
>>> globe.inspect()
('A', 'E', 'I', 'O', 'U')
>>> globe.pick() in vowels ②
True
>>> len(globe.inspect()) ③
4
>>> globe2 = AddableBingoCage('XYZ') ④
>>> globe3 = globe + globe2
>>> len(globe3.inspect()) ⑤
7
>>> void = globe + [10, 20] ⑥
Traceback (most recent call last):
    ...
TypeError: unsupported operand type(s) for +: 'AddableBingoCage' and 'list'
```

① Создаем объект globe с пятью элементами (все гласные буквы).
② Извлекаем один элемент и проверяем, что это гласная.
③ Убеждаемся, что количество элементов в globe уменьшилось до четырех.
④ Создаем второй экземпляр с тремя элементами.
⑤ Создаем третий экземпляр, складывая первые два. В этом экземпляре семь элементов.
⑥ Попытка сложить AddableBingoCage со списком приводит к исключению TypeError. Такое сообщение интерпретатор Python генерирует, когда наш метод __add__ возвращает NotImplemented.

Объект AddableBingoCage изменяемый, и в примере 13.17 показано, как он ведет себя после добавления метода __iadd__.

Пример 13.17. Существующий объект AddableBingoCage можно модифицировать с помощью оператора += (продолжение примера 13.16)

```python
>>> globe_orig = globe ①
>>> len(globe.inspect()) ②
4
>>> globe += globe2 ③
>>> len(globe.inspect())
7
>>> globe += ['M', 'N'] ④
>>> len(globe.inspect())
9
>>> globe is globe_orig ⑤
True
```