---
source_image: page_061.png
page_number: 61
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 32.68
tokens: 7661
characters: 1765
timestamp: 2025-12-24T02:41:36.343300
finish_reason: stop
---

Имея экземпляр datetime, можно получить из него объекты date и time путем вызова одноименных методов:

In [117]: dt.date()
Out[117]: datetime.date(2011, 10, 29)

In [118]: dt.time()
Out[118]: datetime.time(20, 30, 21)

Метод strftime форматирует объект datetime, представляя его в виде строки:

In [119]: dt.strftime("%Y-%m-%d %H:%M")
Out[119]: '2011-10-29 20:30'

Чтобы разобрать строку и представить ее в виде объекта datetime, нужно вызвать функцию strptime:

In [120]: datetime.strptime("20091031", "%Y%m%d")
Out[120]: datetime.datetime(2009, 10, 31, 0, 0)

В табл. 11.2 приведен полный перечень спецификаций формата.
При агрегировании или еще какой-то группировке временных рядов иногда бывает полезно заменить некоторые компоненты даты или времени, например обнулить минуты и секунды, создав новый объект:

In [121]: dt_hour = dt.replace(minute=0, second=0)

In [122]: dt_hour
Out[122]: datetime.datetime(2011, 10, 29, 20, 0)

Поскольку тип datetime.datetime неизменяемый, эти и другие подобные методы порождают новые объекты. Так, в предыдущем примере объект dt не изменяется в результате применения метода replace:

In [123]: dt
Out[123]: datetime.datetime(2011, 10, 29, 20, 30, 21)

Результатом вычитания объектов datetime является объект типа datetime.timedelta:

In [124]: dt2 = datetime(2011, 11, 15, 22, 30)

In [125]: delta = dt2 - dt

In [126]: delta
Out[126]: datetime.timedelta(days=17, seconds=7179)

In [127]: type(delta)
Out[127]: datetime.timedelta

Результат timedelta(17, 7179) показывает, что в timedelta закодировано смещение 17 дней и 7179 секунд.

Сложение объектов timedelta и datetime дает новый объект datetime, отстоящий от исходного на указанный промежуток времени:

In [128]: dt
Out[128]: datetime.datetime(2011, 10, 29, 20, 30, 21)