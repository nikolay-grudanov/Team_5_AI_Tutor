---
source_image: page_163.png
page_number: 163
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 29.38
tokens: 7678
characters: 2307
timestamp: 2025-12-24T02:44:21.472399
finish_reason: stop
---

Подвохи целочисленного индексирования

Начинающие часто испытывают затруднения при работе с объектами pandas, индексированными целыми числами, из-за различий с семантикой индексирования встроенных в Python структур данных, таких как списки и кортежи. Например, вряд ли вы ожидаете столкнуться с ошибкой в следующем коде:

In [164]: ser = pd.Series(np.arange(3.))

In [165]: ser
Out[165]:
    0   0.0
    1   1.0
    2   2.0
dtype: float64

In [166]: ser[-1]
---------------------------------------------------------------------------
ValueError                                Traceback (most recent call last)
/miniconda/envs/book-env/lib/python3.10/site-packages/pandas/core/indexes/range.py in get_loc(self, key, method, tolerance)
    384         try:
--> 385             return self._range.index(new_key)
    386         except ValueError as err:
ValueError: -1 is not in range
The above exception was the direct cause of the following exception:
KeyError                                 Traceback (most recent call last)
<ipython-input-166-44969a759c20> in <module>
----> 1 ser[-1]
/miniconda/envs/book-env/lib/python3.10/site-packages/pandas/core/series.py in __getitem__(self, key)
    956     elif key_is_scalar:
--> 958         return self._get_value(key)
    959
    960     if is_hashable(key):
/miniconda/envs/book-env/lib/python3.10/site-packages/pandas/core/series.py in _get_value(self, label, takeable)
   1067         # Similar to Index.get_value, but we do not fall back to positional
--> 1068         loc = self.index.get_loc(label)
   1070         return self.index._get_values_for_loc(self, loc, label)
   1071
/miniconda/envs/book-env/lib/python3.10/site-packages/pandas/core/indexes/range.py in get_loc(self, key, method, tolerance)
    384         try:
--> 385             return self._range.index(new_key)
    386         except ValueError as err:
    387             raise KeyError(key) from err
    388         self._check_indexing_error(key)
    389     raise KeyError(key)

KeyError: -1

В данном примере pandas могла бы «откатиться» к целочисленному индексированию, но в общем случае это трудно сделать, не внеся тонкие ошибки в пользовательский код. Здесь мы имеем индекс, содержащий 0, 1, 2, но понять, чего хочет пользователь (индексировать по метке или по позиции), трудно: