---
source_image: page_385.png
page_number: 385
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 34.97
tokens: 7775
characters: 1933
timestamp: 2025-12-24T02:50:57.002050
finish_reason: stop
---

Наконец, иногда желательно сдвинуть индекс результата на какую-то величину, скажем вычесть одну секунду из правого конца, чтобы было понятнее, к какому интервалу относится временная метка. Для этого следует прибавить смещение к результирующему индексу:

In [219]: from pandas.tseries.frequencies import to_offset

In [220]: result = ts.resample("5min", closed="right", label="right").sum()

In [221]: result.index = result.index + to_offset("-1s")

In [222]: result
Out[222]:
1999-12-31 23:59:59    0
2000-01-01 00:04:59    15
2000-01-01 00:09:59    40
2000-01-01 00:14:59    11
Freq: 5T, dtype: int64

Передискретизация OHLC
В финансовых приложениях очень часто временной ряд агрегируют, вычисляя четыре значения для каждого интервала: первое (открытие — open), последнее (закрытие — close), максимальное (high) и минимальное (low). Задав параметр how='ohlc', мы получим объект DataFrame, в столбцах которого находятся эти четыре агрегата, которые эффективно вычисляются одним вызовом функции:

In [223]: ts = pd.Series(np.random.permutation(np.arange(len(dates))), index=dates)

In [224]: ts.resample("5min").ohlc()
Out[224]:
          open  high  low  close
2000-01-01 00:00:00   8    8   1    5
2000-01-01 00:05:00   6   11   2    2
2000-01-01 00:10:00   0    7   0    7

Повышающая передискретизация и интерполяция
Повышающая передискретизация — это преобразование от низкой частоты к более высокой, агрегирование при этом не требуется. Рассмотрим объект DataFrame, содержащий недельные данные:

In [225]: frame = pd.DataFrame(np.random.standard_normal((2, 4)),
      ....:                 index=pd.date_range("2000-01-01", periods=2,
      ....:                 freq="W-WED"),
      ....:                 columns=["Colorado", "Texas", "New York", "Ohio"])

In [226]: frame
Out[226]:
         Colorado   Texas  New York   Ohio
2000-01-05 -0.896431  0.927238  0.482284 -0.867130
2000-01-12  0.493841 -0.155434  1.397286  1.507055