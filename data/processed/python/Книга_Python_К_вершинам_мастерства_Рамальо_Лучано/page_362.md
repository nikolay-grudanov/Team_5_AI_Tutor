---
source_image: page_362.png
page_number: 362
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 21.30
tokens: 11560
characters: 1311
timestamp: 2025-12-24T01:51:00.990755
finish_reason: stop
---

>>> globe.loaded()
True
>>> picks = [globe.pick() for i in balls]
>>> globe.loaded()
False

Check that 'LookupError' (or a subclass) is the exception thrown when the device is empty::

    >>> globe = ConcreteTombola([])
    >>> try:
    ...     globe.pick()
    ... except LookupError as exc:
    ...     print('OK')
OK

Load and pick 100 balls to verify that they all come out::

    >>> balls = list(range(100))
    >>> globe = ConcreteTombola(balls)
    >>> picks = []
    >>> while globe.inspect():
    ...     picks.append(globe.pick())
    >>> len(picks) == len(balls)
True
    >>> set(picks) == set(balls)
True

Check that the order has changed and is not simply reversed::

    >>> picks != balls
True
    >>> picks[::-1] != balls
True

Примечание: для последних двух тестов существует *очень* небольшая вероятность завершения с ошибкой, даже если реализация корректна.
Вероятность, что 100 шаров случайно будут извлечены в том же порядке, в каком их возвращает inspect, составляет 1/100!, т.е. приблизительно 1.07e-158. Гораздо вероятнее выиграть в Lotto или программисту стать миллиардером.

THE END

Использование метода register на практике

В примере 11.14 мы использовали Tombola.register в качестве декоратора класса. В версиях, предшествующих Python 3.3, такое использование метода register за-