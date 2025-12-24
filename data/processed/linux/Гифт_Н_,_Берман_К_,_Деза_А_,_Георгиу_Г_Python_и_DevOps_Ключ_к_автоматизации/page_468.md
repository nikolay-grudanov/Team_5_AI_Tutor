---
source_image: page_468.png
page_number: 468
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 35.81
tokens: 7613
characters: 1784
timestamp: 2025-12-24T03:13:14.679096
finish_reason: stop
---

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
    <td>396.9</td>
    <td>4.98</td>
    <td>24.0</td>
  </tr>
</table>

In[0]:

adhoc_predict = actual_sample[["CHAS", "RM", "TAX", "PTRATIO", "B", "LSTAT"]]
adhoc_predict.head()

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

Технологический процесс JSON

Этот раздел блокнота удобен для отладки приложений Flask. Как упоминалось ранее, намного проще разработать код API в проекте машинного обучения, убедиться в его правильной работе, а затем перенести в сценарий. Альтернатива не так привлекательна: пытаться достичь нужного синтаксиса кода в программном проекте, где нет таких интерактивных инструментов, как в Jupyter.

In[0]:

json_payload = adhoc_predict.to_json()
json_payload

Out[0]:

{
  "CHAS": {"0": 0},
  "RM": {"0": 6.575},
  "TAX": {"0": 296.0},
  "PTRATIO": {"0": 15.3},
  "B": {"0": 396.9},
  "LSTAT": {"0": 4.98}
}

Масштабирование входных данных

Для предсказания необходимо обратное масштабирование данных. Следует произвести эту операцию в блокноте, а не пытаться заставить ее работать в веб-приложении, отладка которого — намного более трудная задача. Ниже приведен код для реализации этой части конвейера машинного обучения. В дальнейшем его можно использовать для создания функции в приложении Flask.

In[0]:

scaler = StandardScaler().fit(adhoc_predict)
scaled_adhoc_predict = scaler.transform(adhoc_predict)