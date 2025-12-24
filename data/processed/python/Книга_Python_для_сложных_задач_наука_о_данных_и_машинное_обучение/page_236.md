---
source_image: page_236.png
page_number: 236
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 33.43
tokens: 7598
characters: 2016
timestamp: 2025-12-24T00:57:36.449637
finish_reason: stop
---

Для меток даты/времени библиотека Pandas предоставляет тип данных Timestamp. Этот тип является заменой для нативного типа данных datetime языка Python, он основан на более эффективном типе данных numpy.datetime64. Соответствующая индексная конструкция — DatetimeIndex.

Для периодов времени библиотека Pandas предоставляет тип данных Period. Этот тип на основе типа данных numpy.datetime64 кодирует интервал времени фиксированной периодичности. Соответствующая индексная конструкция — PeriodIndex.

Для временных дельт (продолжительностей) библиотека Pandas предоставляет тип данных Timedelta. Timedelta — основанная на типе numpy.timedelta64 более эффективная замена нативного типа данных datetime.timedelta языка Python. Соответствующая индексная конструкция — TimedeltaIndex.

Самые базовые из этих объектов даты/времени — объекты Timestamp и DatetimeIndex. Хотя к ним и можно обращаться непосредственно, чаще используют функцию pd.to_datetime(), умеющую выполнять синтаксический разбор широкого диапазона форматов. При передаче в функцию pd.to_datetime() отдельной даты она возвращает Timestamp, при передаче ряда дат по умолчанию возвращает DatetimeIndex:

In[15]: dates = pd.to_datetime([datetime(2015, 7, 3), '4th of July, 2015', '2015-Jul-6', '07-07-2015', '20150708'])
dates

Out[15]: DatetimeIndex(['2015-07-03', '2015-07-04', '2015-07-06', '2015-07-07', '2015-07-08'],
dtype='datetime64[ns]', freq=None)

Любой объект DatetimeIndex можно с помощью функции to_period() преобразовать в объект PeriodIndex, указав код для периодичности интервала. В данном случае мы использовали код 'D', означающий, что периодичность интервала — один день:

In[16]: dates.to_period('D')

Out[16]: PeriodIndex(['2015-07-03', '2015-07-04', '2015-07-06', '2015-07-07', '2015-07-08'],
dtype='int64', freq='D')

Объект TimedeltaIndex создается, например, при вычитании одной даты из другой:

In[17]: dates - dates[0]

Out[17]:
TimedeltaIndex(['0 days', '1 days', '3 days', '4 days', '5 days'],
dtype='timedelta64[ns]', freq=None)