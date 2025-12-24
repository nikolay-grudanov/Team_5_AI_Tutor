---
source_image: page_521.png
page_number: 521
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 22.42
tokens: 7331
characters: 1431
timestamp: 2025-12-24T01:04:39.837531
finish_reason: stop
---

Для показанных на рис. 5.112 конкретных начальных значений кластеры сходятся всего за три итерации. Интерактивную версию рисунка можно увидеть в онлайн-приложении (https://github.com/jakevdp/PythonDataScienceHandbook).

Алгоритм k-средних достаточно прост для того, чтобы уместиться в нескольких строках кода. Вот простейшая его реализация (рис. 5.113):

In[5]: from sklearn.metrics import pairwise_distances_argmin

    def find_clusters(X, n_clusters, rseed=2):
        # 1. Выбираем кластеры случайным образом
        rng = np.random.RandomState(rseed)
        i = rng.permutation(X.shape[0])[:n_clusters]
        centers = X[i]

        while True:
            # 2a. Присваиваем метки в соответствии с ближайшим центром
            labels = pairwise_distances_argmin(X, centers)

            # 2b. Находим новые центры, исходя из средних значений точек
            new_centers = np.array([X[labels == i].mean(0)
                                    for i in range(n_clusters)])

            # 2c. Проверяем сходимость
            if np.all(centers == new_centers):
                break
            centers = new_centers

        return centers, labels

    centers, labels = find_clusters(X, 4)
    plt.scatter(X[:, 0], X[:, 1], c=labels,
                s=50, cmap='viridis');

![Данные, маркированные с помощью метода k-средних](../images/chapter_5/fig_5_113.png)

Рис. 5 113. Данные, маркированные с помощью метода k-средних