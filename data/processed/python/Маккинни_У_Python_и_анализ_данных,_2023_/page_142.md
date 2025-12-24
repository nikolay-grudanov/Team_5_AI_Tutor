---
source_image: page_142.png
page_number: 142
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 20.05
tokens: 7399
characters: 1202
timestamp: 2025-12-24T02:43:40.882682
finish_reason: stop
---

California    False
Ohio          True
Oregon        True
Texas         True
dtype: bool

У объекта Series есть также методы экземпляра:

In [39]: obj4.isna()
Out[39]:
California    True
Ohio          False
Oregon        False
Texas         False
dtype: bool

Более подробно работа с отсутствующими данными будет обсуждаться в главе 7.

Во многих приложениях полезно, что при выполнении арифметических операций объект Series автоматически выравнивает данные по индексной метке:

In [40]: obj3
Out[40]:
Ohio      35000
Texas     71000
Oregon    16000
Utah      5000
dtype: int64

In [41]: obj4
Out[41]:
California   NaN
Ohio         35000.0
Oregon       16000.0
Texas        71000.0
dtype: float64

In [42]: obj3 + obj4
Out[42]:
California   NaN
Ohio         70000.0
Oregon       32000.0
Texas        142000.0
Utah         NaN
dtype: float64

Вопрос о выравнивании данных будет подробнее рассмотрен ниже. Если у вас имеется опыт работы с базами данных, то можете считать, что это аналог операции соединения.

И у самого объекта Series, и у его индекса имеется атрибут name, тесно связанный с другими частями функциональности pandas:

In [43]: obj4.name = "population"

In [44]: obj4.index.name = "state"