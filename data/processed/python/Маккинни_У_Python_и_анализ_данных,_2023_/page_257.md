---
source_image: page_257.png
page_number: 257
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 31.41
tokens: 7639
characters: 1472
timestamp: 2025-12-24T02:47:06.889726
finish_reason: stop
---

a    0.929616   0.316376   0.183919
b    0.204560      NaN     0.567725
c    0.595545   0.964515      NaN
d      NaN     0.653177   0.748907

Обратной к unstack операцией является stack:

In [19]: data.unstack().stack()
Out[19]:
    a    1    0.929616
         2    0.316376
         3    0.183919
    b    1    0.204560
         3    0.567725
    c    1    0.595545
         2    0.964515
    d    2    0.653177
         3    0.748907
dtype: float64

Методы stack и unstack будут подробно рассмотрены в разделе 8.3.
В случае DataFrame иерархический индекс может существовать для любой оси:

In [20]: frame = pd.DataFrame(np.arange(12).reshape((4, 3)),
    ....:                 index=[["a", "a", "b", "b"], [1, 2, 1, 2]],
    ....:                 columns=[["Ohio", "Ohio", "Colorado"],
    ....:                              ["Green", "Red", "Green"]])
In [21]: frame
Out[21]:
      Ohio Colorado
      Green Red Green
a  1   0   1   2
   2   3   4   5
b  1   6   7   8
   2   9  10  11

Уровни иерархии могут иметь имена (как строки или любые объекты Python). В таком случае они будут показаны при выводе на консоль:

In [22]: frame.index.names = ["key1", "key2"]
In [23]: frame.columns.names = ["state", "color"]
In [24]: frame
Out[24]:
state    Ohio Colorado
color    Green Red Green
key1 key2
a        1   0   1   2
         2   3   4   5
b        1   6   7   8
         2   9  10  11

Эти имена замещают атрибут name, используемый только для одноуровневых индексов.