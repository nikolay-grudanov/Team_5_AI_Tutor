---
source_image: page_179.png
page_number: 179
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 50.01
tokens: 11861
characters: 2286
timestamp: 2025-12-24T01:43:09.316057
finish_reason: stop
---

Получение информации о параметрах

VAR_KEYWORD
Словарь именованных параметров.

KEYWORD_ONLY
Чисто именованный параметр (появились в Python 3).

POSITIONAL_ONLY
Чисто позиционный параметр; в настоящее время в синтаксисе объявления функций не поддерживаются, но встречаются в существующих функциях, написанных на C (например, divmod), которые не принимают именованных параметров.

Помимо атрибутов name, default и kind, у объектов типа inspect.Parameter есть атрибут annotation, который обычно равен inspect._empty, но может содержать метаданные сигнатуры, задаваемые с помощью нового синтаксиса аннотаций в Python 3 (аннотации рассматриваются в следующем разделе).

У объекта inspect.Signature имеется метод bind, который принимает любое число аргументов и связывает их с параметрами, указанными в сигнатуре, следуя обычным правилам сопоставления фактических аргументов с формальными параметрами. Каркас может использовать эту возможность для проверки аргументов до фактического вызова функции. См. пример 5.18.

Пример 5.18. Связывание сигнатуры функции tag из примера 5.10 со словарем аргументов

```python
>>> import inspect
>>> sig = inspect.signature(tag)    # Получаем сигнатуру функции tag из примера 5.10.
>>> my_tag = {'name': 'img', 'title': 'Sunset Boulevard', 'src': 'sunset.jpg', 'cls': 'framed'}   # Передаем словарь аргументов методу .bind().
>>> bound_args = sig.bind(**my_tag)  # Возвращается объект типа inspect.BoundArguments.
<inspect.BoundArguments object at 0x...>
>>> for name, value in bound_args.arguments.items():   # Обходим все элементы в объекте bound_args.arguments, имеющем тип OrderedDict, и выводим имена и значения аргументов.
    print(name, '=', value)
...
name = img
cls = framed
attrs = {'title': 'Sunset Boulevard', 'src': 'sunset.jpg'}
>>> del my_tag['name']   # Удаляем обязательный аргумент из my_tag.
>>> bound_args = sig.bind(**my_tag)   # Traceback (most recent call last):
...
TypeError: 'name' parameter lacking default value
```

1 Получаем сигнатуру функции tag из примера 5.10.
2 Передаем словарь аргументов методу .bind().
3 Возвращается объект типа inspect.BoundArguments.
4 Обходим все элементы в объекте bound_args.arguments, имеющем тип OrderedDict, и выводим имена и значения аргументов.
5 Удаляем обязательный аргумент из my_tag.