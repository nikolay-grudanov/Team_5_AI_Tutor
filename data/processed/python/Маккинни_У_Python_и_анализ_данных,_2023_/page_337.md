---
source_image: page_337.png
page_number: 337
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 70.79
tokens: 8965
characters: 3784
timestamp: 2025-12-24T02:49:58.823065
finish_reason: stop
---

In [95]: grouped = frame.groupby(quartiles)

In [96]: grouped.apply(get_stats)
Out[96]:

<table>
  <tr>
    <th></th>
    <th>min</th>
    <th>max</th>
    <th>count</th>
    <th>mean</th>
  </tr>
  <tr>
    <td>data1<br>(-2.956, -1.23]</td>
    <td>data1 -2.949343</td>
    <td>-1.230179</td>
    <td>94</td>
    <td>-1.658818</td>
  </tr>
  <tr>
    <td></td>
    <td>data2 -3.399312</td>
    <td>1.670835</td>
    <td>94</td>
    <td>-0.033333</td>
  </tr>
  <tr>
    <td>(-1.23, 0.489]</td>
    <td>data1 -1.228918</td>
    <td>0.488675</td>
    <td>598</td>
    <td>-0.329524</td>
  </tr>
  <tr>
    <td></td>
    <td>data2 -2.989741</td>
    <td>3.260383</td>
    <td>598</td>
    <td>-0.002622</td>
  </tr>
  <tr>
    <td>(0.489, 2.208]</td>
    <td>data1 0.489965</td>
    <td>2.200997</td>
    <td>298</td>
    <td>1.065727</td>
  </tr>
  <tr>
    <td></td>
    <td>data2 -3.745356</td>
    <td>2.954439</td>
    <td>298</td>
    <td>0.078249</td>
  </tr>
  <tr>
    <td>(2.208, 3.928]</td>
    <td>data1 2.212303</td>
    <td>3.927528</td>
    <td>10</td>
    <td>2.644253</td>
  </tr>
  <tr>
    <td></td>
    <td>data2 -1.929776</td>
    <td>1.765640</td>
    <td>10</td>
    <td>0.024750</td>
  </tr>
</table>

Имейте в виду, что тот же результат можно вычислить проще:
In [97]: grouped.agg(["min", "max", "count", "mean"])
Out[97]:

<table>
  <tr>
    <th></th>
    <th colspan="4">data1</th>
    <th colspan="4">data2</th>
  </tr>
  <tr>
    <th></th>
    <th>min</th>
    <th>max</th>
    <th>count</th>
    <th>mean</th>
    <th>min</th>
    <th>max</th>
    <th>count</th>
    <th>mean</th>
  </tr>
  <tr>
    <td>data1<br>(-2.956, -1.23]</td>
    <td>-2.949343</td>
    <td>-1.230179</td>
    <td>94</td>
    <td>-1.658818</td>
    <td>-3.399312</td>
    <td>1.670835</td>
    <td>94</td>
    <td></td>
  </tr>
  <tr>
    <td>(-1.23, 0.489]</td>
    <td>-1.228918</td>
    <td>0.488675</td>
    <td>598</td>
    <td>-0.329524</td>
    <td>-2.989741</td>
    <td>3.260383</td>
    <td>598</td>
    <td></td>
  </tr>
  <tr>
    <td>(0.489, 2.208]</td>
    <td>0.489965</td>
    <td>2.200997</td>
    <td>298</td>
    <td>1.065727</td>
    <td>-3.745356</td>
    <td>2.954439</td>
    <td>298</td>
    <td></td>
  </tr>
  <tr>
    <td>(2.208, 3.928]</td>
    <td>2.212303</td>
    <td>3.927528</td>
    <td>10</td>
    <td>2.644253</td>
    <td>-1.929776</td>
    <td>1.765640</td>
    <td>10</td>
    <td></td>
  </tr>
</table>

<table>
  <tr>
    <th></th>
    <th colspan="4">mean</th>
  </tr>
  <tr>
    <td>data1<br>(-2.956, -1.23]</td>
    <td>-0.033333</td>
    <td></td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>(-1.23, 0.489]</td>
    <td>-0.002622</td>
    <td></td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>(0.489, 2.208]</td>
    <td>0.078249</td>
    <td></td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>(2.208, 3.928]</td>
    <td>0.024750</td>
    <td></td>
    <td></td>
    <td></td>
  </tr>
</table>

Это были интервалы одинаковой длины, а чтобы вычислить интервалы равного размера на основе выборочных квантилей, нужно использовать функцию pandas.qcut. Мы можем передать количество выборочных квартилей для вычисления интервалов (4) и labels=False, чтобы получать только индексы квартилей, а не интервалы:

In [98]: quartiles_samp = pd.qcut(frame["data1"], 4, labels=False)

In [99]: quartiles_samp.head()
Out[99]:
0    1
1    3
2    2
3    2
4    3
Name: data1, dtype: int64

In [100]: grouped = frame.groupby(quartiles_samp)

In [101]: grouped.apply(get_stats)
Out[101]:

<table>
  <tr>
    <th></th>
    <th>min</th>
    <th>max</th>
    <th>count</th>
    <th>mean</th>
  </tr>
  <tr>
    <td>data1<br>0</td>
    <td>data1 -2.949343</td>
    <td>-0.685484</td>
    <td>250</td>
    <td>-1.212173</td>
  </tr>
</table>