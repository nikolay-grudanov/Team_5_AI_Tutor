---
source_image: page_186.png
page_number: 186
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 42.73
tokens: 11827
characters: 1915
timestamp: 2025-12-24T01:43:15.004342
finish_reason: stop
---

Пример 5.26. Использование partial позволяет вызывать функцию с двумя аргументами там, где требуется вызываемый объект с одним аргументом

```python
>>> from operator import mul
>>> from functools import partial
>>> triple = partial(mul, 3)  # Создаем новую функцию triple из mul, связав первый аргумент со значением 3.
>>> triple(7)  # Тестируем ее.
21
>>> list(map(triple, range(1, 10)))  # Используем triple совместно с map; mul в этом примере не смогла бы работать с map.
[3, 6, 9, 12, 15, 18, 21, 24, 27]
```

1 Создаем новую функцию triple из mul, связав первый аргумент со значением 3.
2 Тестируем ее.
3 Используем triple совместно с map; mul в этом примере не смогла бы работать с map.

Более полезный пример относится к функции unicode.normalize, с которой мы встречались в разделе «Нормализация Unicode для правильного сравнения» главы 4. Для многих языков перед сравнением или сохранением строки рекомендуется нормализовывать с помощью вызова unicode.normalize('NFC', s). Если это приходится делать часто, то удобно завести функцию nfc, как показано в примере 5.27.

Пример 5.27. Построение вспомогательной функции нормализации Unicode-строк с помощью partial

```python
>>> import unicodedata, functools
>>> nfc = functools.partial(unicodedata.normalize, 'NFC')
>>> s1 = 'café'
>>> s2 = 'cafe\u0301'
>>> s1, s2
('café', 'café')
>>> s1 == s2
False
>>> nfc(s1) == nfc(s2)
True
```

Функция partial принимает в первом аргументе вызываемый объект, а за ним — произвольное число позиционных и именованных аргументов, подлежащих связыванию.

В примере 5.28 демонстрируется использование partial совместно с функцией tag из примера 5.10 для фиксации одного позиционного и одного именованного аргумента.

Пример 5.28. Применение partial к функции tag из примера 5.10

```python
>>> from tagger import tag
>>> tag
<function tag at 0x10206d1e0>  # function tag at 0x10206d1e0
>>> from functools import partial
```