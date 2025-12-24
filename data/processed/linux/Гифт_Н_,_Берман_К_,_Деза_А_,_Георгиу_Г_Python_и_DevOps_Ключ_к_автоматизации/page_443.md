---
source_image: page_443.png
page_number: 443
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 27.24
tokens: 7332
characters: 1247
timestamp: 2025-12-24T03:12:31.722127
finish_reason: stop
---

контрольный набор данных отделяется для последующей проверки безошибочности обученной модели.

In[0]:

from sklearn.model_selection import train_test_split

Выделение и изучение признаков и целевой переменной. Полезно явно извлечь целевую переменную и переменные признаков и привести их к единой форме. После этого желательно проверить форму и убедиться, что она подходит для машинного обучения с помощью sklearn.

In[0]:

y = df['Weight-Pounds'].values #Цель
y = y.reshape(-1, 1)
X = df['Height-Inches'].values #Признак(и)
X = X.reshape(-1, 1)

In[14]:

y.shape

Out[14]:
(25000, 1)

Разбиение данных. Данные разбиваются в соотношении 80/20 %.

In[15]:

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
print(X_train.shape, y_train.shape)
print(X_test.shape, y_test.shape)

Out[15]:

(20000, 1) (20000, 1)
(5000, 1) (5000, 1)

Подгонка модели. Производим подгонку модели с помощью алгоритма линейной регрессии, импортируемого из sklearn.

In[0]:

from sklearn.linear_model import LinearRegression
lm = LinearRegression()
model = lm.fit(X_train, y_train)
y_predicted = lm.predict(X_test)

Выводим показатель безошибочности модели линейной регрессии. Посмотрим теперь, какую безошибочность демонстрирует обученная модель при