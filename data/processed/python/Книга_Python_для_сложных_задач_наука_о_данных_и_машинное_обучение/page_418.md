---
source_image: page_418.png
page_number: 418
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 18.29
tokens: 7261
characters: 1088
timestamp: 2025-12-24T01:01:54.616956
finish_reason: stop
---

y += err * rng.randn(N)
return X, y

X, y = make_data(40)

Визуализируем наши данные вместе с несколькими аппроксимациями их многочленами различной степени (рис. 5.27):

In[12]: %matplotlib inline
    import matplotlib.pyplot as plt
    import seaborn; seaborn.set()  # plot formatting

    X_test = np.linspace(-0.1, 1.1, 500)[:, None]

    plt.scatter(X.ravel(), y, color='black')
    axis = plt.axis()
    for degree in [1, 3, 5]:
        y_test = PolynomialRegression(degree).fit(X, y).predict(X_test)
        plt.plot(X_test.ravel(), y_test, label='degree={0}'.format(degree))
    plt.xlim(-0.1, 1.0)
    plt.ylim(-2, 12)
    plt.legend(loc='best');

![Рис. 5.27. Аппроксимации набора данных тремя различными полиномиальными моделями](https://i.imgur.com/3Q5z5QG.png)

Параметром, служащим для управления сложностью модели, в данном случае является степень многочлена, которая может быть любым неотрицательным числом. Не помешает задать себе вопрос: какая степень многочлена обеспечивает подходящий компромисс между систематической ошибкой (недообучение) и дисперсией (переобучение)?