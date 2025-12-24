---
source_image: page_423.png
page_number: 423
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 24.56
tokens: 7366
characters: 1413
timestamp: 2025-12-24T01:02:09.432730
finish_reason: stop
---

Заметная особенность кривой обучения — сходимость к конкретному значению оценки при росте числа обучающих выборок. В частности, если количество точек достигло значения, при котором данная конкретная модель сошлась, то добавление новых обучающих данных не поможет! Единственным способом улучшить качество модели в этом случае будет использование другой (зачастую более сложной) модели.

Схематическое изображение кривой обучения

![Схематическое изображение кривой обучения](https://i.imgur.com/3Q5z5QG.png)

Рис. 5.32. Схематическое изображение типичной кривой обучения

Кривые обучения в библиотеке Scikit-Learn. Библиотека Scikit-Learn предоставляет удобные утилиты для вычисления кривых обучения для моделей. В этом разделе мы вычислим кривую обучения для нашего исходного набора данных с полиномиальными моделями второй и девятой степени (рис. 5.33):

In[17]:
from sklearn.learning_curve import learning_curve

fig, ax = plt.subplots(1, 2, figsize=(16, 6))
fig.subplots_adjust(left=0.0625, right=0.95, wspace=0.1)

for i, degree in enumerate([2, 9]):
    N, train_lc, val_lc = learning_curve(PolynomialRegression(degree),
        X, y, cv=7,
        train_sizes=np.linspace(0.3, 1, 25))

    ax[i].plot(N, np.mean(train_lc, 1), color='blue', label='training score')
    ax[i].plot(N, np.mean(val_lc, 1), color='red', label='validation score')
    ax[i].hlines(np.mean([train_lc[-1], val_lc[-1]]), N[0], N[-1],