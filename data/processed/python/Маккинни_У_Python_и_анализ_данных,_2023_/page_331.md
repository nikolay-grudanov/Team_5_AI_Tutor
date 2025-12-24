---
source_image: page_331.png
page_number: 331
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 73.19
tokens: 9026
characters: 4203
timestamp: 2025-12-24T02:49:50.469156
finish_reason: stop
---

<table>
  <tr>
    <th>day</th>
    <th>smoker</th>
    <th>0.160113</th>
    <th>0.042347</th>
    <th>0.193226</th>
  </tr>
  <tr>
    <td></td>
    <td>Yes</td>
    <td>0.187250</td>
    <td>0.154134</td>
    <td>0.644685</td>
  </tr>
  <tr>
    <td>Thur</td>
    <td>No</td>
    <td>0.160298</td>
    <td>0.038774</td>
    <td>0.193350</td>
  </tr>
  <tr>
    <td></td>
    <td>Yes</td>
    <td>0.163863</td>
    <td>0.039389</td>
    <td>0.151240</td>
  </tr>
</table>

Здесь мы передали список функций агрегирования методу agg, который независимо вычисляет агрегаты для групп данных.

Совершенно необязательно соглашаться с именами столбцов, предложенными объектом GroupBy; в частности все лямбда-функции называются '<lambda>', поэтому различить их затруднительно (можете убедиться сами, распечатав атрибут функции __name__). Поэтому если передать список кортежей вида (name, function), то в качестве имени столбца DataFrame будет взят первый элемент кортежа (можно считать, что список 2-кортежей — упорядоченное отображение):

In [72]: grouped_pct.agg([("average", "mean"), ("stdev", np.std)])
Out[72]:
<table>
  <tr>
    <th>day</th>
    <th>smoker</th>
    <th>average</th>
    <th>stdev</th>
  </tr>
  <tr>
    <td>Fri</td>
    <td>No</td>
    <td>0.151650</td>
    <td>0.028123</td>
  </tr>
  <tr>
    <td></td>
    <td>Yes</td>
    <td>0.174783</td>
    <td>0.051293</td>
  </tr>
  <tr>
    <td>Sat</td>
    <td>No</td>
    <td>0.158048</td>
    <td>0.039767</td>
  </tr>
  <tr>
    <td></td>
    <td>Yes</td>
    <td>0.147906</td>
    <td>0.061375</td>
  </tr>
  <tr>
    <td>Sun</td>
    <td>No</td>
    <td>0.160113</td>
    <td>0.042347</td>
  </tr>
  <tr>
    <td></td>
    <td>Yes</td>
    <td>0.187250</td>
    <td>0.154134</td>
  </tr>
  <tr>
    <td>Thur</td>
    <td>No</td>
    <td>0.160298</td>
    <td>0.038774</td>
  </tr>
  <tr>
    <td></td>
    <td>Yes</td>
    <td>0.163863</td>
    <td>0.039389</td>
  </tr>
</table>

В случае DataFrame диапазон возможностей шире, поскольку можно задавать список функций, применяемых ко всем столбцам, или разные функции для разных столбцов. Допустим, нам нужно вычислить три одинаковые статистики для столбцов tip_pct и total_bill:

In [73]: functions = ["count", "mean", "max"]

In [74]: result = grouped[["tip_pct", "total_bill"]].agg(functions)

In [75]: result
Out[75]:
<table>
  <tr>
    <th rowspan="2">day</th>
    <th rowspan="2">smoker</th>
    <th colspan="3">tip_pct</th>
    <th colspan="3">total_bill</th>
  </tr>
  <tr>
    <th>count</th>
    <th>mean</th>
    <th>max</th>
    <th>count</th>
    <th>mean</th>
    <th>max</th>
  </tr>
  <tr>
    <td>Fri</td>
    <td>No</td>
    <td>4</td>
    <td>0.151650</td>
    <td>0.187735</td>
    <td>4</td>
    <td>18.420000</td>
    <td>22.75</td>
  </tr>
  <tr>
    <td></td>
    <td>Yes</td>
    <td>15</td>
    <td>0.174783</td>
    <td>0.263480</td>
    <td>15</td>
    <td>16.813333</td>
    <td>40.17</td>
  </tr>
  <tr>
    <td>Sat</td>
    <td>No</td>
    <td>45</td>
    <td>0.158048</td>
    <td>0.291990</td>
    <td>45</td>
    <td>19.661778</td>
    <td>48.33</td>
  </tr>
  <tr>
    <td></td>
    <td>Yes</td>
    <td>42</td>
    <td>0.147906</td>
    <td>0.325733</td>
    <td>42</td>
    <td>21.276667</td>
    <td>50.81</td>
  </tr>
  <tr>
    <td>Sun</td>
    <td>No</td>
    <td>57</td>
    <td>0.160113</td>
    <td>0.252672</td>
    <td>57</td>
    <td>20.506667</td>
    <td>48.17</td>
  </tr>
  <tr>
    <td></td>
    <td>Yes</td>
    <td>19</td>
    <td>0.187250</td>
    <td>0.710345</td>
    <td>19</td>
    <td>24.120000</td>
    <td>45.35</td>
  </tr>
  <tr>
    <td>Thur</td>
    <td>No</td>
    <td>45</td>
    <td>0.160298</td>
    <td>0.266312</td>
    <td>45</td>
    <td>17.113111</td>
    <td>41.19</td>
  </tr>
  <tr>
    <td></td>
    <td>Yes</td>
    <td>17</td>
    <td>0.163863</td>
    <td>0.241255</td>
    <td>17</td>
    <td>19.190588</td>
    <td>43.11</td>
  </tr>
</table>

Как видите, в результирующем DataFrame имеются иерархические столбцы — точно так же, как было бы, если бы мы агрегировали каждый столбец по отдельности, а потом склеили результаты с помощью метода concat, передав ему имена столбцов в качестве аргумента keys: