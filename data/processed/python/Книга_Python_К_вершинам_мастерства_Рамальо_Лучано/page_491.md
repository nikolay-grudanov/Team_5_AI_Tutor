---
source_image: page_491.png
page_number: 491
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 35.58
tokens: 11753
characters: 1920
timestamp: 2025-12-24T01:57:34.100393
finish_reason: stop
---

Базовое поведение генератора, используемого в качестве сопрограммы

'GEN_CREATED'
Ожидает начала выполнения.

'GEN_RUNNING'
Выполняется интерпретатором¹.

'GEN_SUSPENDED'
Приостановлена в выражении yield.

'GEN_CLOSED'
Исполнение завершилось.

Из того, что аргумент метода send становится значением ожидающего выражения yield, следует, что вызов вида my_coro.send(42) возможен только в момент, когда сопрограмма приостановлена. Но это не так, если сопрограмма еще не активирована, т. е. находится в состоянии 'GEN_CREATED'. Поэтому обращение к сопрограмме всегда начинается с вызова next(my_coro); или можно вызвать my_coro.send(None) — результат будет точно такой же.

Вот что произойдет, если создать объект сопрограммы и сразу же послать ему значение, отличное от None:

```python
>>> my_coro = simple_coroutine()
>>> my_coro.send(1729)
Traceback (most recent call last):
    File "<stdin>", line 1, in <module>
TypeError: can't send non-None value to a just-started generator
```

Сообщение абсолютно понятно («Не могу послать значение, отличное от None, только что созданному генератору»).

Начальный вызов next(my_coro) часто называют «инициализацией» (priming) сопрограммы (т. е. продвижением ее к первому yield, чтобы дальше можно было работать нормально).

Чтобы лучше прочувствовать поведение сопрограммы, полезно посмотреть, что происходит, когда yield встречается несколько раз.

Пример 16.2. Сопрограмма с двумя yield

```python
>>> def simple_coro2(a):
...     print('-> Started: a =', a)
...     b = yield a
...     print('-> Received: b =', b)
...     c = yield a + b
...     print('-> Received: c =', c)
...
>>> my_coro2 = simple_coro2(14)
>>> from inspect import getgeneratorstate
>>> getgeneratorstate(my_coro2)  # 1
'GEN_CREATED'
```

¹ Это состояние можно увидеть только в многопоточной программе или если объект-генератор вызывает функцию getgeneratorstate для себя самого, что вряд ли имеет смысл.