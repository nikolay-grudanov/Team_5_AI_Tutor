---
source_image: page_358.png
page_number: 358
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 25.98
tokens: 7763
characters: 1745
timestamp: 2025-12-24T02:49:53.427859
finish_reason: stop
---

11.2. Основы работы с временными рядами

In [39]: dates = [datetime(2011, 1, 2), datetime(2011, 1, 5),
    ....:         datetime(2011, 1, 7), datetime(2011, 1, 8),
    ....:         datetime(2011, 1, 10), datetime(2011, 1, 12)]

In [40]: ts = pd.Series(np.random.standard_normal(6), index=dates)

In [41]: ts
Out[41]:
2011-01-02   -0.204708
2011-01-05    0.478943
2011-01-07   -0.519439
2011-01-08   -0.555730
2011-01-10    1.965781
2011-01-12    1.393406
dtype: float64

Под капотом объекты datetime помещаются в объект типа DatetimeIndex:

In [42]: ts.index
Out[42]:
DatetimeIndex(['2011-01-02', '2011-01-05', '2011-01-07', '2011-01-08',
               '2011-01-10', '2011-01-12'],
              dtype='datetime64[ns]', freq=None)

Как и для других объектов Series, арифметические операции над временными рядами с различными индексами автоматически приводят к выравниванию дат:

In [43]: ts + ts[::2]
Out[43]:
2011-01-02   -0.409415
2011-01-05     NaN
2011-01-07   -1.038877
2011-01-08     NaN
2011-01-10    3.931561
2011-01-12     NaN
dtype: float64

Напомним, что конструкция ts[::2] выбирает каждый второй элемент ts.
В pandas временные метки хранятся в типе данных NumPy datetime64 с наносекундным разрешением:

In [44]: ts.index.dtype
Out[44]: dtype('<M8[ns]')

Скалярные значения в индексе DatetimeIndex — это объекты pandas типа Timestamp:

In [45]: stamp = ts.index[0]

In [46]: stamp
Out[46]: Timestamp('2011-01-02 00:00:00')

Объект типа pandas.Timestamp можно использовать всюду, где допустим объект datetime. Обратное, однако, неверно, потому что в pandas.Timestamp можно хранить данные с наносекундной точностью, а в datetime — только с микросекундной. Кроме того, в pandas.Timestamp можно хранить информацию о частоте (если име-