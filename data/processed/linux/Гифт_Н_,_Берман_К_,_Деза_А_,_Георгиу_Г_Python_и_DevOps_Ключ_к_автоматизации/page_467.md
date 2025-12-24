---
source_image: page_467.png
page_number: 467
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 56.05
tokens: 7945
characters: 2192
timestamp: 2025-12-24T03:13:34.826544
finish_reason: stop
---

"Org House Price": Y_validation,
    "Pred House Price": predictions
})
evaluate["difference"] = evaluate["Org House Price"]-evaluate["Pred House Price"]
evaluate.head()

Разности приведены далее.

Out[0]:

<table>
  <tr>
    <th></th>
    <th>Org house price</th>
    <th>Pred house price</th>
    <th>Difference</th>
  </tr>
  <tr>
    <td>0</td>
    <td>21.7</td>
    <td>21</td>
    <td>0.7</td>
  </tr>
  <tr>
    <td>1</td>
    <td>18.5</td>
    <td>19</td>
    <td>-0.5</td>
  </tr>
  <tr>
    <td>2</td>
    <td>22.2</td>
    <td>20</td>
    <td>2.2</td>
  </tr>
  <tr>
    <td>3</td>
    <td>20.4</td>
    <td>19</td>
    <td>1.4</td>
  </tr>
  <tr>
    <td>4</td>
    <td>8.8</td>
    <td>9</td>
    <td>-0.2</td>
  </tr>
</table>

Для просмотра распределения данных в Pandas очень удобен метод describe:

In[0]:
evaluate.describe()

Out[0]:

<table>
  <tr>
    <th></th>
    <th>Org house price</th>
    <th>Pred house price</th>
    <th>Difference</th>
  </tr>
  <tr>
    <td>count</td>
    <td>102.000000</td>
    <td>102.000000</td>
    <td>102.000000</td>
  </tr>
  <tr>
    <td>mean</td>
    <td>22.573529</td>
    <td>22.117647</td>
    <td>0.455882</td>
  </tr>
  <tr>
    <td>std</td>
    <td>9.033622</td>
    <td>8.758921</td>
    <td>5.154438</td>
  </tr>
  <tr>
    <td>min</td>
    <td>6.300000</td>
    <td>8.000000</td>
    <td>-34.100000</td>
  </tr>
  <tr>
    <td>25%</td>
    <td>17.350000</td>
    <td>17.000000</td>
    <td>-0.800000</td>
  </tr>
  <tr>
    <td>50%</td>
    <td>21.800000</td>
    <td>20.500000</td>
    <td>0.600000</td>
  </tr>
  <tr>
    <td>75%</td>
    <td>24.800000</td>
    <td>25.000000</td>
    <td>2.200000</td>
  </tr>
  <tr>
    <td>max</td>
    <td>50.000000</td>
    <td>56.000000</td>
    <td>22.000000</td>
  </tr>
</table>

adhoc_predict

Проверим эту модель для предсказания и посмотрим на ее работу после загрузки. При разработке веб-API для модели машинного обучения желательно протестировать части кода, которые API будет выполнять в самом блокноте. Отлаживать и создавать функции в блокноте намного проще, чем мучиться с созданием нужных функций в веб-приложении.

In[0]:
actual_sample = df.head(1)
actual_sample

Out[0]: