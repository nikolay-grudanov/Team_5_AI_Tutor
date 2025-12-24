---
source_image: page_668.png
page_number: 668
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 43.15
tokens: 11703
characters: 1669
timestamp: 2025-12-24T02:05:35.742909
finish_reason: stop
---

Пример 20.13. Метод является непереопределяющим дескриптором

```python
>>> obj = Managed()
>>> obj.spam   # 1
<bound method Managed.spam of <descriptorkinds.Managed object at 0x74c80c>>
>>> Managed.spam   # 2
<function Managed.spam at 0x734734>
>>> obj.spam = 7   # 3
>>> obj.spam
7
```

1 Чтение obj.spam возвращает объект, представляющий связанный метод.
2 Однако чтение Managed.spam возвращает функцию.
3 Присваивание атрибуту obj.spam маскирует атрибут класса, делая метод spam недоступным через объект obj.

Поскольку в функциях не реализован метод __set__, они являются непереопределяющими дескрипторами, что видно из последней строки примера 20.13.

Еще отметим, что в примере 20.13 чтение obj.spam и Managed.spam дает разные объекты. Как для любых дескрипторов, метод __get__ функции возвращает ссылку на себя, если доступ осуществляется через управляемый класс. Но при доступе через экземпляр метод __get__ функции возвращает объект связанного метода: вызываемый объект, который обертывает функцию и связывает управляемый экземпляр (например, obj) с первым аргументом функции (т. е. self) — точно также, как делает функция functools.partial (см. раздел «Фиксация аргументов с помощью functools.partial» главы 5).

Чтобы лучше понять этот механизм, рассмотрим пример 20.14.

Пример 20.14. method_is_descriptor.py: класс Text, наследующий UserString

import collections

class Text(collections.UserString):

    def __repr__(self):
        return 'Text({!r})'.format(self.data)

    def reverse(self):
        return self[::-1]

Исследуем работу метода Text.reverse.

Пример 20.15. Эксперименты с методом

```python
>>> word = Text('forward')
>>> word   # 1
```