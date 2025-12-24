---
source_image: page_413.png
page_number: 413
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 27.20
tokens: 7582
characters: 1758
timestamp: 2025-12-24T02:51:40.706686
finish_reason: stop
---

Parch    0
Ticket   0
Fare     1
Cabin    327
Embarked 0
dtype: int64

В статистике и машинном обучении типичная задача заключается в том, чтобы предсказать, выживет ли пассажир, на основе признаков, содержащихся в данных. Модель обучается на обучающем наборе данных, а затем оценивается на не пересекающемся с ним тестовом наборе данных.

Я хотел бы использовать в качестве предсказательного признака возраст Age, но в этом столбце есть отсутствующие данные. Существует несколько способов восполнить отсутствующие данные, я выберу самый простой и заменю значения null в обеих таблицах медианными значениями для обучающего набора:

In [92]: impute_value = train['Age'].median()

In [93]: train['Age'] = train['Age'].fillna(impute_value)

In [94]: test['Age'] = test['Age'].fillna(impute_value)

Теперь мы должны описать модель. Я добавлю столбец IsFemale, вычисляемый на основе столбца 'Sex':

In [95]: train['IsFemale'] = (train['Sex'] == 'female').astype(int)

In [96]: test['IsFemale'] = (test['Sex'] == 'female').astype(int)

Выберем переменные модели и создадим массивы NumPy:

In [97]: predictors = ['Pclass', 'IsFemale', 'Age']

In [98]: X_train = train[predictors].to_numpy()

In [99]: X_test = test[predictors].to_numpy()

In [100]: y_train = train['Survived'].to_numpy()

In [101]: X_train[:5]
Out[101]:
array([[3., 0., 22.],
       [1., 1., 38.],
       [3., 1., 26.],
       [1., 1., 35.],
       [3., 0., 35.]])

In [102]: y_train[:5]
Out[102]: array([0, 1, 1, 1, 0])

Я вовсе не утверждаю, что это хорошая модель или что признаки сконструированы правильно. Мы воспользуемся моделью LogisticRegression из scikit-learn и создадим ее экземпляр:

In [103]: from sklearn.linear_model import LogisticRegression

In [104]: model = LogisticRegression()