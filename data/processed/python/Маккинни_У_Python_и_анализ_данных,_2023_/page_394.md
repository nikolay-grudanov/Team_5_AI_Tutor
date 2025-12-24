---
source_image: page_394.png
page_number: 394
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 16.43
tokens: 7403
characters: 1142
timestamp: 2025-12-24T02:50:54.463143
finish_reason: stop
---

простой скользящей оконной функции, для которой размер окна равен промежутку.

Поскольку экспоненциально взвешенная статистика придает больший вес недавним наблюдениям, она быстрее «адаптируется» к изменениям по сравнению с вариантом с равными весами.

В pandas имеется оператор ewm (exponentially weighted moving — экспоненциально взвешенный сдвиг), который работает совместно с rolling и expanding. В примере ниже скользящее среднее котировок акций Apple за 60 дней сравнивается с экспоненциально взвешенным (EW) скользящим средним для span=60 (рис. 11.7):

In [265]: aapl_px = close_px["AAPL"]["2006":"2007"]

In [266]: ma30 = aapl_px.rolling(30, min_periods=20).mean()

In [267]: ewma30 = aapl_px.ewm(span=30).mean()

In [268]: aapl_px.plot(style="k-", label="Price")
Out[268]: <AxesSubplot:>

In [269]: ma30.plot(style="k--", label="Simple Moving Avg")
Out[269]: <AxesSubplot:>

In [270]: ewma30.plot(style="k-", label="EW MA")
Out[270]: <AxesSubplot:>

In [271]: plt.legend()

![Простое и экспоненциально взвешенное скользящее среднее](https://i.imgur.com/3Q5z5QG.png)

Рис. 11.7. Простое и экспоненциально взвешенное скользящее среднее