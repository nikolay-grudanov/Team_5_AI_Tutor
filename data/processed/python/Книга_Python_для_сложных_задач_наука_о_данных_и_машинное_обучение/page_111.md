---
source_image: page_111.png
page_number: 111
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 21.40
tokens: 7307
characters: 1065
timestamp: 2025-12-24T00:54:16.292115
finish_reason: stop
---

In[14]: %matplotlib inline
    import matplotlib.pyplot as plt
    import seaborn; seaborn.set()  # for plot styling

    plt.scatter(X[:, 0], X[:, 1]);

![Нормально распределенные точки](../images/ch2_7.png)

Рис. 2.7. Нормально распределенные точки

Воспользуемся «прихотливой» индексацией для выборки 20 случайных точек. Мы сделаем это с помощью выбора предварительно 20 случайных индексов без повторов и воспользуемся этими индексами для выбора части исходного массива:

In[15]: indices = np.random.choice(X.shape[0], 20, replace=False)
    indices

Out[15]: array([93, 45, 73, 81, 50, 10, 98, 94,  4, 64, 65, 89, 47, 84, 82,
                80, 25, 90, 63, 20])

In[16]: selection = X[indices]  # Тут используется «прихотливая» индексация
    selection.shape

Out[16]: (20, 2)

Чтобы посмотреть, какие точки были выбраны, нарисуем поверх первой диаграммы большие круги в местах расположения выбранных точек (рис. 2.8).

In[17]: plt.scatter(X[:, 0], X[:, 1], alpha=0.3)
    plt.scatter(selection[:, 0], selection[:, 1],
                facecolor='none', s=200);