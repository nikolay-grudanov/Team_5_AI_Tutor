---
source_image: page_342.png
page_number: 342
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 26.83
tokens: 7688
characters: 1833
timestamp: 2025-12-24T02:49:24.243874
finish_reason: stop
---

Пример: групповое взвешенное среднее и корреляция

Принцип разделения–применения–объединения, лежащий в основе groupby, позволяет легко выразить такие операции между столбцами DataFrame или двумя объектами Series, как вычисление группового взвешенного среднего. В качестве примера возьмем следующий набор данных, содержащий групповые ключи, значения и веса:

In [127]: df = pd.DataFrame({"category": ["a", "a", "a", "a",
                                      "b", "b", "b", "b"],
                        "data": np.random.standard_normal(8),
                        "weights": np.random.uniform(size=8)})

In [128]: df
Out[128]:
   category    data   weights
0        a -1.691656  0.955905
1        a  0.511622  0.012745
2        a -0.401675  0.137009
3        a  0.968578  0.763037
4        b -1.818215  0.492472
5        b  0.279963  0.832908
6        b -0.200819  0.658331
7        b -0.217221  0.612009

Групповое взвешенное среднее по столбцу category равно:

In [129]: grouped = df.groupby("category")

In [130]: def get_wavg(group):
      return np.average(group["data"], weights=group["weights"])

In [131]: grouped.apply(get_wavg)
Out[131]:
category
a   -0.495807
b   -0.357273
dtype: float64

В качестве другого примера рассмотрим набор данных с сайта Yahoo! Finance, содержащий цены дня на некоторые акции и индекс S&P 500 (торговый код SPX):

In [132]: close_px = pd.read_csv("examples/stock_px.csv", parse_dates=True,
      index_col=0)

In [133]: close_px.info()
<class 'pandas.core.frame.DataFrame'>
DatetimeIndex: 2214 entries, 2003-01-02 to 2011-10-14
Data columns (total 4 columns):
# Column  Non-Null Count Dtype
--- ------ -------------- ------
0 AAPL    2214 non-null float64
1 MSFT    2214 non-null float64
2 XOM     2214 non-null float64
3 SPX     2214 non-null float64
dtypes: float64(4)
memory usage: 86.5 KB