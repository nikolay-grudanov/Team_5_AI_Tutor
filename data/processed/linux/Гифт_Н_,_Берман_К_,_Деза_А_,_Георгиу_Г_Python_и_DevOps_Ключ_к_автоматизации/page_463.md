---
source_image: page_463.png
page_number: 463
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 67.81
tokens: 8169
characters: 2594
timestamp: 2025-12-24T03:13:39.997959
finish_reason: stop
---

from sklearn.ensemble import RandomForestRegressor
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.ensemble import ExtraTreesRegressor
from sklearn.ensemble import AdaBoostRegressor
from sklearn.metrics import mean_squared_error

In[0]:

boston_housing = "https://raw.githubusercontent.com/noahgift/boston_housing_pickle/master/housing.csv"
names = ['CRIM', 'ZN', 'INDUS', 'CHAS',
    'NOX', 'RM', 'AGE', 'DIS', 'RAD', 'TAX',
    'PTRATIO', 'B', 'LSTAT', 'MEDV']
df = read_csv(boston_housing, delim_whitespace=True, names=names)

In[0]:

df.head()

Out[0]:

<table>
  <tr>
    <th>CRIM</th>
    <th>ZN</th>
    <th>INDUS</th>
    <th>CHAS</th>
    <th>NOX</th>
    <th>RM</th>
    <th>AGE</th>
    <th>DIS</th>
    <th>RAD</th>
    <th>TAX</th>
    <th>PTRATIO</th>
    <th>B</th>
    <th>LSTAT</th>
    <th>MEDV</th>
  </tr>
  <tr>
    <td>0 0.00632</td>
    <td>18.0</td>
    <td>2.31</td>
    <td>0</td>
    <td>0.538</td>
    <td>6.575</td>
    <td>65.2</td>
    <td>4.0900</td>
    <td>1</td>
    <td>296.0</td>
    <td>15.3</td>
    <td>396.90</td>
    <td>4.98</td>
    <td>24.0</td>
  </tr>
  <tr>
    <td>1 0.02731</td>
    <td>0.0</td>
    <td>7.07</td>
    <td>0</td>
    <td>0.469</td>
    <td>6.421</td>
    <td>78.9</td>
    <td>4.9671</td>
    <td>2</td>
    <td>242.0</td>
    <td>17.8</td>
    <td>396.90</td>
    <td>9.14</td>
    <td>21.6</td>
  </tr>
  <tr>
    <td>2 0.02729</td>
    <td>0.0</td>
    <td>7.07</td>
    <td>0</td>
    <td>0.469</td>
    <td>7.185</td>
    <td>61.1</td>
    <td>4.9671</td>
    <td>2</td>
    <td>242.0</td>
    <td>17.8</td>
    <td>392.83</td>
    <td>4.03</td>
    <td>34.7</td>
  </tr>
  <tr>
    <td>3 0.03237</td>
    <td>0.0</td>
    <td>2.18</td>
    <td>0</td>
    <td>0.458</td>
    <td>6.998</td>
    <td>45.8</td>
    <td>6.0622</td>
    <td>3</td>
    <td>222.0</td>
    <td>18.7</td>
    <td>394.63</td>
    <td>2.94</td>
    <td>33.4</td>
  </tr>
  <tr>
    <td>4 0.06905</td>
    <td>0.0</td>
    <td>2.18</td>
    <td>0</td>
    <td>0.458</td>
    <td>7.147</td>
    <td>54.2</td>
    <td>6.0622</td>
    <td>3</td>
    <td>222.0</td>
    <td>18.7</td>
    <td>396.90</td>
    <td>5.33</td>
    <td>36.2</td>
  </tr>
</table>

Разведочный анализ данных

Признаки модели:

• \( CHAS \) — фиктивное значение для реки Чарльз (1, если участок граничит с рекой, 0 в противном случае);
• \( RM \) — среднее количество комнат в доме;
• \( TAX \) — полный налог на недвижимость из расчета на 10 000 долларов;
• \( PTRATIO \) — число учащихся на одного преподавателя;
• \( Bk \) — доля афроамериканцев по городам;