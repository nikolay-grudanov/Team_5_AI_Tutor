---
source_image: page_472.png
page_number: 472
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 22.02
tokens: 7303
characters: 1058
timestamp: 2025-12-24T01:03:20.560609
finish_reason: stop
---

472 Глава 5 • Машинное обучение

In[22]: from sklearn.grid_search import GridSearchCV
    param_grid = {'svc__C': [1, 5, 10, 50],
                  'svc__gamma': [0.0001, 0.0005, 0.001, 0.005]}
    grid = GridSearchCV(model, param_grid)
    %time grid.fit(Xtrain, ytrain)
    print(grid.best_params_)

CPU times: user 47.8 s, sys: 4.08 s, total: 51.8 s
Wall time: 26 s
{'svc__gamma': 0.001, 'svc__C': 10}

Оптимальные значения приходятся на середину нашей сетки. Если бы они приходились на края сетки, то желательно было бы расширить сетку, чтобы убедиться в нахождении истинного оптимума.

Теперь с помощью этой, подвергнутой перекрестной проверке модели можно предсказать метки для контрольных данных, которые модель еще не видела:

In[23]: model = grid.best_estimator_
    yfit = model.predict(Xtest)

Рассмотрим некоторые из контрольных изображений и предсказанных для них значений (рис. 5.65):

![Прогнозируемые имена. Неверные метки выделены полужирным](https://i.imgur.com/5.65.png)

Рис. 5.65. Прогнозируемые имена. Неверные метки выделены полужирным