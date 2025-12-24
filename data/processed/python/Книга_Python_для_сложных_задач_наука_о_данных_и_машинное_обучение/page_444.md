---
source_image: page_444.png
page_number: 444
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 20.95
tokens: 7288
characters: 1073
timestamp: 2025-12-24T01:02:39.069511
finish_reason: stop
---

444 Глава 5 • Машинное обучение

![Данные для линейной регрессии](./images/linearegression_data.png)

Рис. 5.42. Данные для линейной регрессии

In[2]: rng = np.random.RandomState(1)
    x = 10 * rng.rand(50)
    y = 2 * x - 5 + rng.randn(50)
    plt.scatter(x, y);

Воспользуемся оценивателем LinearRegression из библиотеки Scikit-Learn для обучения на этих данных и поиска оптимальной прямой (рис. 5.43):

In[3]: from sklearn.linear_model import LinearRegression
    model = LinearRegression(fit_intercept=True)

    model.fit(x[:, np.newaxis], y)

    xfit = np.linspace(0, 10, 1000)
    yfit = model.predict(xfit[:, np.newaxis])

    plt.scatter(x, y)
    plt.plot(xfit, yfit);

Подбираемые параметры модели (в библиотеке Scikit-Learn всегда содержат в конце знак подчеркивания) включают угловой коэффициент и точку пересечения с осью координат. В данном случае соответствующие параметры — coef_ и intercept_:

In[4]: print("Model slope:    ", model.coef_[0])
    print("Model intercept:", model.intercept_)

Model slope:    2.02720881036
Model intercept: -4.99857708555