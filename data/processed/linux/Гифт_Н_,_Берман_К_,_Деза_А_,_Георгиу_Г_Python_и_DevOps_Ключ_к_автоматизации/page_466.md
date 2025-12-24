---
source_image: page_466.png
page_number: 466
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 26.49
tokens: 7419
characters: 1517
timestamp: 2025-12-24T03:13:05.149494
finish_reason: stop
---

-11.830068 (6.559724) with: {'n_estimators': 200}
-11.879805 (6.512414) with: {'n_estimators': 250}
-11.895362 (6.487726) with: {'n_estimators': 300}
-12.008611 (6.468623) with: {'n_estimators': 350}
-12.053759 (6.453899) with: {'n_estimators': 400}

/usr/local/lib/python3.6/dist-packages/sklearn/model_selection/_search.py:841:
DeprecationWarning:
DeprecationWarning)

Подгонка модели

Подгонку модели мы будем производить с помощью GradientBoostingRegressor. Последний шаг после обучения модели — только подгонка и проверка погрешности на выделенных данных. Данные масштабируются, передаются в модель, и оценивается показатель безошибочности по метрике «среднеквадратическая ошибка».

In[0]:

# Подготовка модели
scaler = StandardScaler().fit(X_train)
rescaledX = scaler.transform(X_train)
model = GradientBoostingRegressor(random_state=seed, n_estimators=400)
model.fit(rescaledX, Y_train)
# Преобразование проверочного набора данных
rescaledValidationX = scaler.transform(X_validation)
predictions = model.predict(rescaledValidationX)
print("Mean Squared Error: \n")
print(mean_squared_error(Y_validation, predictions))

Out[0]:

Mean Squared Error:

26.326748591395717

Оценка работы модели

Один из самых каверзных аспектов машинного обучения — оценка модели. Пример демонстрирует добавление в один и тот же объект DataFrame предсказаний и исходной цены на недвижимость. Далее на основе этого DataFrame можно вычислить разность между ними.

In[0]:

predictions=predictions.astype(int)
evaluate = pd.DataFrame({