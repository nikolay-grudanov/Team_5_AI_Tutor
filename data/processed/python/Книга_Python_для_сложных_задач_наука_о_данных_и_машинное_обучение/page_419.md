---
source_image: page_419.png
page_number: 419
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 23.16
tokens: 7341
characters: 1459
timestamp: 2025-12-24T01:02:02.044401
finish_reason: stop
---

Чтобы решить этот вопрос, визуализируем кривую проверки для этих конкретных данных и моделей. Проще всего сделать это с помощью предоставляемой библиотекой Scikit-Learn удобной утилиты validation_curve. Эта функция, получив на входе модель, данные, название параметра и диапазон для анализа, автоматически вычисляет в этом диапазоне значение как оценки эффективности для обучения, так и оценки эффективности для проверки (рис. 5.28):

In[13]:
from sklearn.learning_curve import validation_curve
degree = np.arange(0, 21)
train_score, val_score = validation_curve(PolynomialRegression(), X, y,
                                         'polynomialfeatures__degree',
                                         degree, cv=7)

plt.plot(degree, np.median(train_score, 1), color='blue',
         label='training score')   # Оценка обучения
plt.plot(degree, np.median(val_score, 1), color='red',
         label='validation score') # Оценка проверки
plt.legend(loc='best')
plt.ylim(0, 1)
plt.xlabel('degree') # Степень
plt.ylabel('score'); # Оценка

![Кривая проверки](https://i.imgur.com/3Q5z5QG.png)

Рис. 5.28. Кривая проверки для приведенных на рис. 5.27 данных (ср.: рис. 5.26)

Этот график в точности демонстрирует ожидаемое нами качественное поведение: оценка эффективности для обучения на всем диапазоне превышает оценку эффективности для проверки; оценка эффективности для обучения монотонно растет с ростом сложности модели, а оценка эффективности для проверки