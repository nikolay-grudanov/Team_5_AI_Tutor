---
source_image: page_153.png
page_number: 153
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 23.68
tokens: 7500
characters: 1466
timestamp: 2025-12-24T02:44:02.318794
finish_reason: stop
---

c    3.6
d    4.5
e    NaN
dtype: float64

Для упорядоченных данных, например временных рядов, иногда желательно произвести интерполяцию, или восполнение отсутствующих значений в процессе переиндексации. Это позволяет сделать параметр method; так, если задать для него значение ffill, то вместо отсутствующих значений будут подставлены значения из ближайшей предшествующей строки, имеющейся в индексе:

In [102]: obj3 = pd.Series(["blue", "purple", "yellow"], index=[0, 2, 4])

In [103]: obj3
Out[103]:
0    blue
2    purple
4    yellow
dtype: object

In [104]: obj3.reindex(np.arange(6), method="ffill")
Out[104]:
0    blue
1    blue
2    purple
3    purple
4    yellow
5    yellow
dtype: object

В случае объекта DataFrame метод reindex может изменять строки, столбцы или то и другое. Если передать ему просто последовательность, то в результирующем объекте переиндексируются строки:

In [105]: frame = pd.DataFrame(np.arange(9).reshape((3, 3)),
      ....:                 index=["a", "c", "d"],
      ....:                 columns=["Ohio", "Texas", "California"])

In [106]: frame
Out[106]:
   Ohio  Texas  California
a     0      1            2
c     3      4            5
d     6      7            8

In [107]: frame2 = frame.reindex(index=["a", "b", "c", "d"])

In [108]: frame2
Out[108]:
   Ohio  Texas  California
a   0.0   1.0   2.0
b   NaN   NaN   NaN
c   3.0   4.0   5.0
d   6.0   7.0   8.0

Столбцы можно переиндексировать, задав ключевое слово columns: