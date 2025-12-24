---
source_image: page_294.png
page_number: 294
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 27.53
tokens: 7420
characters: 1640
timestamp: 2025-12-24T00:58:57.896181
finish_reason: stop
---

У функции plt.hexbin имеется множество интересных параметров, включая возможность задавать вес для каждой точки и менять выводимое значение для каждого интервала на любой сводный показатель библиотеки NumPy (среднее значение весов, стандартное отклонение весов и т. д.).

Ядерная оценка плотности распределения

Еще один часто используемый метод оценки плотностей в многомерном пространстве — ядерная оценка плотности распределения (kernel density estimation, KDE). Более подробно мы рассмотрим ее в разделе «Заглянем глубже: ядерная оценка плотности распределения» главы 5, а пока отметим, что KDE можно представлять как способ «размазать» точки в пространстве и сложить результаты для получения гладкой функции. В пакете scipy.stats имеется исключительно быстрая и простая реализация KDE. Вот короткий пример использования KDE на вышеуказанных данных (рис. 4.40):

In[10]: from scipy.stats import gaussian_kde

    # Выполняем подбор на массиве размера [Ndim, Nsamples]
    data = np.vstack([x, y])
    kde = gaussian_kde(data)

    # Вычисляем на регулярной координатной сетке
    xgrid = np.linspace(-3.5, 3.5, 40)
    ygrid = np.linspace(-6, 6, 40)
    Xgrid, Ygrid = np.meshgrid(xgrid, ygrid)
    Z = kde.evaluate(np.vstack([Xgrid.ravel(), Ygrid.ravel()]))

    # Выводим график результата в виде изображения
    plt.imshow(Z.reshape(Xgrid.shape),
        origin='lower', aspect='auto',
        extent=[-3.5, 3.5, -6, 6],
        cmap='Blues')
    cb = plt.colorbar()
    cb.set_label("density") # Плотность

![Ядерная оценка плотности распределения](https://i.imgur.com/3Q5z5QG.png)

Рис. 4.40. Ядерная оценка плотности распределения