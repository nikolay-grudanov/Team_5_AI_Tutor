---
source_image: page_441.png
page_number: 441
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 44.46
tokens: 7622
characters: 1290
timestamp: 2025-12-24T03:12:44.955012
finish_reason: stop
---

In[0]:

import seaborn as sns
import numpy as np

In[9]:

sns.lmplot("Height-Inches", "Weight-Pounds", data=df)

![График lmplot роста/веса](../images/ch14_01.png)

Рис. 14.1. График lmplot роста/веса

Общие статистические показатели

Далее можно сгенерировать некоторые статистические показатели.

In[10]:

df.describe()

Out[10]:

<table>
  <tr>
    <th></th>
    <th>Index</th>
    <th>Height-Inches</th>
    <th>Weight-Pounds</th>
  </tr>
  <tr>
    <td>count</td>
    <td>25000.000000</td>
    <td>25000.000000</td>
    <td>25000.000000</td>
  </tr>
  <tr>
    <td>mean</td>
    <td>12500.500000</td>
    <td>67.993114</td>
    <td>127.079421</td>
  </tr>
  <tr>
    <td>std</td>
    <td>7217.022701</td>
    <td>1.901679</td>
    <td>11.660898</td>
  </tr>
  <tr>
    <td>min</td>
    <td>1.000000</td>
    <td>60.278360</td>
    <td>78.014760</td>
  </tr>
  <tr>
    <td>25%</td>
    <td>6250.750000</td>
    <td>66.704397</td>
    <td>119.308675</td>
  </tr>
  <tr>
    <td>50%</td>
    <td>12500.500000</td>
    <td>67.995700</td>
    <td>127.157750</td>
  </tr>
  <tr>
    <td>75%</td>
    <td>18750.250000</td>
    <td>69.272958</td>
    <td>134.892850</td>
  </tr>
  <tr>
    <td>max</td>
    <td>25000.000000</td>
    <td>75.152800</td>
    <td>170.924000</td>
  </tr>
</table>