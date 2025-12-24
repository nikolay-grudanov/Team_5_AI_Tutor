---
source_image: page_483.png
page_number: 483
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 20.27
tokens: 7287
characters: 1064
timestamp: 2025-12-24T01:03:38.556608
finish_reason: stop
---

Рассмотрим данные, полученные из сочетания быстрых и медленных колебаний (рис. 5.76):

In[10]: rng = np.random.RandomState(42)
    x = 10 * rng.rand(200)

    def model(x, sigma=0.3):
        fast_oscillation = np.sin(5 * x)
        slow_oscillation = np.sin(0.5 * x)
        noise = sigma * rng.randn(len(x))

        return slow_oscillation + fast_oscillation + noise

    y = model(x)
    plt.errorbar(x, y, 0.3, fmt='o');
    
![Данные для регрессии с помощью случайного леса](https://i.imgur.com/3Q5z5QG.png)

Рис. 5.76. Данные для регрессии с помощью случайного леса

Найти оптимальную аппроксимирующую кривую с помощью регрессии на основе случайного леса можно следующим образом (рис. 5.77):

In[11]: from sklearn.ensemble import RandomForestRegressor
    forest = RandomForestRegressor(200)
    forest.fit(x[:, None], y)

    xfit = np.linspace(0, 10, 1000)
    yfit = forest.predict(xfit[:, None])
    ytrue = model(xfit, sigma=0)

    plt.errorbar(x, y, 0.3, fmt='o', alpha=0.5)
    plt.plot(xfit, yfit, '-r');
    plt.plot(xfit, ytrue, '-k', alpha=0.5);