---
source_image: page_361.png
page_number: 361
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 23.55
tokens: 11571
characters: 1390
timestamp: 2025-12-24T01:51:01.078659
finish_reason: stop
---

Как тестировались подклассы Tombola

лежащие тестированию модули, даже если в дальнейшем они ни разу не упоминаются в коде: классы необходимо загрузить в память.
3 Строим список из _abc_registry (это объект weakSet), чтобы его можно было конкатенировать с результатом, возвращенным __subclasses__().

4 Обходим все найденные подклассы, передавая каждый функции test.

5 Аргумент cls — подлежащий тестированию класс — связывается с именем ConcreteTombola в глобальном пространстве имен, предназначенном для запуска doctest-скрипта.

6 Выводим на печать результат теста, содержащий имя класса, количество выполненных тестов, в том числе завершившихся неудачно, и метку 'OK' или 'FAIL'.

Файл с doctest-скриптами приведен в примере 11.16.

Пример 11.16. tombola_tests.rst: doctest-скрипты для подклассов Tombola

================
Tombola tests
================

Every concrete subclass of Tombola should pass these tests.

Create and load instance from iterable::

    >>> balls = list(range(3))
    >>> globe = ConcreteTombola(balls)
    >>> globe.loaded()
    True
    >>> globe.inspect()
    (0, 1, 2)

Pick and collect balls::

    >>> picks = []
    >>> picks.append(globe.pick())
    >>> picks.append(globe.pick())
    >>> picks.append(globe.pick())

Check state and results::

    >>> globe.loaded()
    False
    >>> sorted(picks) == balls
    True

Reload::

    >>> globe.load(balls)