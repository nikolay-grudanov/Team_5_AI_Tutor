---
source_image: page_465.png
page_number: 465
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 30.54
tokens: 7551
characters: 1757
timestamp: 2025-12-24T03:13:07.636130
finish_reason: stop
---

In[0]:

for sample in list(X_validation)[0:2]:
    print(f"X_validation {sample}")

Out[0]:

X_validation [   1.      6.395  666.     20.2    391.34   13.27  ]
X_validation [   0.      5.895  224.     20.2    394.81   10.56  ]

Тонкая настройка масштабированного GBM¹

В этой модели используется несколько продвинутых методик, которые можно встретить во многих успешных проектах Kaggle. В их числе решетчатый поиск (grid search) оптимальных гиперпараметров. Обратите внимание также на масштабирование данных. Для безошибочных предсказаний большинству алгоритмов машинного обучения требуется какое-либо масштабирование.

In[0]:
# Опции проверки и метрика оценки на основе метода
# среднеквадратичной ошибки
num_folds = 10
seed = 7
RMS = 'neg_mean_squared_error'
scaler = StandardScaler().fit(X_train)
rescaledX = scaler.transform(X_train)
param_grid = dict(n_estimators=numpy.array([50,100,150,200,250,300,350,400]))
model = GradientBoostingRegressor(random_state=seed)
kfold = KFold(n_splits=num_folds, random_state=seed)
grid = GridSearchCV(estimator=model, param_grid=param_grid, scoring=RMS, cv=kfold)
grid_result = grid.fit(rescaledX, Y_train)

print("Best: %f using %s" % (grid_result.best_score_, grid_result.best_params_))
means = grid_result.cv_results_['mean_test_score']
stds = grid_result.cv_results_['std_test_score']
params = grid_result.cv_results_['params']
for mean, stdev, param in zip(means, stds, params):
    print("%f (%f) with: %r" % (mean, stdev, param))

Out[0]:

Best: -11.830068 using {'n_estimators': 200}
-12.479635 (6.348297) with: {'n_estimators': 50}
-12.102737 (6.441597) with: {'n_estimators': 100}
-11.843649 (6.631569) with: {'n_estimators': 150}

¹ Gradient boosting machines — метод градиентного бустинга. — Примеч. пер.