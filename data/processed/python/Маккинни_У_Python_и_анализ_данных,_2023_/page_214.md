---
source_image: page_214.png
page_number: 214
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 24.11
tokens: 7399
characters: 1234
timestamp: 2025-12-24T02:45:46.673788
finish_reason: stop
---

2    NaN
3    0.0
dtype: float64

Метод isna дает булев объект Series, в котором элементы True соответствуют отсутствующим значениям:

In [16]: float_data.isna()
Out[16]:
0   False
1   False
2   True
3   False
dtype: bool

В pandas мы приняли соглашение, заимствованное из языка программирования R, — обозначать отсутствующие данные NA — not available (недоступны). В статистических приложениях NA может означать, что данные не существуют или существуют, но не наблюдаемы (например, из-за сложностей сбора данных). В процессе очистки данных зачастую важно анализировать сами отсутствующие данные, чтобы выявить проблемы, относящиеся к их сбору, или потенциальное смещение, вызванное отсутствием данных.

Встроенное в Python значение None также рассматривается как NA в массивах объектов:

In [17]: string_data = pd.Series(["aardvark", np.nan, None, "avocado"])

In [18]: string_data
Out[18]:
0    aardvark
1     NaN
2     None
3    avocado
dtype: object

In [19]: string_data.isna()
Out[19]:
0   False
1   True
2   True
3   False
dtype: bool

In [20]: float_data = pd.Series([1, 2, None], dtype='float64')

In [21]: float_data
Out[21]:
0    1.0
1    2.0
2    NaN
dtype: float64

In [22]: float_data.isna()
Out[22]:
0   False
1   False