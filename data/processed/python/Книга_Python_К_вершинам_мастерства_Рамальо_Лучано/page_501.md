---
source_image: page_501.png
page_number: 501
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 46.50
tokens: 11735
characters: 1679
timestamp: 2025-12-24T01:58:12.741055
finish_reason: stop
---

Возврат значения из сопрограммы

count += 1
average = total/count
return Result(count, average) ②

① Чтобы вернуть значение, сопрограмма должна завершиться нормально, поэтому в новой версии averager проверяется условие выхода из цикла подсчета среднего.
② Возвращаем именованный кортеж, содержащий count и average. До версии Python 3.3 возврат значения из генераторной функции считался ошибкой.

Чтобы увидеть, как работает новая версия averager, мы можем проследить за ее выполнением в оболочке (пример 16.14).

Пример 16.14. coroaverager2.py: doctest-скрипт, иллюстрирующий поведение averager

>>> coro_avg = averager()
>>> next(coro_avg)
>>> coro_avg.send(10) ①
>>> coro_avg.send(30)
>>> coro_avg.send(6.5)
>>> coro_avg.send(None) ②
Traceback (most recent call last):
...
StopIteration: Result(count=3, average=15.5)

① Эта версия не отдает значений.
② Отправка None приводит к выходу из цикла и завершению сопрограммы с возвратом результата. Как обычно, генератор возбуждает исключение StopIteration. Возвращенное значение можно прочитать из атрибута исключения value.

Отметим, что значение выражения return передается вызывающей стороне «контрабандой» — в виде атрибута объекта-исключения StopIteration. Это не совсем честно, но сохраняет существующее поведение объектов-генераторов: возбуждение StopIteration по исчерпании.

В примере 16.15 показано, как получить значение, возвращенное сопрограммой.

Пример 16.15. Перехват StopIteration позволяет получить значение, возвращенное averager

>>> coro_avg = averager()
>>> next(coro_avg)
>>> coro_avg.send(10)
>>> coro_avg.send(30)
>>> coro_avg.send(6.5)
>>> try:
...     coro_avg.send(None)
... except StopIteration as exc: