---
source_image: page_464.png
page_number: 464
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 36.40
tokens: 7710
characters: 1854
timestamp: 2025-12-24T03:13:08.605383
finish_reason: stop
---

• \( LSTAT \) — процент работающих мужчин без среднего образования;
• \( MEDV \) — медианная стоимость не арендуемых домов в тысячах долларов.

In[0]:

prices = df['MEDV']
df = df.drop(['CRIM','ZN','INDUS','NOX','AGE','DIS','RAD'], axis = 1)
features = df.drop('MEDV', axis = 1)
df.head()

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

Моделирование

В этой части блокнота производится собственно моделирование. Для удобства мы всегда делим блокнот на четыре основных раздела:

• ввод данных;
• разведочный анализ данных;
• моделирование;
• заключение.

В посвященном моделированию разделе данные извлекаются из объекта DataFrame и передаются в модуль train_test_split sklearn, который и берет на себя весь труд по разбиению данных на обучающие и проверочные.

Разбиение данных

In[0]:

# Отделяем проверочный набор данных
array = df.values
X = array[:,0:6]
Y = array[:,6]
validation_size = 0.20
seed = 7
X_train, X_validation, Y_train, Y_validation = train_test_split(X, Y,
    test_size=validation_size, random_state=seed)