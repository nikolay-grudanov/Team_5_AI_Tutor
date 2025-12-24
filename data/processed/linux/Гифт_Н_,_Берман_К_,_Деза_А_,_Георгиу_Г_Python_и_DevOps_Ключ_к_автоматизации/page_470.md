---
source_image: page_470.png
page_number: 470
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 41.19
tokens: 7692
characters: 1551
timestamp: 2025-12-24T03:13:20.280362
finish_reason: stop
---

adhoc_predict на основе выгрузки

In[0]:

actual_sample2 = df.head(5)
actual_sample2

Out[0]:

<table>
  <tr>
    <th>CHAS</th>
    <th>RM</th>
    <th>TAX</th>
    <th>PTRATIO</th>
    <th>B</th>
    <th>LSTAT</th>
    <th>MEDV</th>
  </tr>
  <tr>
    <td>0</td>
    <td>6.575</td>
    <td>296.0</td>
    <td>15.3</td>
    <td>396.90</td>
    <td>4.98</td>
    <td>24.0</td>
  </tr>
  <tr>
    <td>1</td>
    <td>6.421</td>
    <td>242.0</td>
    <td>17.8</td>
    <td>396.90</td>
    <td>9.14</td>
    <td>21.6</td>
  </tr>
  <tr>
    <td>2</td>
    <td>7.185</td>
    <td>242.0</td>
    <td>17.8</td>
    <td>392.83</td>
    <td>4.03</td>
    <td>34.7</td>
  </tr>
  <tr>
    <td>3</td>
    <td>6.998</td>
    <td>222.0</td>
    <td>18.7</td>
    <td>394.63</td>
    <td>2.94</td>
    <td>33.4</td>
  </tr>
  <tr>
    <td>4</td>
    <td>7.147</td>
    <td>222.0</td>
    <td>18.7</td>
    <td>396.90</td>
    <td>5.33</td>
    <td>36.2</td>
  </tr>
</table>

In[0]:

adhoc_predict2 = actual_sample[["CHAS", "RM", "TAX", "PTRATIO", "B", "LSTAT"]]
adhoc_predict2.head()

Out[0]:

<table>
  <tr>
    <th>CHAS</th>
    <th>RM</th>
    <th>TAX</th>
    <th>PTRATIO</th>
    <th>B</th>
    <th>LSTAT</th>
  </tr>
  <tr>
    <td>0</td>
    <td>6.575</td>
    <td>296.0</td>
    <td>15.3</td>
    <td>396.9</td>
    <td>4.98</td>
  </tr>
</table>

Масштабирование входных данных

In[0]:

scaler = StandardScaler().fit(adhoc_predict2)
scaled_adhoc_predict2 = scaler.transform(adhoc_predict2)
scaled_adhoc_predict2

Out[0]:

array([[0., 0., 0., 0., 0., 0.]])