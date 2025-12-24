---
source_image: page_450.png
page_number: 450
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 25.70
tokens: 7365
characters: 1383
timestamp: 2025-12-24T01:02:52.975147
finish_reason: stop
---

Регуляризация

Применение базисных функций в нашей линейной модели делает ее намного гибче, но также и быстро приводит к переобучению (за подробностями обратитесь к разделу «Гиперпараметры и проверка модели» данной главы). Например, если выбрать слишком много Гауссовых базисных функций, мы в итоге получим не слишком хорошие результаты (рис. 5.47):

In[10]: model = make_pipeline(GaussianFeatures(30),
    LinearRegression())
model.fit(x[:, np.newaxis], y)
plt.scatter(x, y)
plt.plot(xfit, model.predict(xfit[:, np.newaxis]))
plt.xlim(0, 10)
plt.ylim(-1.5, 1.5);

![Пример переобучения на данных: слишком сложная модель с базисными функциями](../images/chapter5/fig_5_47.png)

Рис. 5.47. Пример переобучения на данных: слишком сложная модель с базисными функциями

В результате проекции данных на 30-мерный базис модель оказалась слишком уж гибкой и стремится к экстремальным значениям в промежутках между точками, в которых она ограничена данными. Причину этого можно понять, построив график коэффициентов Гауссовых базисных функций в соответствии с координатой x (рис. 5.48):

In[11]: def basis_plot(model, title=None):
    fig, ax = plt.subplots(2, sharex=True)
    model.fit(x[:, np.newaxis], y)
    ax[0].scatter(x, y)
    ax[0].plot(xfit, model.predict(xfit[:, np.newaxis]))
    ax[0].set(xlabel='x', ylabel='y', ylim=(-1.5, 1.5))

    if title:
        ax[0].set_title(title)