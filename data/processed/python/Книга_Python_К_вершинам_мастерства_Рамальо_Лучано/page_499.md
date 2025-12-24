---
source_image: page_499.png
page_number: 499
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 41.06
tokens: 11668
characters: 1657
timestamp: 2025-12-24T01:58:02.418103
finish_reason: stop
---

Завершение сопрограммы и обработка исключений

Пример 16.9. Активация и завершение demo_exc_handling без исключения

```python
>>> exc_coro = demo_exc_handling()
>>> next(exc_coro)
-> coroutine started
>>> exc_coro.send(11)
-> coroutine received: 11
>>> exc_coro.send(22)
-> coroutine received: 22
>>> exc_coro.close()
>>> from inspect import getgeneratorstate
>>> getgeneratorstate(exc_coro)
'GEN_CLOSED'
```

Если в demo_exc_handling методом throw передано исключение DemoException, то оно обрабатывается, и сопрограмма продолжается, как показано в примере 16.10.

Пример 16.10. Возбуждение исключения DemoException в demo_exc_handling не приводит к выходу из нее

```python
>>> exc_coro = demo_exc_handling()
>>> next(exc_coro)
-> coroutine started
>>> exc_coro.send(11)
-> coroutine received: 11
>>> exc_coro.throw(DemoException)
*** DemoException handled. Continuing...
>>> getgeneratorstate(exc_coro)
'GEN_SUSPENDED'
```

С другой стороны, если возбужденное в сопрограмме исключение не обработано, то она останавливается и переходит в состояние 'GEN_CLOSED'.

Пример 16.11. Сопрограмма завершается, если не может обработать возбужденное в ней исключение

```python
>>> exc_coro = demo_exc_handling()
>>> next(exc_coro)
-> coroutine started
>>> exc_coro.send(11)
-> coroutine received: 11
>>> exc_coro.throw(ZeroDivisionError)
Traceback (most recent call last):
    ...
ZeroDivisionError
>>> getgeneratorstate(exc_coro)
'GEN_CLOSED'
```

Если необходимо, чтобы вне зависимости от способа завершения сопрограммы был выполнен какой-то код очистки, то соответствующую часть тела сопрограммы нужно обернуть блоком try/finally, как показано в примере 16.12.